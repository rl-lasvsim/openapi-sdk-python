from qianxing_openapi.http_client import HttpClient
from qianxing_openapi import sim_record_model


class SimRecord:
    client: HttpClient

    def __init__(self, client: HttpClient):
        self.client = client

    def get_record_ids(
        self, scen_id: str, scen_ver: str
    ) -> sim_record_model.GetRecordIdsResp:
        resp = self.client.post(
            "/openapi/sim_record/v1/ids/get",
            {"scen_id": scen_id, "scen_ver": scen_ver},
        )
        return sim_record_model.GetRecordIdsResp(resp)

    def get_track_results(
        self, id: str, obj_id: str
    ) -> sim_record_model.GetTrackResultsResp:
        resp = self.client.post(
            "/openapi/sim_record/v1/track_result/get",
            {"id": id, "obj_id": obj_id},
        )
        return sim_record_model.GetTrackResultsResp(resp)

    def get_sensor_results(
        self, id: str, obj_id: str
    ) -> sim_record_model.GetSensorResultsResp:
        resp = self.client.post(
            "/openapi/sim_record/v1/sensor_result/get",
            {"id": id, "obj_id": obj_id},
        )
        return sim_record_model.GetSensorResultsResp(resp)

    def get_step_results(
        self, id: str, obj_id: str
    ) -> sim_record_model.GetStepResultsResp:
        resp = self.client.post(
            "/openapi/sim_record/v1/step_result/get",
            {"id": id, "obj_id": obj_id},
        )
        return sim_record_model.GetStepResultsResp(resp)

    def get_path_results(
        self, id: str, obj_id: str
    ) -> sim_record_model.GetPathResultsResp:
        resp = self.client.post(
            "/openapi/sim_record/v1/path_result/get",
            {"id": id, "obj_id": obj_id},
        )
        return sim_record_model.GetPathResultsResp(resp)

    def get_reference_line_results(
        self, id: str, obj_id: str
    ) -> sim_record_model.GetReferenceLineResultsResp:
        resp = self.client.post(
            "/openapi/sim_record/v1/reference_line_result/get",
            {"id": id, "obj_id": obj_id},
        )
        return sim_record_model.GetReferenceLineResultsResp(resp)
