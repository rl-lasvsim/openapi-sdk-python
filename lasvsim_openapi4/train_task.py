"""
Train task client.
"""
from typing import Optional
from lasvsim_openapi4.http_client import HttpClient
from lasvsim_openapi4.train_task_model import GetSceneIdListReq, GetSceneIdListRes


class TrainTask:
    """Train task client."""
    
    def __init__(self, http_client: HttpClient) -> None:
        """Initialize train task client.
        
        Args:
            http_client: HTTP client.
        """
        self.http_client = http_client.clone()

    def copy_record(self, task_id: int) -> Optional[GetSceneIdListRes]:
        """Copy record.
        
        Args:
            task_id: Task ID.
            
        Returns:
            GetSceneIdListRes if success, None otherwise.
        """
        req = GetSceneIdListReq(task_id=task_id)
        reply = self.http_client.post(
            "/openapi/train_task/{task_id}/scene_id_list",
            req,
            GetSceneIdListRes,
        )
        return reply
