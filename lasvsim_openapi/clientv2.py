from typing import Optional

from lasvsim_openapi.http_client import HttpConfig, HttpClient
from lasvsim_openapi.simulatorv2 import *
class ClientV2:
    simulator: SimulatorV2 = None
    def __init__(self, config: HttpConfig):
        self.http_client = HttpClient(config)
    def init_simulator_from_config(self, sim_config: SimulatorConfig) -> SimulatorV2:
        """Initialize a simulator from the given configuration.
        
        Args:
            sim_config: Configuration for the simulator
            
        Returns:
            A new simulator instance
        """
        simulator = SimulatorV2(self.http_client)
        simulator.init_from_config(sim_config)
        return simulator