"""
Process task model module for the lasvsim API.
"""
from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class CopyRecordReq:
    """Request for copying a record."""
    task_id: int = 0  # 任务ID
    record_id: int = 0  # 剧本ID
    
    def __init__(self, task_id: int = 0, record_id: int = 0):
        self.task_id = task_id
        self.record_id = record_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class CopyRecordRes:
    """Response for copying a record."""
    sim_record_id: str = ""
    scen_id: str = ""
    scen_ver: str = ""
    new_record_id: int = 0
    
    def __init__(self, sim_record_id: str = "", scen_id: str = "", scen_ver: str = "", new_record_id: int = 0):
        self.sim_record_id = sim_record_id
        self.scen_id = scen_id
        self.scen_ver = scen_ver
        self.new_record_id = new_record_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class GetRecordScenarioReq:
    """Request for getting record scenario."""
    task_id: int = 0  # 任务ID
    record_id: int = 0  # 剧本ID
    
    def __init__(self, task_id: int = 0, record_id: int = 0):
        self.task_id = task_id
        self.record_id = record_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class GetRecordScenarioRes:
    """Response for getting record scenario."""
    scen_id: str = ""
    scen_ver: str = ""
    
    def __init__(self,scen_id: str = "", scen_ver: str = ""):
        self.scen_id = scen_id
        self.scen_ver = scen_ver

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class GetTaskRecordIdsReq:
    """Request for getting task record IDs."""
    task_id: int = 0
    
    def __init__(self, task_id: int = 0):
        self.task_id = task_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class GetTaskRecordIdsRes:
    """Response for getting task record IDs."""
    record_ids: List[int] = field(default_factory=list)
    
    def __init__(self,record_ids: List[int] = None):
        self.record_ids = record_ids

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class ScenarioRef:
    """Scenario reference for task creation."""
    map_name: str = ""
    scenario_asset_id: str = ""
    scenario_asset_version: str = ""
    scenario_name: str = ""
    scenario_id: str = ""
    source_record_id: int = 0
    
    def __init__(self, map_name: str = "", scenario_asset_id: str = "", 
                 scenario_asset_version: str = "", scenario_name: str = "",
                 scenario_id: str = "", source_record_id: int = 0):
        self.map_name = map_name
        self.scenario_asset_id = scenario_asset_id
        self.scenario_asset_version = scenario_asset_version
        self.scenario_name = scenario_name
        self.scenario_id = scenario_id
        self.source_record_id = source_record_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)
    
    def to_dict(self) -> dict:
        return {
            "map_name": self.map_name,
            "scenario_asset_id": self.scenario_asset_id,
            "scenario_asset_version": self.scenario_asset_version,
            "scenario_name": self.scenario_name,
            "scenario_id": self.scenario_id,
            "source_record_id": self.source_record_id,
        }


@dataclass
class CreateTaskReq:
    """Request for creating a task."""
    name: str = ""  # 任务名称
    folder_id: int = 0  # 文件夹 ID
    scene_v2_infos: List[ScenarioRef] = field(default_factory=list)  # 场景基础信息列表
    
    def __init__(self, name: str = "", folder_id: int = 0, scene_v2_infos: List[ScenarioRef] = None):
        self.name = name
        self.folder_id = folder_id
        self.scene_v2_infos = scene_v2_infos or []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        scene_v2_infos = [ScenarioRef.from_dict(item) for item in data.get("scene_v2_infos", [])]
        return cls(
            name=data.get("name", ""),
            folder_id=data.get("folder_id", 0),
            scene_v2_infos=scene_v2_infos,
        )
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "folder_id": self.folder_id,
            "scene_v2_infos": [info.to_dict() for info in self.scene_v2_infos],
        }


@dataclass
class CreateTaskRes:
    """Response for creating a task."""
    id: int = 0  # 任务 ID
    record_ids: List[int] = field(default_factory=list)  # 记录 ID 列表
    
    def __init__(self, id: int = 0, record_ids: List[int] = None):
        self.id = id
        self.record_ids = record_ids or []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            id=data.get("id", 0),
            record_ids=data.get("record_ids", []),
        )
