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
