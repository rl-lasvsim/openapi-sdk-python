from typing import Optional
from lasvsim_openapi2.http_client import HttpClient
from lasvsim_openapi2.process_task_model import (
    CopyRecordRes,
    CopyRecordReq,
    GetRecordScenarioRes,
    GetRecordScenarioReq,
    GetTaskRecordIdsRes,
    GetTaskRecordIdsReq
)

class ProcessTask:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def copy_record(self, task_id: int, record_id: int) -> Optional[CopyRecordRes]:
        """Copy a process task record"""
        try:
            response = self.http_client.post(
                "/openapi/process_task/v2/record/copy",
                CopyRecordReq(task_id=task_id, record_id=record_id)
            )
            return CopyRecordRes(**response)
        except Exception as e:
            print(f"Error copying record: {e}")
            return None

    def get_record_scenario(self, task_id: int, record_id: int) -> Optional[GetRecordScenarioRes]:
        """Get scenario for a process task record"""
        try:
            response = self.http_client.post(
                "/openapi/process_task/v2/record/scenario/get",
                GetRecordScenarioReq(task_id=task_id, record_id=record_id)
            )
            return GetRecordScenarioRes(**response)
        except Exception as e:
            print(f"Error getting record scenario: {e}")
            return None

    def get_task_record_ids(self, task_id: int) -> Optional[GetTaskRecordIdsRes]:
        """Get record IDs for a process task"""
        try:
            response = self.http_client.post(
                "/openapi/process_task/v2/record/id_list",
                GetTaskRecordIdsReq(task_id=task_id)
            )
            return GetTaskRecordIdsRes(**response)
        except Exception as e:
            print(f"Error getting task record IDs: {e}")
            return None
