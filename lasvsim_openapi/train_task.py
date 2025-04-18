"""
Train task client.
"""
from typing import Optional
from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.train_task_model import GetSceneIdListReq, GetSceneIdListRes
from lasvsim_openapi.train_task_fast import TrainTaskFast


class TrainTask:
    """Train task client."""

    train_task_fast: TrainTaskFast
    
    def __init__(self, http_client: HttpClient) -> None:
        """Initialize train task client.
        
        Args:
            http_client: HTTP client.
        """
        self.train_task_fast = TrainTaskFast(http_client)

    def get_scene_id_list(self, task_id: int) -> GetSceneIdListRes:
        """Copy record.
        
        Args:
            task_id: Task ID
            
        Returns:
            Get scene ID list response
            
        Raises:
            APIError: If the request fails
        """
        reply = self.train_task_fast.get_scene_id_list(task_id)
        return GetSceneIdListRes.from_dict(reply)
