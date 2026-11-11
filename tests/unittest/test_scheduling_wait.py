"""Tests for the wait performed inside client_fast's simulator init (no server needed)."""
from lasvsim_openapi.simulator import Simulator
from lasvsim_openapi.simulator_model import SchedulingState, SchedulingStatusRes


class _FakeScheduling:
    """提交后排队，等 ready 时才给出实例信息。"""

    def __init__(self, task_id=7, simulation_id="", simulation_addr="", state=None):
        from lasvsim_openapi.simulator_model import SchedulingState, SchedulingStatusRes

        self.task_id = task_id
        self.simulation_id = simulation_id
        self.simulation_addr = simulation_addr
        self.state = state or SchedulingState.RUNNING
        self.waited = []

    def wait_ready(self, task_id=0, simulation_id="", timeout=60.0, interval=1.0, on_status=None):
        from lasvsim_openapi.simulator_model import SchedulingStatusRes

        self.waited.append(task_id)
        return SchedulingStatusRes(
            task_id=task_id,
            state=self.state,
            simulation_id="sim",
            simulation_addr="addr",
        )


def _client_fast(task):
    from lasvsim_openapi.client_fast import ClientFast
    from lasvsim_openapi.http_client import HttpClient, HttpConfig

    client = ClientFast.__new__(ClientFast)
    client.http_client = HttpClient(HttpConfig(token="***", endpoint="http://localhost:1"))
    client.local_mode = False
    client.simulation_scheduling = task
    return client


def _config():
    from lasvsim_openapi.simulator import SimulatorConfig

    return SimulatorConfig(scen_id="scen", scen_ver="v1", sim_record_id="rec", max_step=10)


def _patch_init_v2(task, replies):
    """让提交走脚本结果，不真的发请求；返回恢复函数。"""
    from lasvsim_openapi.simulator_fast import SimulatorFast

    original = SimulatorFast.__dict__["init_v2"]

    def fake(cls, http_client, req):
        replies.append(req)
        return {
            "task_id": task.task_id,
            "simulation_id": task.simulation_id,
            "simulation_addr": task.simulation_addr,
        }

    SimulatorFast.init_v2 = classmethod(fake)

    def restore():
        SimulatorFast.init_v2 = original

    return restore


def test_fast_init_waits_until_ready():
    """Fast init submits, waits for scheduling, then hands back a ready simulator."""
    task = _FakeScheduling(task_id=7)
    client = _client_fast(task)
    requests = []
    restore = _patch_init_v2(task, requests)

    try:
        fast = client.init_simulator_from_config(_config(), timeout=5.0, interval=0)
    finally:
        restore()

    assert requests[0].scen_id == "scen"

    assert task.waited == [7]
    assert fast.task_id == 7
    assert fast.simulation_id == "sim"
    assert fast.simulation_addr == "addr"
    assert fast.http_client.headers["x-md-simulation_id"] == "sim"
    assert fast.http_client.headers["x-md-rl-direct-addr"] == "addr"


def test_fast_init_skips_wait_for_direct_deployment():
    """当提交就带实例信息时（直连部署），不再问调度状态。"""
    task = _FakeScheduling(task_id=0, simulation_id="sim", simulation_addr="addr")
    client = _client_fast(task)
    restore = _patch_init_v2(task, [])

    try:
        fast = client.init_simulator_from_config(_config(), interval=0)
    finally:
        restore()

    assert task.waited == []
    assert fast.simulation_id == "sim"
    assert fast.http_client.headers["x-md-rl-direct-addr"] == "addr"


def test_client_exposes_single_init_entry():
    """The client has one init entry, plus reconnect."""
    from lasvsim_openapi.client import Client
    from lasvsim_openapi.simulator_fast import SimulatorFast

    assert hasattr(Client, "init_simulator_from_config")
    assert hasattr(Client, "init_simulator_from_sim")
    # 等调度成功在 init 内部完成，不再单独暴露
    assert not hasattr(Client, "wait_scheduling_ready")
    assert not hasattr(Simulator, "wait_scheduling_ready")
    # 未就绪的仿真器不再由外部构造
    assert not hasattr(SimulatorFast, "from_task")


def test_init_simulator_from_sim_keeps_session():
    """Reconnecting to an existing instance keeps its session info."""
    from lasvsim_openapi.client import Client
    from lasvsim_openapi.client_fast import ClientFast
    from lasvsim_openapi.http_client import HttpConfig

    client = Client.__new__(Client)
    client.client_fast = ClientFast(
        HttpConfig(token="***", endpoint="http://localhost:1")
    )

    simulator = client.init_simulator_from_sim("sim", "addr")

    assert simulator.simulator_fast.simulation_id == "sim"
    assert simulator.simulator_fast.simulation_addr == "addr"
    assert simulator.ready is True
