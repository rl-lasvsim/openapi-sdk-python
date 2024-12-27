from dataclasses import dataclass
from typing import List, Optional

@dataclass
class GetRecordIdsReq:
    scen_id: str = ""
    scen_ver: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetRecordIdsRes:
    ids: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetTrackResultsReq:
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetTrackResultsRes:
    data: List['TrackResult'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetSensorResultsReq:
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetSensorResultsRes:
    data: List['SensorResult'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetStepResultsReq:
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetStepResultsRes:
    data: List['StepResult'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetPathResultsReq:
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetPathResultsRes:
    data: List['PathResult'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetReferenceLineResultsReq:
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetReferenceLineResultsRes:
    data: List['ReferenceLineResult'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class TrackResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: Optional['Track'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class Track:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    phi: float = 0.0
    lane_id: str = ""
    position_type: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class SensorResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List['SensorObj'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class SensorObj:
    id: str = ""
    speed: float = 0.0
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    length: float = 0.0
    width: float = 0.0
    height: float = 0.0
    phi: float = 0.0
    exterior_light: str = ""
    risk_2_ego: int = 0
    lon_acc: float = 0.0
    v: float = 0.0
    lat_acc: float = 0.0
    w: float = 0.0
    w_acc: float = 0.0
    lane_id: str = ""
    position_type: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class StepResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: Optional['Step'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class Step:
    speed: float = 0.0
    acc: float = 0.0
    mileage: float = 0.0
    ste_wheel: float = 0.0
    turn_signal: str = ""
    v: float = 0.0
    lat_acc: float = 0.0
    w: float = 0.0
    w_acc: float = 0.0
    reference_speed: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class PathResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List['Path'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class Path:
    points: List['PathPoint'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class PathPoint:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class ReferenceLineResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List['ReferenceLine'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class ReferenceLine:
    points: List[PathPoint] = None
    line_ids: List[str] = None
    line_types: List[str] = None
    line_idxs: List[int] = None
    opposite: bool = False

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data
