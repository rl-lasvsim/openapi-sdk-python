from typing import Optional

from lasvsim_openapi.http_client import HttpConfig, HttpClient
from lasvsim_openapi.simulator_fast import *
from lasvsim_openapi.http_client import HttpConfig, HttpClient
from lasvsim_openapi.train_task import TrainTask
from lasvsim_openapi.resources import Resources
from lasvsim_openapi.process_task import ProcessTask
from lasvsim_openapi.simulator import SimulatorConfig
from lasvsim_openapi.sim_record import SimRecord

class ClientFast:
    simulator: SimulatorFast = None
    def __init__(self, config: HttpConfig):
        """Initialize a new API client.
        
        Args:
            config: HTTP configuration for the client
        """
        self.config = config
        self.http_client = HttpClient(config)
        self.init_common_client()

    def init_common_client(self):
        """Initialize the common client components."""
        self.train_task = TrainTask(self.http_client)
        self.resources = Resources(self.http_client)
        self.process_task = ProcessTask(self.http_client)
        self.sim_record = SimRecord(self.http_client)

    def init_simulator_from_config(self, sim_config: SimulatorConfig) -> SimulatorFast:
        """Initialize a simulator from the given configuration.
        
        Args:
            sim_config: Configuration for the simulator
            
        Returns:
            A new simulator instance
        """
        simulator = SimulatorFast(http_client=self.http_client,sim_config = sim_config    )
        return simulator