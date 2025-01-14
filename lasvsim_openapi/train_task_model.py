"""
Train task model.
"""
from typing import List
from dataclasses import dataclass


@dataclass
class GetSceneIdListReq:
    """Request for getting scene ID list."""
    task_id: int = 0

    def __init__(self, task_id: int = 0):
        self.task_id = task_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(task_id=data.get("task_id", 0))

@dataclass
class GetSceneIdListRes:
    """Get scene id list response."""
    scene_id_list: List[str] = None
    scene_version_list: List[str] = None
    
    def __init__(self):
        self.scene_id_list = []
        self.scene_version_list = []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return cls()
        instance = cls()
        instance.scene_id_list = data.get("scene_id_list", [])
        instance.scene_version_list = data.get("scene_version_list", [])
        return instance
