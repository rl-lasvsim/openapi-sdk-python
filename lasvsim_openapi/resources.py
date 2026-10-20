"""
Resource module for the lasvsim API.
"""
from typing import Optional
from dataclasses import dataclass

from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.qxmap import Qxmap
from lasvsim_openapi.resources_fast import ResourcesFast
from lasvsim_openapi.resources_model import (
    ListScenariosReq, ListScenariosRes, ScenarioItem, Pagination,
    ScenarioTag, MapImportReq, MapImportRes, ScenarioImportReq, ScenarioImportRes,
    TrafficFlowGenerateReq, TrafficFlowGenerateRes,
    GetScenarioInfoRes, GetMapInfoRes,
)

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

    def list_scenarios(self, folder_id: int = 0, page_num: int = 1, page_size: int = 10) -> ListScenariosRes:
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
        reply = self.resources_fast.list_scenarios(folder_id, page_num, page_size)
        return ListScenariosRes.from_dict(reply)

    def import_map(self, name: str, desc: str = "", folder_id: int = 0,
                   tags: list = None, data: bytes = None) -> MapImportRes:
        """Import a map via JSON data.
        
        Args:
            name: Map name
            desc: Map description
            folder_id: Folder ID (optional, default 0)
            tags: List of ScenarioTag or tag dicts (optional)
            data: Map JSON data as bytes (optional)
            
        Returns:
            MapImportRes with the new map id
        """
        tag_dicts = None
        if tags is not None:
            tag_dicts = [t.to_dict() if isinstance(t, ScenarioTag) else t for t in tags]
        reply = self.resources_fast.import_map(name, desc, folder_id, tag_dicts, data)
        return MapImportRes.from_dict(reply)

    def import_scenario(self, name: str, desc: str = "", folder_id: int = 0,
                        tags: list = None, data: bytes = None) -> ScenarioImportRes:
        """Import a scenario via JSON data.
        
        Args:
            name: Scenario name
            desc: Scenario description
            folder_id: Folder ID (optional, default 0)
            tags: List of ScenarioTag or tag dicts (optional)
            data: Scenario JSON data as bytes (optional)
            
        Returns:
            ScenarioImportRes with the new scenario id
        """
        tag_dicts = None
        if tags is not None:
            tag_dicts = [t.to_dict() if isinstance(t, ScenarioTag) else t for t in tags]
        reply = self.resources_fast.import_scenario(name, desc, folder_id, tag_dicts, data)
        return ScenarioImportRes.from_dict(reply)

    def generate_traffic_flow(self, map_asset_id: str, map_asset_version: str,
                              test_vehicles: list = None, config: dict = None,
                              exists_env_vehicles: list = None,
                              exists_env_peds: list = None,
                              exists_env_nmvs: list = None) -> TrafficFlowGenerateRes:
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
            TrafficFlowGenerateRes
        """
        reply = self.resources_fast.generate_traffic_flow(
            map_asset_id, map_asset_version,
            test_vehicles, config,
            exists_env_vehicles, exists_env_peds, exists_env_nmvs,
        )
        return TrafficFlowGenerateRes.from_dict(reply)

    def get_scenario_info(self, id: int) -> GetScenarioInfoRes:
        """Get scenario basic info by ID.
        
        Args:
            id: Scenario ID
            
        Returns:
            GetScenarioInfoRes
        """
        reply = self.resources_fast.get_scenario_info(id)
        return GetScenarioInfoRes.from_dict(reply)

    def get_map_info(self, id: int) -> GetMapInfoRes:
        """Get map basic info by ID.
        
        Args:
            id: Map ID
            
        Returns:
            GetMapInfoRes
        """
        reply = self.resources_fast.get_map_info(id)
        return GetMapInfoRes.from_dict(reply)
