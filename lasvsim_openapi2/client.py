from typing import Dict, Any
from lasvsim_openapi2.http_client import HttpClient
from lasvsim_openapi2.process_task import ProcessTask
from lasvsim_openapi2.resource import Resource
from lasvsim_openapi2.sim_record import SimRecord
from lasvsim_openapi2.simulator import Simulator
from lasvsim_openapi2.train_task import TrainTask

class Client:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.http_client = HttpClient(config)
        self.init_common_client()

    def init_common_client(self):
        self.train_task = TrainTask(self.http_client)
        self.resources = Resource(self.http_client)
        self.process_task = ProcessTask(self.http_client)
        self.sim_record = SimRecord(self.http_client)

    def init_simulator_from_config(self, sim_config) -> Simulator:
        return Simulator.from_config(self.http_client, sim_config)

    def init_simulator_from_sim(self, sim_id, addr) -> Simulator:
        return Simulator.from_sim(self.http_client, sim_id, addr)
