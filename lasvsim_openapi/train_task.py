"""
Train task client.
"""
from typing import Optional
from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.train_task_model import GetSceneIdListReq, GetSceneIdListRes


class TrainTask:
    """Train task client."""
    
    def __init__(self, http_client: HttpClient) -> None:
        """Initialize train task client.
        
        Args:
            http_client: HTTP client.
        """
        self.http_client = http_client.clone()

    def copy_record(self, task_id: int) -> GetSceneIdListRes:
        """Copy record.
        
        Args:
            task_id: Task ID
            
        Returns:
            Get scene ID list response
            
        Raises:
            APIError: If the request fails
        """
        req = GetSceneIdListReq(task_id=task_id)
        
        return self.http_client.post(
            "/openapi/train_task/v2/record/copy",
            {"task_id": req.task_id},
            GetSceneIdListRes
        )
