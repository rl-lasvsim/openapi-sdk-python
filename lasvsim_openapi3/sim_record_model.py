from dataclasses import dataclass
from typing import List, Optional
from .resource import Point

@dataclass
class Track:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    phi: float = 0.0
    lane_id: str = ""
    position_type: str = ""

@dataclass
class TrackResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: Optional[Track] = None

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

@dataclass
class SensorResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List[SensorObj] = None

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

@dataclass
class StepResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: Optional[Step] = None

@dataclass
class PathPoint:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

@dataclass
class Path:
    points: List[PathPoint] = None

@dataclass
class PathResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List[Path] = None

@dataclass
class ReferenceLine:
    points: List[PathPoint] = None
    line_ids: List[str] = None
    line_types: List[str] = None
    line_idxs: List[int] = None
    opposite: bool = False

@dataclass
class ReferenceLineResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List[ReferenceLine] = None

@dataclass
class GetRecordIdsReq:
    scen_id: str
    scen_ver: str

@dataclass
class GetRecordIdsRes:
    ids: List[str] = None
