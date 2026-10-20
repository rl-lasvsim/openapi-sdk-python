"""
Resource module data structures.
"""
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Pagination:
    """Pagination parameters."""
    num: int = 1
    size: int = 10
    total: int = 0
    
    def __init__(self, num: int = 1, size: int = 10, total: int = 0):
        self.num = num
        self.size = size
        self.total = total
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        obj = cls()
        for key, value in data.items():
            setattr(obj, key, value)
        return obj


@dataclass
class ScenarioItem:
    """Scenario item data structure."""
    id: int = 0
    name: str = ""
    desc: str = ""
    asset_id: str = ""
    asset_version: str = ""
    
    def __init__(self, id: int = 0, name: str = "", desc: str = "", asset_id: str = "", asset_version: str = ""):
        self.id = id
        self.name = name
        self.desc = desc
        self.asset_id = asset_id
        self.asset_version = asset_version
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        obj = cls()
        for key, value in data.items():
            setattr(obj, key, value)
        return obj


@dataclass
class ListScenariosReq:
    """Request for listing scenarios."""
    folder_id: int = 0
    page: Optional[Pagination] = None
    
    def __init__(self, folder_id: int = 0, page: Optional[Pagination] = None):
        self.folder_id = folder_id
        self.page = page
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        result = {
            "folder_id": self.folder_id,
        }
        if self.page is not None:
            result["page"] = {
                "num": self.page.num,
                "size": self.page.size,
            }
        return result


@dataclass
class ListScenariosRes:
    """Response for listing scenarios."""
    list: List[ScenarioItem] = field(default_factory=list)
    page: Optional[Pagination] = None
    
    def __init__(self):
        self.list = []
        self.page = None
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        obj = cls()
        list_data = data.get("list", [])
        obj.list = [ScenarioItem.from_dict(item) for item in list_data]
        page_data = data.get("page")
        obj.page = None if page_data is None else Pagination.from_dict(page_data)
        return obj


@dataclass
class ScenarioTag:
    """Scenario tag."""
    id: int = 0
    name: str = ""
    
    def __init__(self, id: int = 0, name: str = ""):
        self.id = id
        self.name = name
    
    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name}
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        obj = cls()
        obj.id = data.get("id", 0)
        obj.name = data.get("name", "")
        return obj


@dataclass
class MapImportReq:
    """Request for importing a map."""
    name: str = ""
    desc: str = ""
    folder_id: int = 0
    tags: Optional[List[ScenarioTag]] = None
    data: Optional[bytes] = None
    
    def __init__(self, name: str = "", desc: str = "", folder_id: int = 0,
                 tags: Optional[List[ScenarioTag]] = None, data: Optional[bytes] = None):
        self.name = name
        self.desc = desc
        self.folder_id = folder_id
        self.tags = tags
        self.data = data
    
    def to_dict(self) -> dict:
        result = {
            "name": self.name,
            "desc": self.desc,
            "folder_id": self.folder_id,
        }
        if self.tags is not None:
            result["tags"] = [t.to_dict() for t in self.tags]
        if self.data is not None:
            import base64
            result["data"] = base64.b64encode(self.data).decode("utf-8") if isinstance(self.data, bytes) else self.data
        return result


@dataclass
class MapImportRes:
    """Response for importing a map."""
    id: int = 0
    
    def __init__(self):
        self.id = 0
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        obj = cls()
        obj.id = data.get("id", 0)
        return obj


@dataclass
class ScenarioImportReq:
    """Request for importing a scenario."""
    name: str = ""
    desc: str = ""
    folder_id: int = 0
    tags: Optional[List[ScenarioTag]] = None
    data: Optional[bytes] = None
    
    def __init__(self, name: str = "", desc: str = "", folder_id: int = 0,
                 tags: Optional[List[ScenarioTag]] = None, data: Optional[bytes] = None):
        self.name = name
        self.desc = desc
        self.folder_id = folder_id
        self.tags = tags
        self.data = data
    
    def to_dict(self) -> dict:
        result = {
            "name": self.name,
            "desc": self.desc,
            "folder_id": self.folder_id,
        }
        if self.tags is not None:
            result["tags"] = [t.to_dict() for t in self.tags]
        if self.data is not None:
            import base64
            result["data"] = base64.b64encode(self.data).decode("utf-8") if isinstance(self.data, bytes) else self.data
        return result


@dataclass
class ScenarioImportRes:
    """Response for importing a scenario."""
    id: int = 0
    
    def __init__(self):
        self.id = 0
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        obj = cls()
        obj.id = data.get("id", 0)
        return obj


@dataclass
class TrafficFlowGenerateReq:
    """Request for generating random traffic flow.
    
    Note: test_vehicles, config, exists_env_vehicles, exists_env_peds, exists_env_nmvs
    are complex nested structures. Pass them as dicts matching the API JSON schema.
    """
    test_vehicles: Optional[List[dict]] = None
    config: Optional[dict] = None
    map_asset_id: str = ""
    map_asset_version: str = ""
    exists_env_vehicles: Optional[List[dict]] = None
    exists_env_peds: Optional[List[dict]] = None
    exists_env_nmvs: Optional[List[dict]] = None
    
    def __init__(self, test_vehicles: Optional[List[dict]] = None, config: Optional[dict] = None,
                 map_asset_id: str = "", map_asset_version: str = "",
                 exists_env_vehicles: Optional[List[dict]] = None,
                 exists_env_peds: Optional[List[dict]] = None,
                 exists_env_nmvs: Optional[List[dict]] = None):
        self.test_vehicles = test_vehicles
        self.config = config
        self.map_asset_id = map_asset_id
        self.map_asset_version = map_asset_version
        self.exists_env_vehicles = exists_env_vehicles
        self.exists_env_peds = exists_env_peds
        self.exists_env_nmvs = exists_env_nmvs
    
    def to_dict(self) -> dict:
        result = {
            "map_asset_id": self.map_asset_id,
            "map_asset_version": self.map_asset_version,
        }
        if self.test_vehicles is not None:
            result["test_vehicles"] = self.test_vehicles
        if self.config is not None:
            result["config"] = self.config
        if self.exists_env_vehicles is not None:
            result["exists_env_vehicles"] = self.exists_env_vehicles
        if self.exists_env_peds is not None:
            result["exists_env_peds"] = self.exists_env_peds
        if self.exists_env_nmvs is not None:
            result["exists_env_nmvs"] = self.exists_env_nmvs
        return result


@dataclass
class TrafficFlowGenerateRes:
    """Response for generating random traffic flow.
    
    Fields are returned as dicts matching the API JSON schema.
    """
    env_vehicles: Optional[List[dict]] = field(default_factory=list)
    env_peds: Optional[List[dict]] = field(default_factory=list)
    env_nmvs: Optional[List[dict]] = field(default_factory=list)
    vehicle_flows: Optional[List[dict]] = field(default_factory=list)
    
    def __init__(self):
        self.env_vehicles = []
        self.env_peds = []
        self.env_nmvs = []
        self.vehicle_flows = []
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        obj = cls()
        obj.env_vehicles = data.get("env_vehicles", [])
        obj.env_peds = data.get("env_peds", [])
        obj.env_nmvs = data.get("env_nmvs", [])
        obj.vehicle_flows = data.get("vehicle_flows", [])
        return obj


@dataclass
class GetScenarioInfoReq:
    """Request for getting scenario info."""
    id: int = 0
    
    def __init__(self, id: int = 0):
        self.id = id
    
    def to_dict(self) -> dict:
        return {"id": self.id}


@dataclass
class GetScenarioInfoRes:
    """Response for getting scenario info."""
    id: int = 0
    name: str = ""
    desc: str = ""
    asset_id: str = ""
    asset_version: str = ""
    img_url: str = ""
    folder_id: int = 0
    create_time: int = 0
    update_time: int = 0
    
    def __init__(self):
        self.id = 0
        self.name = ""
        self.desc = ""
        self.asset_id = ""
        self.asset_version = ""
        self.img_url = ""
        self.folder_id = 0
        self.create_time = 0
        self.update_time = 0
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        obj = cls()
        for key, value in data.items():
            setattr(obj, key, value)
        return obj


@dataclass
class GetMapInfoReq:
    """Request for getting map info."""
    id: int = 0
    
    def __init__(self, id: int = 0):
        self.id = id
    
    def to_dict(self) -> dict:
        return {"id": self.id}


@dataclass
class GetMapInfoRes:
    """Response for getting map info."""
    id: int = 0
    name: str = ""
    desc: str = ""
    asset_id: str = ""
    asset_version: str = ""
    img_url: str = ""
    folder_id: int = 0
    size: int = 0
    create_time: int = 0
    update_time: int = 0
    
    def __init__(self):
        self.id = 0
        self.name = ""
        self.desc = ""
        self.asset_id = ""
        self.asset_version = ""
        self.img_url = ""
        self.folder_id = 0
        self.size = 0
        self.create_time = 0
        self.update_time = 0
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        obj = cls()
        for key, value in data.items():
            setattr(obj, key, value)
        return obj
