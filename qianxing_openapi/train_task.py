from qianxing_openapi.http_client import HttpClient
from qianxing_openapi.response_model import GetSceneIdListRes


class TrainTask:
    client: HttpClient

    def __init__(self, client: HttpClient):
        self.client = client

    def get_scene_id_list(self, task_id: int):
        resp = self.client.get(
            "/openapi/train_task/{}/scene_id_list".format(task_id), {}
        )
        return GetSceneIdListRes(resp)
