"""Tests for the scheduling task API models (no server needed)."""
from lasvsim_openapi.simulator_model import (
    InitV2Req,
    InitV2Res,
    SchedulingStatusReq,
    SchedulingStatusRes,
    SchedulingState,
)


def test_submit_task_req_to_dict():
    """Request carries the scenario and the control type."""
    req = InitV2Req(
        scen_id="scen",
        scen_ver="1.0",
        sim_record_id="rec",
        max_step=600,
        ctrl_type=3,
    )
    data = req.to_dict()
    assert data["scen_id"] == "scen"
    assert data["scen_ver"] == "1.0"
    assert data["sim_record_id"] == "rec"
    assert data["max_step"] == 600
    assert data["ctrl_type"] == 3


def test_submit_task_res_from_dict():
    """Response carries the task id and the instance info."""
    res = InitV2Res.from_dict(
        {"task_id": 16, "simulation_id": "sim", "simulation_addr": "addr"}
    )
    assert res.task_id == 16
    assert res.simulation_id == "sim"
    assert res.simulation_addr == "addr"


def test_task_status_res_states():
    """Only the running state means the instance is ready."""
    pending = SchedulingStatusRes.from_dict({"task_id": 16, "state": SchedulingState.PENDING})
    running = SchedulingStatusRes.from_dict({"task_id": 16, "state": SchedulingState.RUNNING})
    finished = SchedulingStatusRes.from_dict({"task_id": 16, "state": SchedulingState.FINISHED})

    assert pending.ready is False
    assert running.ready is True
    assert finished.ready is False


def test_task_status_req_to_dict():
    """Query carries the task id (0 for direct deployments)."""
    assert SchedulingStatusReq(task_id=0).to_dict() == {"task_id": 0, "simulation_id": ""}
    assert SchedulingStatusReq(task_id=3, simulation_id="sim").to_dict() == {
        "task_id": 3,
        "simulation_id": "sim",
    }


def test_simulator_carries_task_id():
    """The simulator keeps the scheduling task id, so callers can query scheduling status."""
    from lasvsim_openapi.http_client import HttpClient, HttpConfig
    from lasvsim_openapi.simulator import Simulator
    from lasvsim_openapi.simulator_fast import SimulatorFast

    http_client = HttpClient(HttpConfig(token="test-token", endpoint="http://localhost:1"))
    sim_fast = SimulatorFast.from_session(http_client, "sim-id", "addr", task_id=16)
    simulator = Simulator(sim_fast)

    assert simulator.task_id == 16
    assert simulator.simulator_fast.task_id == 16


def test_simulator_config_carries_max_step_and_ctrl_type():
    """Config passes the step limit and the control type to the simulation task."""
    from lasvsim_openapi.simulator_model import SimulatorConfig

    config = SimulatorConfig("scen", "1.0", "rec", max_step=600, ctrl_type=3)
    assert config.max_step == 600
    assert config.ctrl_type == 3
