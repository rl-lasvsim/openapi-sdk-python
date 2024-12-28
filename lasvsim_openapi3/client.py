from dataclasses import dataclass
from typing import Optional
from .httpclient import HttpClient, HttpConfig
from .processtask import ProcessTask
from .resource import Resource
from .simrecord import SimRecord
from .simulation import Simulator
from .traintask import TrainTask
from .simulation_model import SimulatorConfig

@dataclass
class Client:
    config: HttpConfig
    http_client: Optional[HttpClient] = None
    train_task: Optional[TrainTask] = None
    resources: Optional[Resource] = None
    process_task: Optional[ProcessTask] = None
    simulator: Optional[Simulator] = None
    sim_record: Optional[SimRecord] = None

    def __init__(self, config: HttpConfig):
        self.config = config
        self.http_client = HttpClient(config)
        self.init_common_client()

    def init_common_client(self):
        self.train_task = TrainTask(self.http_client)
        self.resources = Resource(self.http_client)
        self.process_task = ProcessTask(self.http_client)
        self.sim_record = SimRecord(self.http_client)

    def init_simulator_from_config(self, sim_config: SimulatorConfig) -> Optional[Simulator]:
        return Simulator.from_config(self.http_client, sim_config)

    def init_simulator_from_sim(self, sim_id: str, addr: str) -> Optional[Simulator]:
        return Simulator.from_sim(self.http_client, sim_id, addr)
