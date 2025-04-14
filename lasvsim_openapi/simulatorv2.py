from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.simulator_model import (SimulatorConfig)
class SimulatorV2:    
    """Simulator client for the API."""

    http_client: HttpClient = None
    simulation_id: str = ""

    def __init__(self, http_client: HttpClient,sim_config: SimulatorConfig):
        """Initialize simulator client.

        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client.clone()

        reply = self.http_client.post(
            "/openapi/cosim/v2/simulation/init",
            {
                "scen_id": sim_config.scen_id,
                "scen_ver": sim_config.scen_ver,
                "sim_record_id": sim_config.sim_record_id,
            },
        )

        self.http_client.headers["x-md-simulation_id"] = reply['simulation_id'],
        self.http_client.headers["x-md-rl-direct-addr"] =  reply['simulation_addr']
        self.simulation_id =  reply['simulation_id']
    
    def step(self):
        """Step the simulation forward.

        Returns:
            dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/step",
            {"simulation_id": self.simulation_id},
        )
