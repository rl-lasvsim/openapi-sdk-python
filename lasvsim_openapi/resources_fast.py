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

    def import_map(self, name: str, desc: str = "", folder_id: int = 0,
                   tags: list = None, data: bytes = None) -> dict:
        """Import a map via JSON data.
        
        Args:
            name: Map name
            desc: Map description
            folder_id: Folder ID (optional, default 0)
            tags: List of tag dicts with 'id' and 'name' (optional)
            data: Map JSON data as bytes (optional)
            
        Returns:
            Import map response with id
            
        Raises:
            APIError: If the request fails
        """
        req = {
            "name": name,
            "desc": desc,
            "folder_id": folder_id,
        }
        if tags is not None:
            req["tags"] = tags
        if data is not None:
            import base64
            req["data"] = base64.b64encode(data).decode("utf-8") if isinstance(data, bytes) else data
        return self.http_client.post(
            "/openapi/resource/v2/map/import",
            req,
        )

    def import_scenario(self, name: str, desc: str = "", folder_id: int = 0,
                        tags: list = None, data: bytes = None) -> dict:
        """Import a scenario via JSON data.
        
        Args:
            name: Scenario name
            desc: Scenario description
            folder_id: Folder ID (optional, default 0)
            tags: List of tag dicts with 'id' and 'name' (optional)
            data: Scenario JSON data as bytes (optional)
            
        Returns:
            Import scenario response with id
            
        Raises:
            APIError: If the request fails
        """
        req = {
            "name": name,
            "desc": desc,
            "folder_id": folder_id,
        }
        if tags is not None:
            req["tags"] = tags
        if data is not None:
            import base64
            req["data"] = base64.b64encode(data).decode("utf-8") if isinstance(data, bytes) else data
        return self.http_client.post(
            "/openapi/resource/v2/scenario/import",
            req,
        )

    def generate_traffic_flow(self, map_asset_id: str, map_asset_version: str,
                              test_vehicles: list = None, config: dict = None,
                              exists_env_vehicles: list = None,
                              exists_env_peds: list = None,
                              exists_env_nmvs: list = None) -> dict:
        """Generate random traffic flow for a scenario.
        
        Args:
            map_asset_id: Map asset ID (required)
            map_asset_version: Map asset version (required)
            test_vehicles: List of test vehicle dicts (optional)
            config: Scenario config dict (optional)
            exists_env_vehicles: Existing environment vehicles (optional)
            exists_env_peds: Existing environment pedestrians (optional)
            exists_env_nmvs: Existing environment non-motor vehicles (optional)
            
        Returns:
            Traffic flow generation response
            
        Raises:
            APIError: If the request fails
        """
        req = {
            "map_asset_id": map_asset_id,
            "map_asset_version": map_asset_version,
        }
        if test_vehicles is not None:
            req["test_vehicles"] = test_vehicles
        if config is not None:
            req["config"] = config
        if exists_env_vehicles is not None:
            req["exists_env_vehicles"] = exists_env_vehicles
        if exists_env_peds is not None:
            req["exists_env_peds"] = exists_env_peds
        if exists_env_nmvs is not None:
            req["exists_env_nmvs"] = exists_env_nmvs
        return self.http_client.post(
            "/openapi/resource/v2/scenario/traffic_flow/generate",
            req,
        )

    def get_scenario_info(self, id: int) -> dict:
        """Get scenario basic info by ID.
        
        Args:
            id: Scenario ID
            
        Returns:
            Scenario info dict
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/resource/v2/scenario/info",
            {"id": id},
        )

    def get_map_info(self, id: int) -> dict:
        """Get map basic info by ID.
        
        Args:
            id: Map ID
            
        Returns:
            Map info dict
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/resource/v2/map/info",
            {"id": id},
        )
