from http_client import HttpClient
import response_struct


class TrainTask:
    client: HttpClient

    def __init__(self, client: HttpClient):
        self.client = client

    def get_scene_id_list(self, task_id: int):
        resp = self.client.get("/train_task/{}/scene_id_list".format(task_id), {})
        return response_struct.GetSceneIdListRes(resp)
