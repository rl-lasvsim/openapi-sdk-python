# 包含仿真器等功能的客户端

from simulator import Simulator, SimulatorConfig
from http_client import HttpConfig, HttpClient
from train_task import TrainTask


class Client(object):
    train_task: TrainTask

    def __init__(self, config: HttpConfig):
        self.config = config
        self.init_common_client(config)

    def init_common_client(self, config: HttpConfig):
        client = HttpClient(config, {})
        self.train_task = TrainTask(client)

    def init_simulator_from_config(self, sim_config: SimulatorConfig):
        simulator = Simulator(self.config)
        simulator.init_from_config(sim_config)
        return simulator
