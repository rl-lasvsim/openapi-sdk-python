"""
Resource module for the lasvsim API.
"""
from typing import Optional
from dataclasses import dataclass

from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.qxmap import Qxmap


@dataclass
class GetHdMapReq:
    """Request for getting HD map."""
    scen_id: str = ""
    scen_ver: str = ""
    
    def __init__(self, scen_id: str = "", scen_ver: str = ""):
        self.scen_id = scen_id
        self.scen_ver = scen_ver

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class GetHdMapRes:
    """Response for getting HD map."""
    map: Optional[Qxmap] = None
    
    def __init__(self):
        self.map = None

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        map_data = data.pop("data", None)
        instance = cls()
        instance.map = None if map_data is None else Qxmap.from_dict(map_data)
        return instance

class Resources:
    """Resources client for the API."""
    http_client: HttpClient = None

    def __init__(self, http_client: HttpClient):
        """Initialize resources client.
        
        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client.clone()

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
        return self.http_client.post(
            "/openapi/resource/v2/scenario/map/get",
            {"scen_id": scen_id, "scen_ver": scen_ver},
            GetHdMapRes
        )
