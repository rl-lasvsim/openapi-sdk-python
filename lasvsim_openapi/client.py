"""
Client module for the lasvsim API.
"""
from typing import Callable, Optional

from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.train_task import TrainTask
from lasvsim_openapi.resources import Resources
from lasvsim_openapi.process_task import ProcessTask
from lasvsim_openapi.simulator import Simulator, SimulatorConfig
from lasvsim_openapi.simulator_model import SchedulingStatusRes
from lasvsim_openapi.sim_record import SimRecord
from lasvsim_openapi.viewhelper import ViewHelper
from lasvsim_openapi.client_fast import ClientFast
from lasvsim_openapi.opensim import run_opensim

class Client:
    """Main client for the API."""
    train_task: TrainTask = None
    resources: Resources = None
    process_task: ProcessTask = None
    sim_record: SimRecord = None
    viewhelper: ViewHelper = None

    client_fast: ClientFast = None
    local_mode: bool = False

    def __init__(self, config: HttpConfig = None, local_mode: bool = False):
        """Initialize a new API client.
        
        Args:
            config: HTTP configuration for the client
        """
        if config is None and not local_mode:
            raise ValueError("HttpConfig is required unless local_mode is True")

        if local_mode:
            opensim_config = run_opensim()
            config = HttpConfig(endpoint=f"http://localhost:{opensim_config.run_port}", token="")

        self.local_mode = local_mode
        self.client_fast = ClientFast(config, local_mode=local_mode)
        self.init_common_client()

    def init_common_client(self):
        """Initialize the common client components."""
        self.train_task = TrainTask(self.client_fast.http_client)
        self.resources = Resources(self.client_fast.http_client)
        self.process_task = ProcessTask(self.client_fast.http_client)
        self.sim_record = SimRecord(self.client_fast.http_client)
        self.viewhelper = ViewHelper(self.client_fast.http_client)

    def init_simulator_from_config(
        self,
        sim_config: SimulatorConfig,
        timeout: float = 120.0,
        interval: float = 1.0,
        on_status: Optional[Callable[[SchedulingStatusRes], None]] = None,
    ) -> Simulator:
        """Initialize a simulator from the given configuration.

        提交仿真任务并等到就绪，返回可以直接驱动的仿真器（带任务号
        simulator.task_id）。排队/就绪的等待在 client_fast 里完成。

        Args:
            sim_config: Configuration for the simulator（场景、仿真记录、最大步数、控制类型）
            timeout: 最长等待就绪的秒数
            interval: 轮询调度状态的间隔秒数
            on_status: 每次轮询到调度状态时的回调，便于展示排队进度

        Returns:
            A new simulator instance（带仿真任务号 simulator.task_id）

        Raises:
            APIError: If the request fails
        """
        return Simulator(
            self.client_fast.init_simulator_from_config(
                sim_config,
                timeout=timeout,
                interval=interval,
                on_status=on_status,
            )
        )

    def init_simulator_from_sim(self, simulation_id: str, simulation_addr: str) -> Simulator:
        """Reconnect to an existing simulator session.
        
        Args:
            simulation_id: Existing simulation ID
            simulation_addr: Existing simulation address
            
        Returns:
            A simulator instance connected to the existing session
        """
        from lasvsim_openapi.simulator_fast import SimulatorFast
        sim_fast = SimulatorFast.from_session(
            self.client_fast.http_client, simulation_id, simulation_addr
        )
        return Simulator(sim_fast)
