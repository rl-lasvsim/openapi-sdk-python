from qianxing_openapi.http_client import HttpClient
from dataclasses import dataclass


class TrainTask:
    client: HttpClient

    def __init__(self, client: HttpClient):
        self.client = client

    def get_scene_id_list(self, task_id: int):
        resp = self.client.get(
            "/openapi/train_task/{}/scene_id_list".format(task_id), {}
        )
        return GetSceneIdListRes(resp)


@dataclass
class GetSceneIdListRes:
    scene_id_list: list[str] = None
    scene_version_list: list[str] = None

    def __init__(self, data: dict):
        if data == None:
            return
        self.__dict__ = data
