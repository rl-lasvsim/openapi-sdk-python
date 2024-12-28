from typing import Optional
from .train_task_model import (
    GetSceneIdListReq,
    GetSceneIdListRes
)
from .httpclient import HttpClient
from .train_task_model import GetSceneIdListReq, GetSceneIdListRes

class TrainTask:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client.clone()

    def copy_record(self, task_id: int) -> Optional[GetSceneIdListRes]:
        req = GetSceneIdListReq(task_id=task_id)
        res = GetSceneIdListRes()
        self.http_client.post(
            "/openapi/train_task/{task_id}/scene_id_list",
            req,
            res
        )
        return res
