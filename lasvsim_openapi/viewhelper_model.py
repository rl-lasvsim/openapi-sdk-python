"""
ViewHelper module data structures.
"""
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class FolderInfo:
    """Folder information (tree structure)."""
    id: int = 0
    name: str = ""
    pid: int = 0
    children: List['FolderInfo'] = field(default_factory=list)

    def __init__(self, id: int = 0, name: str = "", pid: int = 0, children: List['FolderInfo'] = None):
        self.id = id
        self.name = name
        self.pid = pid
        self.children = children or []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        obj = cls()
        obj.id = data.get("id", 0)
        obj.name = data.get("name", "")
        obj.pid = data.get("pid", 0)
        children_data = data.get("children", [])
        obj.children = [FolderInfo.from_dict(item) for item in (children_data or [])]
        return obj


@dataclass
class FolderListReq:
    """Request for listing folders."""
    service_code: int = 0

    def __init__(self, service_code: int = 0):
        self.service_code = service_code

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "service_code": self.service_code,
        }


@dataclass
class FolderListRes:
    """Response for listing folders."""
    folders: List[FolderInfo] = field(default_factory=list)

    def __init__(self):
        self.folders = []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        obj = cls()
        folders_data = data.get("folders", [])
        obj.folders = [FolderInfo.from_dict(item) for item in (folders_data or [])]
        return obj
