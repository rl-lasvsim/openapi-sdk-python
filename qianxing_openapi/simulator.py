
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
            "/cosim/v2/simulation/task/record_ids/get", sim_config.__dict__)
        print(res)
