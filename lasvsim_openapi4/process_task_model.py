"""
Process task model module for the lasvsim API.
"""
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class CopyRecordReq:
    """Request for copying a record."""
    task_id: int = 0  # 任务ID
    record_id: int = 0  # 剧本ID


@dataclass
class CopyRecordRes:
    """Response for copying a record."""
    sim_record_id: str = ""
    scen_id: str = ""
    scen_ver: str = ""
    new_record_id: int = 0

    def __init__(self, data: dict = None):
        if data is None:
            return
        self.__dict__.update(data)


@dataclass
class GetRecordScenarioReq:
    """Request for getting record scenario."""
    task_id: int = 0  # 任务ID
    record_id: int = 0  # 剧本ID


@dataclass
class GetRecordScenarioRes:
    """Response for getting record scenario."""
    scen_id: str = ""
    scen_ver: str = ""

    def __init__(self, data: dict = None):
        if data is None:
            return
        self.__dict__.update(data)


@dataclass
class GetTaskRecordIdsReq:
    """Request for getting task record IDs."""
    task_id: int = 0


@dataclass
class GetTaskRecordIdsRes:
    """Response for getting task record IDs."""
    record_ids: List[int] = None

    def __init__(self, data: dict = None):
        if data is None:
            self.record_ids = []
            return
        self.record_ids = data.get("record_ids", [])
