"""
Client module for the lasvsim API.
"""
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.train_task import TrainTask
from lasvsim_openapi.resources import Resources
from lasvsim_openapi.process_task import ProcessTask
from lasvsim_openapi.simulator import Simulator, SimulatorConfig
from lasvsim_openapi.sim_record import SimRecord
from lasvsim_openapi.client_fast import ClientFast
from lasvsim_openapi.opensim import run_opensim

class Client:
    """Main client for the API."""
    train_task: TrainTask = None
    resources: Resources = None
    process_task: ProcessTask = None
    sim_record: SimRecord = None

    client_fast: ClientFast = None

    def __init__(self, config: HttpConfig = None, local_mode: bool = False):
        """Initialize a new API client.
        
        Args:
            config: HTTP configuration for the client
        """
        if config is None and not local_mode:
            raise ValueError("HttpConfig is required unless local_mode is True")

        if local_mode:
            opensim_config = run_opensim()
            config = HttpConfig(endpoint=f"http://localhost:{opensim_config.run_port}", token="")

        self.client_fast = ClientFast(config)
        self.init_common_client()

    def init_common_client(self):
        """Initialize the common client components."""
        self.train_task = TrainTask(self.client_fast.http_client)
        self.resources = Resources(self.client_fast.http_client)
        self.process_task = ProcessTask(self.client_fast.http_client)
        self.sim_record = SimRecord(self.client_fast.http_client)

    def init_simulator_from_config(self, sim_config: SimulatorConfig) -> Simulator:
        """Initialize a simulator from the given configuration.
        
        Args:
            sim_config: Configuration for the simulator
            
        Returns:
            A new simulator instance
        """
        simlator_v2 = self.client_fast.init_simulator_from_config(sim_config)
        simulator = Simulator(simlator_v2)
        return simulator
