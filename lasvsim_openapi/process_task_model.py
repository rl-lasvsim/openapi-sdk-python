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
