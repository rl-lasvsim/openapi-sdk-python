"""
Process task module for the lasvsim API.
"""
from typing import Optional

from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.process_task_fast import ProcessTaskFast
from lasvsim_openapi.process_task_model import (
    CopyRecordReq,
    CopyRecordRes,
    CreateTaskReq,
    CreateTaskRes,
    GetRecordScenarioReq,
    GetRecordScenarioRes,
    GetTaskRecordIdsReq,
    GetTaskRecordIdsRes,
    ScenarioRef,
)


class ProcessTask:
    """Process task client for the API."""
    process_task_fast: ProcessTaskFast

    def __init__(self, http_client: HttpClient):
        """Initialize process task client.
        
        Args:
            http_client: HTTP client instance
        """
        self.process_task_fast = ProcessTaskFast(http_client=http_client)

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
        reply = self.process_task_fast.copy_record(task_id=task_id, record_id=record_id)
        return CopyRecordRes.from_dict(reply)    

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
        reply = self.process_task_fast.get_record_scenario(task_id, record_id)
        return GetRecordScenarioRes.from_dict(reply)

    def get_task_record_ids(self, task_id: int) -> GetTaskRecordIdsRes:
        """Get task record IDs.
        
        Args:
            task_id: Task ID
            
        Returns:
            Get task record IDs response
            
        Raises:
            APIError: If the request fails
        """
        reply = self.process_task_fast.get_task_record_ids(task_id)
        return GetTaskRecordIdsRes.from_dict(reply)

    def create_task(self, name: str, scene_v2_infos: list, folder_id: int = 0, sim_type: int = 0) -> CreateTaskRes:
        """Create a simulation task.
        
        Args:
            name: Task name
            scene_v2_infos: List of ScenarioRef objects or dicts
            folder_id: Folder ID (optional)
            sim_type: Simulation type (0:None; 1:TaskSim; 2:RealTimeSim; 3:CoSim; 4:HILSim)
            
        Returns:
            Create task response
            
        Raises:
            APIError: If the request fails
        """
        reply = self.process_task_fast.create_task(
            name=name,
            scene_v2_infos=scene_v2_infos,
            folder_id=folder_id,
            sim_type=sim_type,
        )
        return CreateTaskRes.from_dict(reply)
