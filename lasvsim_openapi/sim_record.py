"""
Simulation record module for the lasvsim API.
"""
from typing import Optional

from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.sim_record_model import (
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
)


class SimRecord:
    """Simulation record client for the API."""
    http_client: HttpClient = None

    def __init__(self, http_client: HttpClient):
        """Initialize simulation record client.
        
        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client.clone()

    def get_record_ids(self, scen_id: str, scen_ver: str) -> GetRecordIdsRes:
        """Get record IDs.
        
        Args:
            scen_id: Scenario ID
            scen_ver: Scenario version
            
        Returns:
            Record IDs response
            
        Raises:
            APIError: If the request fails
        """
        req = GetRecordIdsReq(scen_id=scen_id, scen_ver=scen_ver)
        
        return self.http_client.post(
            "/openapi/sim_record/v1/ids/get",
            {"scen_id": req.scen_id, "scen_ver": req.scen_ver},
            GetRecordIdsRes
        )

    def get_track_results(self, id: str, obj_id: str) -> GetTrackResultsRes:
        """Get track results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Get track results response
            
        Raises:
            APIError: If the request fails
        """
        req = GetTrackResultsReq(id=id, obj_id=obj_id)
        
        return self.http_client.post(
            "/openapi/sim_record/v2/track/get",
            {"id": req.id, "obj_id": req.obj_id},
            GetTrackResultsRes
        )

    def get_sensor_results(self, id: str, obj_id: str) -> GetSensorResultsRes:
        """Get sensor results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Sensor results response
            
        Raises:
            APIError: If the request fails
        """
        req = GetSensorResultsReq(id=id, obj_id=obj_id)
        
        return self.http_client.post(
            "/openapi/sim_record/v1/sensor_result/get",
            {"id": req.id, "obj_id": req.obj_id},
            GetSensorResultsRes
        )

    def get_step_results(self, id: str, obj_id: str) -> GetStepResultsRes:
        """Get step results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Step results response
            
        Raises:
            APIError: If the request fails
        """
        req = GetStepResultsReq(id=id, obj_id=obj_id)
        
        return self.http_client.post(
            "/openapi/sim_record/v1/step_result/get",
            {"id": req.id, "obj_id": req.obj_id},
            GetStepResultsRes
        )

    def get_path_results(self, id: str, obj_id: str) -> GetPathResultsRes:
        """Get path results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Get path results response
            
        Raises:
            APIError: If the request fails
        """
        req = GetPathResultsReq(id=id, obj_id=obj_id)
        
        return self.http_client.post(
            "/openapi/sim_record/v2/path/get",
            {"id": req.id, "obj_id": req.obj_id},
            GetPathResultsRes
        )

    def get_reference_line_results(self, id: str, obj_id: str) -> GetReferenceLineResultsRes:
        """Get reference line results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Get reference line results response
            
        Raises:
            APIError: If the request fails
        """
        req = GetReferenceLineResultsReq(id=id, obj_id=obj_id)
        
        return self.http_client.post(
            "/openapi/sim_record/v2/reference_line/get",
            {"id": req.id, "obj_id": req.obj_id},
            GetReferenceLineResultsRes
        )
