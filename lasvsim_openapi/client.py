"""
Client module for the lasvsim API.
"""
from typing import Optional

from lasvsim_openapi.http_client import HttpConfig, HttpClient
from lasvsim_openapi.train_task import TrainTask
from lasvsim_openapi.resources import Resources
from lasvsim_openapi.process_task import ProcessTask
from lasvsim_openapi.simulator import Simulator, SimulatorConfig
from lasvsim_openapi.sim_record import SimRecord


class Client:
    """Main client for the API."""
    config: HttpConfig = None
    http_client: HttpClient = None
    train_task: TrainTask = None
    resources: Resources = None
    process_task: ProcessTask = None
    simulator: Simulator = None
    sim_record: SimRecord = None

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

    def init_simulator_from_config(self, sim_config: SimulatorConfig) -> Simulator:
        """Initialize a simulator from the given configuration.
        
        Args:
            sim_config: Configuration for the simulator
            
        Returns:
            A new simulator instance
        """
        simulator = Simulator(self.http_client)
        simulator.init_from_config(sim_config)
        return simulator

    def init_simulator_from_sim(self, sim_id: str, addr: str) -> Simulator:
        """Initialize a simulator from existing simulation.
        
        Args:
            sim_id: ID of the existing simulation
            addr: Address of the simulation
            
        Returns:
            A new simulator instance
        """
        simulator = Simulator(self.http_client)
        simulator.init_from_sim(sim_id, addr)
        return simulator
