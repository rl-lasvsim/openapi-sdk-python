from typing import Optional
from lasvsim_openapi2.http_client import HttpClient
from lasvsim_openapi2.train_task_model import GetSceneIdListRes, GetSceneIdListReq

class TrainTask:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def copy_record(self, task_id: int) -> Optional[GetSceneIdListRes]:
        """Copy record for a training task"""
        try:
            response = self.http_client.post(
                f"/openapi/train_task/{task_id}/scene_id_list",
                GetSceneIdListReq(task_id=task_id)
            )
            return GetSceneIdListRes(**response)
        except Exception as e:
            print(f"Error copying training task record: {e}")
            return None
