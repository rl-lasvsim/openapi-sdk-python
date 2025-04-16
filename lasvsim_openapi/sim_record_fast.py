"""
Simulation record module for the lasvsim API.
"""

from lasvsim_openapi.http_client import HttpClient

class SimRecordFast:
    """Simulation record client for the API."""
    http_client: HttpClient = None

    def __init__(self, http_client: HttpClient):
        """Initialize simulation record client.
        
        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client.clone()

    def get_record_ids(self, scen_id: str, scen_ver: str):
        """Get record IDs.
        
        Args:
            scen_id: Scenario ID
            scen_ver: Scenario version
            
        Returns:
            Record IDs response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/sim_record/v1/ids/get",
            {"scen_id": scen_id, "scen_ver": scen_ver},
        )

    def get_track_results(self, id: str, obj_id: str):
        """Get track results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Get track results response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/sim_record/v1/track_result/get",
            {"id": id, "obj_id": obj_id},
        )

    def get_sensor_results(self, id: str, obj_id: str):
        """Get sensor results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Sensor results response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/sim_record/v1/sensor_result/get",
            {"id": id, "obj_id": obj_id},
        )

    def get_step_results(self, id: str, obj_id: str):
        """Get step results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Step results response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/sim_record/v1/step_result/get",
            {"id": id, "obj_id": obj_id},
        )

    def get_path_results(self, id: str, obj_id: str):
        """Get path results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Get path results response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/sim_record/v1/path_result/get",
            {"id": id, "obj_id": obj_id},
        )

    def get_reference_line_results(self, id: str, obj_id: str):
        """Get reference line results.
        
        Args:
            id: Record ID
            obj_id: Object ID
            
        Returns:
            Get reference line results response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/sim_record/v1/reference_line_result/get",
            {"id": id, "obj_id": obj_id}
        )
