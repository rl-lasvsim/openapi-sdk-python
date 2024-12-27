from typing import Optional
from lasvsim_openapi2.http_client import HttpClient
from lasvsim_openapi2.sim_record_model import (
    GetRecordIdsRes,
    GetRecordIdsReq,
    GetTrackResultsRes,
    GetTrackResultsReq,
    GetSensorResultsRes,
    GetSensorResultsReq,
    GetStepResultsRes,
    GetStepResultsReq,
    GetPathResultsRes,
    GetPathResultsReq,
    GetReferenceLineResultsRes,
    GetReferenceLineResultsReq
)

class SimRecord:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def get_record_ids(self, scen_id: str, scen_ver: str) -> Optional[GetRecordIdsRes]:
        """Get record IDs for a scenario"""
        try:
            response = self.http_client.post(
                "/openapi/sim_record/v1/ids/get",
                GetRecordIdsReq(scen_id=scen_id, scen_ver=scen_ver)
            )
            return GetRecordIdsRes(**response)
        except Exception as e:
            print(f"Error getting record IDs: {e}")
            return None

    def get_track_results(self, id: str, obj_id: str) -> Optional[GetTrackResultsRes]:
        """Get track results for a record"""
        try:
            response = self.http_client.post(
                "/openapi/sim_record/v1/track_result/get",
                GetTrackResultsReq(id=id, obj_id=obj_id)
            )
            return GetTrackResultsRes(**response)
        except Exception as e:
            print(f"Error getting track results: {e}")
            return None

    def get_sensor_results(self, id: str, obj_id: str) -> Optional[GetSensorResultsRes]:
        """Get sensor results for a record"""
        try:
            response = self.http_client.post(
                "/openapi/sim_record/v1/sensor_result/get",
                GetSensorResultsReq(id=id, obj_id=obj_id)
            )
            return GetSensorResultsRes(**response)
        except Exception as e:
            print(f"Error getting sensor results: {e}")
            return None

    def get_step_results(self, id: str, obj_id: str) -> Optional[GetStepResultsRes]:
        """Get step results for a record"""
        try:
            response = self.http_client.post(
                "/openapi/sim_record/v1/step_result/get",
                GetStepResultsReq(id=id, obj_id=obj_id)
            )
            return GetStepResultsRes(**response)
        except Exception as e:
            print(f"Error getting step results: {e}")
            return None

    def get_path_results(self, id: str, obj_id: str) -> Optional[GetPathResultsRes]:
        """Get path results for a record"""
        try:
            response = self.http_client.post(
                "/openapi/sim_record/v1/path_result/get",
                GetPathResultsReq(id=id, obj_id=obj_id)
            )
            return GetPathResultsRes(**response)
        except Exception as e:
            print(f"Error getting path results: {e}")
            return None

    def get_reference_line_results(self, id: str, obj_id: str) -> Optional[GetReferenceLineResultsRes]:
        """Get reference line results for a record"""
        try:
            response = self.http_client.post(
                "/openapi/sim_record/v1/reference_line_result/get",
                GetReferenceLineResultsReq(id=id, obj_id=obj_id)
            )
            return GetReferenceLineResultsRes(**response)
        except Exception as e:
            print(f"Error getting reference line results: {e}")
            return None
