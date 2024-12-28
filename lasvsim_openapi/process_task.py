"""
Process task module for the lasvsim API.
"""
from typing import Optional

from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.process_task_model import (
    CopyRecordReq,
    CopyRecordRes,
    GetRecordScenarioReq,
    GetRecordScenarioRes,
    GetTaskRecordIdsReq,
    GetTaskRecordIdsRes,
)


class ProcessTask:
    """Process task client for the API."""
    http_client: HttpClient = None

    def __init__(self, http_client: HttpClient):
        """Initialize process task client.
        
        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client.clone()

    def copy_record(self, task_id: int, record_id: int) -> CopyRecordRes:
        """Copy a record.
        
        Args:
            task_id: Task ID
            record_id: Record ID
            
        Returns:
            Copy record response
            
        Raises:
            APIError: If the request fails
        """
        req = CopyRecordReq(task_id=task_id, record_id=record_id)
        
        return self.http_client.post(
            "/openapi/process_task/v2/record/copy",
            {"task_id": req.task_id, "record_id": req.record_id},
            CopyRecordRes
        )        

    def get_record_scenario(self, task_id: int, record_id: int) -> GetRecordScenarioRes:
        """Get record scenario.
        
        Args:
            task_id: Task ID
            record_id: Record ID
            
        Returns:
            Get record scenario response
            
        Raises:
            APIError: If the request fails
        """
        req = GetRecordScenarioReq(task_id=task_id, record_id=record_id)
        
        return self.http_client.post(
            "/openapi/process_task/v2/record/scenario/get",
            {"task_id": req.task_id, "record_id": req.record_id},
            GetRecordScenarioRes
        )

    def get_task_record_ids(self, task_id: int) -> GetTaskRecordIdsRes:
        """Get task record IDs.
        
        Args:
            task_id: Task ID
            
        Returns:
            Get task record IDs response
            
        Raises:
            APIError: If the request fails
        """
        req = GetTaskRecordIdsReq(task_id=task_id)
        
        return self.http_client.post(
            "/openapi/process_task/v2/record/id_list",
            {"task_id": req.task_id},
            GetTaskRecordIdsRes
        )
