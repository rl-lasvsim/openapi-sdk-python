"""
Resource module for the lasvsim API.
"""
from typing import Optional
from dataclasses import dataclass

from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.qxmap import Qxmap
from lasvsim_openapi.resources_fast import ResourcesFast

@dataclass
class GetHdMapRes:
    """Response for getting HD map."""
    data: Optional[Qxmap] = None
    
    def __init__(self):
        self.data = None

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        map_data = data.pop("data", None)
        instance = cls()
        instance.data = None if map_data is None else Qxmap.from_dict(map_data)
        return instance

class Resources:
    """Resources client for the API."""
    resources_fast: ResourcesFast

    def __init__(self, http_client: HttpClient):
        """Initialize resources client.
        
        Args:
            http_client: HTTP client instance
        """
        self.resources_fast = ResourcesFast(http_client)

    def get_hd_map(self, scen_id: str, scen_ver: str) -> GetHdMapRes:
        """Get HD map for a scenario.
        
        Args:
            scen_id: Scenario ID
            scen_ver: Scenario version
            
        Returns:
            HD map response
            
        Raises:
            APIError: If the request fails
        """
        reply = self.resources_fast.get_hd_map(scen_id, scen_ver)
        return GetHdMapRes.from_dict(reply)
