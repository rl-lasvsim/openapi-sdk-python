"""
Simulation record module for the lasvsim API.
"""
from typing import Optional

from lasvsim_openapi4.http_client import HttpClient
from lasvsim_openapi4.sim_record_model import (
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
        reply = GetRecordIdsRes()
        
        self.http_client.post(
            "/openapi/sim_record/v1/ids/get",
            {"scen_id": req.scen_id, "scen_ver": req.scen_ver},
            reply
        )
        
        return reply

    def get_track_results(self, id: str, obj_id: str) -> GetTrackResultsRes:
        """Get track results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Track results response
            
        Raises:
            APIError: If the request fails
        """
        req = GetTrackResultsReq(id=id, obj_id=obj_id)
        reply = GetTrackResultsRes()
        
        self.http_client.post(
            "/openapi/sim_record/v1/track_result/get",
            {"id": req.id, "obj_id": req.obj_id},
            reply
        )
        
        return reply

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
        reply = GetSensorResultsRes()
        
        self.http_client.post(
            "/openapi/sim_record/v1/sensor_result/get",
            {"id": req.id, "obj_id": req.obj_id},
            reply
        )
        
        return reply

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
        reply = GetStepResultsRes()
        
        self.http_client.post(
            "/openapi/sim_record/v1/step_result/get",
            {"id": req.id, "obj_id": req.obj_id},
            reply
        )
        
        return reply

    def get_path_results(self, id: str, obj_id: str) -> GetPathResultsRes:
        """Get path results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Path results response
            
        Raises:
            APIError: If the request fails
        """
        req = GetPathResultsReq(id=id, obj_id=obj_id)
        reply = GetPathResultsRes()
        
        self.http_client.post(
            "/openapi/sim_record/v1/path_result/get",
            {"id": req.id, "obj_id": req.obj_id},
            reply
        )
        
        return reply

    def get_reference_line_results(self, id: str, obj_id: str) -> GetReferenceLineResultsRes:
        """Get reference line results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Reference line results response
            
        Raises:
            APIError: If the request fails
        """
        req = GetReferenceLineResultsReq(id=id, obj_id=obj_id)
        reply = GetReferenceLineResultsRes()
        
        self.http_client.post(
            "/openapi/sim_record/v1/reference_line_result/get",
            {"id": req.id, "obj_id": req.obj_id},
            reply
        )
        
        return reply
