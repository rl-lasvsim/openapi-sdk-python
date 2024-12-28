from typing import Optional
from .process_task_model import (
    CopyRecordReq,
    CopyRecordRes,
    GetRecordScenarioReq,
    GetRecordScenarioRes,
    GetTaskRecordIdsReq,
    GetTaskRecordIdsRes
)
from .httpclient import HttpClient
from .process_task_model import (
    CopyRecordReq,
    CopyRecordRes,
    GetRecordScenarioReq,
    GetRecordScenarioRes,
    GetTaskRecordIdsReq,
    GetTaskRecordIdsRes
)

class ProcessTask:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client.clone()

    def copy_record(self, task_id: int, record_id: int) -> Optional[CopyRecordRes]:
        req = CopyRecordReq(task_id=task_id, record_id=record_id)
        res = CopyRecordRes()
        self.http_client.post(
            "/openapi/process_task/v2/record/copy",
            req,
            res
        )
        return res

    def get_record_scenario(self, task_id: int, record_id: int) -> Optional[GetRecordScenarioRes]:
        req = GetRecordScenarioReq(task_id=task_id, record_id=record_id)
        res = GetRecordScenarioRes()
        self.http_client.post(
            "/openapi/process_task/v2/record/scenario/get",
            req,
            res
        )
        return res

    def get_task_record_ids(self, task_id: int) -> Optional[GetTaskRecordIdsRes]:
        req = GetTaskRecordIdsReq(task_id=task_id)
        res = GetTaskRecordIdsRes()
        self.http_client.post(
            "/openapi/process_task/v2/record/id_list",
            req,
            res
        )
        return res
