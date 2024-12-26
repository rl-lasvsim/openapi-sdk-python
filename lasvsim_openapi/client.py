# 包含仿真器等功能的客户端

from lasvsim_openapi.simulator import Simulator, SimulatorConfig
from lasvsim_openapi.http_client import HttpConfig, HttpClient
from lasvsim_openapi.train_task import TrainTask
from lasvsim_openapi.resources import Resources
from lasvsim_openapi.process_task import ProcessTask
from lasvsim_openapi.sim_record import SimRecord


class Client(object):
    train_task: TrainTask
    resources: Resources
    process_task: ProcessTask
    sim_record: SimRecord

    def __init__(self, config: HttpConfig):
        self.config = config
        self.init_common_client(config)

    def init_common_client(self, config: HttpConfig):
        client = HttpClient(config, {})
        self.train_task = TrainTask(client)
        self.resources = Resources(client)
        self.process_task = ProcessTask(client)
        self.sim_record = SimRecord(client)

    def init_simulator_from_config(self, sim_config: SimulatorConfig):
        simulator = Simulator(self.config)
        simulator.init_from_config(sim_config)
        return simulator
