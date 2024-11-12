# 包含仿真器等功能的客户端

from simulator import Simulator, SimulatorConfig
from http_client import HttpConfig
from train_task import TrainTask


class Client(object):
    def __init__(self, config: HttpConfig):
        self.config = config

    def init_simulator_from_config(self, sim_config: SimulatorConfig):
        simulator = Simulator(self.config)
        simulator.init_from_config(sim_config)
        return simulator

    def init_train_task(self):
        return TrainTask(self.config)
