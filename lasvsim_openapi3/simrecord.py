from typing import List, Optional
from .sim_record_model import (
    GetRecordIdsReq,
    GetRecordIdsRes,
    GetTrackResultsReq,
    GetTrackResultsRes,
    GetSensorResultsReq,
    GetSensorResultsRes,
    GetStepResultsReq,
    GetStepResultsRes,
    GetPathResultsReq,
    GetPathResultsRes,
    GetReferenceLineResultsReq,
    GetReferenceLineResultsRes,
    Track,
    TrackResult,
    SensorObj,
    SensorResult,
    Step,
    StepResult,
    PathPoint,
    Path,
    PathResult,
    ReferenceLine,
    ReferenceLineResult
)
from .httpclient import HttpClient

class SimRecord:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client.clone()

    def get_record_ids(self, scen_id: str, scen_ver: str) -> Optional[List[str]]:
        req = GetRecordIdsReq(scen_id=scen_id, scen_ver=scen_ver)
        res = GetRecordIdsRes()
        self.http_client.post(
            "/openapi/sim_record/v1/ids/get",
            req,
            res
        )
        return res.ids

    def get_track_results(self, id: str, obj_id: str) -> Optional[GetTrackResultsRes]:
        req = GetTrackResultsReq(id=id, obj_id=obj_id)
        res = GetTrackResultsRes()
        self.http_client.post(
            "/openapi/sim_record/v1/track_result/get",
            req,
            res
        )
        return res

    def get_sensor_results(self, id: str, obj_id: str) -> Optional[GetSensorResultsRes]:
        req = GetSensorResultsReq(id=id, obj_id=obj_id)
        res = GetSensorResultsRes()
        self.http_client.post(
            "/openapi/sim_record/v1/sensor_result/get",
            req,
            res
        )
        return res

    def get_step_results(self, id: str, obj_id: str) -> Optional[GetStepResultsRes]:
        req = GetStepResultsReq(id=id, obj_id=obj_id)
        res = GetStepResultsRes()
        self.http_client.post(
            "/openapi/sim_record/v1/step_result/get",
            req,
            res
        )
        return res

    def get_path_results(self, id: str, obj_id: str) -> Optional[GetPathResultsRes]:
        req = GetPathResultsReq(id=id, obj_id=obj_id)
        res = GetPathResultsRes()
        self.http_client.post(
            "/openapi/sim_record/v1/path_result/get",
            req,
            res
        )
        return res

    def get_reference_line_results(self, id: str, obj_id: str) -> Optional[GetReferenceLineResultsRes]:
        req = GetReferenceLineResultsReq(id=id, obj_id=obj_id)
        res = GetReferenceLineResultsRes()
        self.http_client.post(
            "/openapi/sim_record/v1/reference_line_result/get",
            req,
            res
        )
        return res
