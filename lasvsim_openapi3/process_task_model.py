from dataclasses import dataclass
from typing import List

@dataclass
class CopyRecordReq:
    task_id: int
    record_id: int

@dataclass
class CopyRecordRes:
    sim_record_id: str
    scen_id: str
    scen_ver: str
    new_record_id: int

@dataclass
class GetRecordScenarioReq:
    task_id: int
    record_id: int

@dataclass
class GetRecordScenarioRes:
    scen_id: str
    scen_ver: str

@dataclass
class GetTaskRecordIdsReq:
    task_id: int

@dataclass
class GetTaskRecordIdsRes:
    record_ids: List[int]
