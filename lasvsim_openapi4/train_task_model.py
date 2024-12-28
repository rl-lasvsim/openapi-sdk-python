"""
Train task model.
"""
from typing import List
from dataclasses import dataclass


@dataclass
class GetSceneIdListReq:
    """Get scene id list request."""
    task_id: int = 0
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        self.__dict__.update(data)


@dataclass
class GetSceneIdListRes:
    """Get scene id list response."""
    scene_id_list: List[str] = None
    scene_version_list: List[str] = None
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.scene_id_list = []
            self.scene_version_list = []
            return
        scene_id_list = data.pop("scene_id_list", [])
        scene_version_list = data.pop("scene_version_list", [])
        self.__dict__.update(data)
        self.scene_id_list = scene_id_list
        self.scene_version_list = scene_version_list
