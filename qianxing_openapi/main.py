from client import Client
from http_client import HttpConfig, HttpClient
from simulator import SimulatorConfig
from dataclasses import dataclass


data = {
    'id': 23,
    'config': {
        'scenario_id': 'gfdsfsf',
        'scenario_version': 'hhhhh',
        'record_id': 1
    },
    'reason': 'my reason',
}


class ErrorModel:
    code: int = 0
    message: str = ""
    reason: str = ""


class MyConfig:
    scenario_id: str
    scenario_version: str
    record_id: int
    # 如果不是必需的字段，需要设置默认值，保证from_dict成功执行。
    not_in_dict: str = None

    def __init__(self, data: dict):
        self.__dict__ = data

    def to_dict(self):
        return self.__dict__


# @dataclass
class MyTabl(ErrorModel):
    id: int
    config: MyConfig

    def __init__(self, data: dict):
        if (data == None):
            return
        config = data.pop('config', None)

        self.__dict__ = data
        self.config = MyConfig(config)


mt = MyTabl(data)


def myfunc() -> MyTabl:
    return mt


def cc():
    return mt


haha = myfunc()
print(mt.id, mt.reason)
print(mt.config.scenario_id)
print(haha.config)
print(haha.config.to_dict())
# hclient = HttpClient(config=HttpConfig(
#     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjE3LCJvaWQiOjI1LCJuYW1lIjoiYWRtaW4iLCJpZGVudGl0eSI6ImFkbWluIiwicGVybWlzc2lvbnMiOltdLCJpc3MiOiJ1c2VyIiwic3ViIjoiTGFzVlNpbSIsImV4cCI6MTczMDc4NzUyNSwibmJmIjoxNzMwMTgyNzI1LCJpYXQiOjE3MzAxODI3MjUsImp0aSI6IjE3In0.Z_eRvOqBIkpJrteM0L4jb9JSmtoa5bFkSz9RLMptcCQ", "http://8.146.201.197:30080"), headers={})
# resp = hclient.post("/dev/api/viewhelper/tableheader/get",
#                     data={"table_code": "LISTCODE_TASK"}, object_hook=MyTabl)
# print(resp)

# api_client = Client(HttpConfig(
#     token="your_token",
#     endpoint="http://localhost:8050/openapi"
# ))

# api_client.InitSimulator(SimulatorConfig(
#     scenario_id="your_scenario_id", scenario_version="your_scenario_version"))
