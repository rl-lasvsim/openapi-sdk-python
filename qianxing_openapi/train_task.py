from http_client import HttpConfig, HttpClient
import response_struct


class TrainTask:
    def __init__(self, http_config: HttpConfig):
        client = HttpClient(http_config, {})
        self.client = client

    def get_scene_id_list(self, task_id: int):
        resp = self.client.get("/train_task/{}/scene_id_list".format(task_id), {})
        return response_struct.GetSceneIdListRes(resp)
