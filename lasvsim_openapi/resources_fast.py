"""
Resource module for the lasvsim API.
"""

from typing import Optional
from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.resources_model import ListScenariosReq

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

    def list_scenarios(self, folder_id: int = 0, page_num: int = 1, page_size: int = 10) -> dict:
        """List scenarios.
        
        Args:
            folder_id: Folder ID (optional, default 0)
            page_num: Page number (optional, default 1)
            page_size: Page size (optional, default 10)
            
        Returns:
            List of scenarios with pagination info
            
        Raises:
            APIError: If the request fails
        """
        req = {
            "folder_id": folder_id,
            "page": {
                "num": page_num,
                "size": page_size,
            }
        }
        return self.http_client.post(
            "/openapi/resource/v2/scenario/list",
            req,
        )
