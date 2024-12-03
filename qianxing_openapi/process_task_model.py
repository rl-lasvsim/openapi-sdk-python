from dataclasses import dataclass


# -----------------------------仿真结构结构--------------------------------
@dataclass
class CopyRecordRes:
    sim_record_id: str = None
    scen_id: str = None
    scen_ver: str = None
    new_record_id: str = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


@dataclass
class GetRecordScenarioRes:
    scen_id: str = None
    scen_ver: str = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


@dataclass
class GetTaskRecordIdsRes:
    record_ids: list[int] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data
