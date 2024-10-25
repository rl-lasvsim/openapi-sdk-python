from client import Client
from http_client import HttpConfig
from simulator import SimulatorConfig

api_client = Client(HttpConfig(
    token="your_token",
    endpoint="http://localhost:8050/openapi"
))

api_client.InitSimulator(SimulatorConfig(
    scenario_id="your_scenario_id", scenario_version="your_scenario_version"))
