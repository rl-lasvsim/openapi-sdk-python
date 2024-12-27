from dataclasses import dataclass
from typing import List

@dataclass
class CopyRecordReq:
    task_id: int = 0
    record_id: int = 0

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data

@dataclass
class CopyRecordRes:
    sim_record_id: str = ""
    scen_id: str = ""
    scen_ver: str = ""
    new_record_id: int = 0

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data

@dataclass
class GetRecordScenarioReq:
    task_id: int = 0
    record_id: int = 0

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data

@dataclass
class GetRecordScenarioRes:
    scen_id: str = ""
    scen_ver: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data

@dataclass
class GetTaskRecordIdsReq:
    task_id: int = 0

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data

@dataclass
class GetTaskRecordIdsRes:
    record_ids: List[int] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data
