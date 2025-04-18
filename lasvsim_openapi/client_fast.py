from typing import Optional

from lasvsim_openapi.http_client import HttpConfig, HttpClient
from lasvsim_openapi.simulator_fast import *
from lasvsim_openapi.http_client import HttpConfig, HttpClient
from lasvsim_openapi.train_task_fast import TrainTaskFast
from lasvsim_openapi.resources_fast import ResourcesFast
from lasvsim_openapi.process_task_fast import ProcessTaskFast
from lasvsim_openapi.simulator import SimulatorConfig
from lasvsim_openapi.sim_record_fast import SimRecordFast

class ClientFast:
    config: HttpConfig = None
    http_client: HttpClient = None

    train_task: TrainTaskFast = None
    resources: ResourcesFast = None
    process_task: ProcessTaskFast = None
    sim_record: SimRecordFast = None

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
        self.train_task = TrainTaskFast(self.http_client)
        self.resources = ResourcesFast(self.http_client)
        self.process_task = ProcessTaskFast(self.http_client)
        self.sim_record = SimRecordFast(self.http_client)

    def init_simulator_from_config(self, sim_config: SimulatorConfig) -> SimulatorFast:
        """Initialize a simulator from the given configuration.
        
        Args:
            sim_config: Configuration for the simulator
            
        Returns:
            A new simulator instance
        """
        simulator = SimulatorFast(http_client=self.http_client, sim_config = sim_config)
        return simulator