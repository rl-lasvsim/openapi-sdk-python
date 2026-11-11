from typing import Optional, Callable

from lasvsim_openapi.http_client import HttpConfig, HttpClient
from lasvsim_openapi.simulator_fast import *
from lasvsim_openapi.http_client import HttpConfig, HttpClient
from lasvsim_openapi.train_task_fast import TrainTaskFast
from lasvsim_openapi.resources_fast import ResourcesFast
from lasvsim_openapi.process_task_fast import ProcessTaskFast
from lasvsim_openapi.simulator import SimulatorConfig, SimulationScheduling
from lasvsim_openapi.simulator_model import InitV2Req, InitV2Res, SchedulingStatusRes
from lasvsim_openapi.sim_record_fast import SimRecordFast
from lasvsim_openapi.viewhelper_fast import ViewHelperFast

class ClientFast:
    config: HttpConfig = None
    http_client: HttpClient = None
    local_mode: bool = False

    train_task: TrainTaskFast = None
    resources: ResourcesFast = None
    process_task: ProcessTaskFast = None
    sim_record: SimRecordFast = None
    viewhelper: ViewHelperFast = None
    simulation_scheduling: SimulationScheduling = None

    def __init__(self, config: HttpConfig, local_mode: bool = False):
        """Initialize a new API client.

        Args:
            config: HTTP configuration for the client
            local_mode: 本地模式（仿真器在进程内跑，没有调度平台）
        """
        self.config = config
        self.local_mode = local_mode
        self.http_client = HttpClient(config)
        self.init_common_client()

    def init_common_client(self):
        """Initialize the common client components."""
        self.train_task = TrainTaskFast(self.http_client)
        self.resources = ResourcesFast(self.http_client)
        self.process_task = ProcessTaskFast(self.http_client)
        self.sim_record = SimRecordFast(self.http_client)
        self.viewhelper = ViewHelperFast(self.http_client)
        self.simulation_scheduling = SimulationScheduling(self.http_client)

    def init_simulator_from_config(
        self,
        sim_config: SimulatorConfig,
        timeout: float = 120.0,
        interval: float = 1.0,
        on_status: Optional[Callable[[SchedulingStatusRes], None]] = None,
    ) -> SimulatorFast:
        """提交仿真任务并等它就绪，返回可以驱动的仿真器。

        远端部署走「提交仿真任务 → 等调度成功」两步，提交后实例要经过调度
        才会起来，这里会等到就绪再返回。直连部署提交时就带实例信息，不必再问。
        本地部署没有调度平台，仿真器在进程内跑，走老的 init 接口，提交即就绪。

        Args:
            sim_config: Configuration for the simulator
            timeout: 最长等待就绪的秒数
            interval: 轮询调度状态的间隔秒数
            on_status: 每次轮询到调度状态时的回调，便于展示排队进度

        Returns:
            已就绪的仿真器实例
        """
        if self.local_mode:
            return SimulatorFast(http_client=self.http_client, sim_config=sim_config)

        reply = SimulatorFast.init_v2(
            self.http_client,
            InitV2Req(
                scen_id=sim_config.scen_id,
                scen_ver=sim_config.scen_ver,
                sim_record_id=sim_config.sim_record_id,
                max_step=sim_config.max_step,
                ctrl_type=sim_config.ctrl_type,
            ),
        )
        task = InitV2Res.from_dict(reply)

        # 直连部署提交时实例就已经在了，不用再去问调度状态。
        if task.simulation_id and task.simulation_addr:
            return SimulatorFast.from_session(
                self.http_client,
                task.simulation_id,
                task.simulation_addr,
                task_id=task.task_id,
            )

        status = self.simulation_scheduling.wait_ready(
            task_id=task.task_id,
            timeout=timeout,
            interval=interval,
            on_status=on_status,
        )
        return SimulatorFast.from_session(
            self.http_client,
            status.simulation_id,
            status.simulation_addr,
            task_id=task.task_id,
        )