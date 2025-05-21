"""
Resource module for the lasvsim API.
"""

from lasvsim_openapi.http_client import HttpClient

class ResourcesFast:
    """Resources client for the API."""
    http_client: HttpClient = None

    def __init__(self, http_client: HttpClient):
        """Initialize resources client.
        
        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client.clone()

    def get_hd_map(self, scen_id: str, scen_ver: str) :
        """Get HD map for a scenario.
        
        Args:
            scen_id: Scenario ID
            scen_ver: Scenario version
            
        Returns:
            HD map response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/resource/v2/scenario/map/get",
            {"scen_id": scen_id, "scen_ver": scen_ver},
        )
