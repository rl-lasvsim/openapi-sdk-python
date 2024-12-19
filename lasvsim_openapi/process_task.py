from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi import process_task_model


class ProcessTask:
    client: HttpClient

    def __init__(self, client: HttpClient):
        self.client = client

    def copy_record(
        self,
        task_id: int = None,
        record_id: int = None,
    ) -> process_task_model.CopyRecordRes:
        req_data = {"task_id": task_id, "record_id": record_id}
        resp = self.client.post(
            "/openapi/process_task/v2/record/copy", req_data)

        return process_task_model.CopyRecordRes(resp)

    def get_record_scenario(
        self,
        task_id: int = None,
        record_id: int = None,
    ) -> process_task_model.GetRecordScenarioRes:
        req_data = {"task_id": task_id, "record_id": record_id}
        resp = self.client.post(
            "/openapi/process_task/v2/record/scenario/get", req_data
        )

        return process_task_model.GetRecordScenarioRes(resp)

    def get_task_record_ids(
        self,
        task_id: int = None,
    ) -> process_task_model.GetTaskRecordIdsRes:
        req_data = {"task_id": task_id}
        print("rr", req_data)
        resp = self.client.post(
            "/openapi/process_task/v2/record/id_list", req_data)
        print("eeee", resp)
        return process_task_model.GetTaskRecordIdsRes(resp)
