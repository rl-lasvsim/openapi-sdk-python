
from http_client import HttpConfig, HttpClient


class SimulatorConfig(object):
    def __init__(self, scenario_id: str = None, scenario_version: str = None, record_id: int = None):
        self.scenario_id = scenario_id
        self.scenario_version = scenario_version
        self.record_id = record_id


class Simulator(object):
    def __init__(self, http_config: HttpConfig, sim_config: SimulatorConfig):
        client = HttpClient(http_config, {})
        res = client.post(
            "/cosim/v2/simulation/init", sim_config.__dict__)
        client.headers["simulation_id"] = res.get("simulation_id")
        client.headers["rl-direct-addr"] = res.get("simulation_addr")
        self.client = client
        self.simulation_id = res.get("simulation_id")

    def step(self,):
        return self.client.post("/cosim/v2/simulation/step", {'simulation_id': self.simulation_id})
