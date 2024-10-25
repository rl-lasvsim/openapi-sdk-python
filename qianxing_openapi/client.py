# 包含仿真器等功能的客户端

from simulator import Simulator, SimulatorConfig
from http_client import HttpConfig


class Client(object):
    def __init__(self, config: HttpConfig):
        self.config = config

    def InitSimulator(self, sim_config: SimulatorConfig):
        return Simulator(self.config, sim_config)
