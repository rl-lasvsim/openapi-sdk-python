"""
Simulation record model module for the lasvsim API.
"""
from typing import List, Optional
from dataclasses import dataclass, field
from lasvsim_openapi.simulator_model import Position


@dataclass
class GetRecordIdsReq:
    """Request for getting record IDs."""
    scen_id: str = ""
    scen_ver: str = ""

    def __init__(self, data: dict = None, scen_id: str = "", scen_ver: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        
        self.scen_id = scen_id
        self.scen_ver = scen_ver


@dataclass
class GetRecordIdsRes:
    """Response for getting record IDs."""
    record_ids: List[str] = field(default_factory=list)
    
    def __init__(self, data: dict = None, record_ids: List[str] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        
        self.record_ids = record_ids if record_ids is not None else []


@dataclass
class Track:
    """Track information."""
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    phi: float = 0.0
    lane_id: str = ""  # 车道ID，允许为空
    position_type: str = ""
    timestamp: int = 0
    position: Optional[Position] = None
    
    def __init__(self, data: dict = None, x: float = 0.0, y: float = 0.0, z: float = 0.0, phi: float = 0.0, lane_id: str = "", position_type: str = "", timestamp: int = 0, position: Optional[Position] = None):
        if data is not None:
            position = data.pop("position", None)
            self.__dict__.update(data)
            self.position = None if position is None else Position(position)
            return
        
        self.x = x
        self.y = y
        self.z = z
        self.phi = phi
        self.lane_id = lane_id
        self.position_type = position_type
        self.timestamp = timestamp
        self.position = position


@dataclass
class TrackResult:
    """Track result information."""
    record_id: str = ""  # 记录的业务ID
    obj_id: str = ""  # 对象ID
    timestamp: int = 0  # 时间戳
    result: Optional[Track] = None  # 轨迹信息

    def __init__(self, data: dict = None, record_id: str = "", obj_id: str = "", timestamp: int = 0, result: Optional[Track] = None):
        if data is not None:
            result = data.pop("result", None)
            self.__dict__.update(data)
            self.result = None if result is None else Track(result)
            return
        
        self.record_id = record_id
        self.obj_id = obj_id
        self.timestamp = timestamp
        self.result = result


@dataclass
class GetTrackResultsReq:
    """Request for getting track results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict = None, id: str = "", obj_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        
        self.id = id
        self.obj_id = obj_id


@dataclass
class GetTrackResultsRes:
    """Response for getting track results."""
    data: List[TrackResult] = field(default_factory=list)

    def __init__(self, data: dict = None, data_list: List[TrackResult] = None):
        if data is not None:
            data_list = data.pop("data", [])
            self.__dict__.update(data)
            self.data = [TrackResult(d) for d in data_list]
            return
        
        self.data = data_list if data_list is not None else []


@dataclass
class SensorObj:
    """Sensor object information."""
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
    lat_speed: float = 0.0
    obj_id: str = ""
    obj_type: int = 0
    position: Optional[Position] = None

    def __init__(self, data: dict = None, id: str = "", speed: float = 0.0, x: float = 0.0, y: float = 0.0, z: float = 0.0, length: float = 0.0, width: float = 0.0, height: float = 0.0, phi: float = 0.0, exterior_light: str = "", risk_2_ego: int = 0, lon_acc: float = 0.0, lat_speed: float = 0.0, obj_id: str = "", obj_type: int = 0, position: Optional[Position] = None):
        if data is not None:
            position = data.pop("position", None)
            self.__dict__.update(data)
            self.position = None if position is None else Position(position)
            return
        
        self.id = id
        self.speed = speed
        self.x = x
        self.y = y
        self.z = z
        self.length = length
        self.width = width
        self.height = height
        self.phi = phi
        self.exterior_light = exterior_light
        self.risk_2_ego = risk_2_ego
        self.lon_acc = lon_acc
        self.lat_speed = lat_speed
        self.obj_id = obj_id
        self.obj_type = obj_type
        self.position = position


@dataclass
class SensorResult:
    """Sensor result information."""
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List[SensorObj] = field(default_factory=list)

    def __init__(self, data: dict = None, record_id: str = "", obj_id: str = "", timestamp: int = 0, result: List[SensorObj] = None):
        if data is not None:
            result = data.pop("result", [])
            self.__dict__.update(data)
            self.result = [SensorObj(item) for item in result]
            return
        
        self.record_id = record_id
        self.obj_id = obj_id
        self.timestamp = timestamp
        self.result = result if result is not None else []


@dataclass
class GetSensorResultsReq:
    """Request for getting sensor results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict = None, id: str = "", obj_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        
        self.id = id
        self.obj_id = obj_id


@dataclass
class GetSensorResultsRes:
    """Response for getting sensor results."""
    data: List[SensorResult] = field(default_factory=list)

    def __init__(self, data: dict = None, data_list: List[SensorResult] = None):
        if data is not None:
            data_list = data.pop("data", [])
            self.__dict__.update(data)
            self.data = [SensorResult(d) for d in data_list]
            return
        
        self.data = data_list if data_list is not None else []


@dataclass
class Step:
    """Step information."""
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
    timestamp: int = 0
    position: Optional[Position] = None

    def __init__(self, data: dict = None, speed: float = 0.0, acc: float = 0.0, mileage: float = 0.0, ste_wheel: float = 0.0, turn_signal: str = "", v: float = 0.0, lat_acc: float = 0.0, w: float = 0.0, w_acc: float = 0.0, reference_speed: float = 0.0, timestamp: int = 0, position: Optional[Position] = None):
        if data is not None:
            position = data.pop("position", None)
            self.__dict__.update(data)
            self.position = None if position is None else Position(position)
            return
        
        self.speed = speed
        self.acc = acc
        self.mileage = mileage
        self.ste_wheel = ste_wheel
        self.turn_signal = turn_signal
        self.v = v
        self.lat_acc = lat_acc
        self.w = w
        self.w_acc = w_acc
        self.reference_speed = reference_speed
        self.timestamp = timestamp
        self.position = position


@dataclass
class StepResult:
    """Step result information."""
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: Optional[Step] = None

    def __init__(self, data: dict = None, record_id: str = "", obj_id: str = "", timestamp: int = 0, result: Optional[Step] = None):
        if data is not None:
            result = data.pop("result", None)
            self.__dict__.update(data)
            self.result = None if result is None else Step(result)
            return
        
        self.record_id = record_id
        self.obj_id = obj_id
        self.timestamp = timestamp
        self.result = result


@dataclass
class GetStepResultsReq:
    """Request for getting step results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict = None, id: str = "", obj_id: str = ""):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        
        self.id = id
        self.obj_id = obj_id


@dataclass
class GetStepResultsRes:
    """Response for getting step results."""
    data: List[StepResult] = field(default_factory=list)

    def __init__(self, data: dict = None, data_list: List[StepResult] = None):
        if data is not None:
            data_list = data.pop("data", [])
            self.__dict__.update(data)
            self.data = [StepResult(d) for d in data_list]
            return
        
        self.data = data_list if data_list is not None else []


@dataclass
class PathPoint:
    """Path point information."""
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z


@dataclass
class Path:
    """Path information."""
    points: List[PathPoint] = field(default_factory=list)

    def __init__(self, data: dict = None, points: List[PathPoint] = None):
        if data is not None:
            points = data.pop("points", [])
            self.__dict__.update(data)
            self.points = [PathPoint(p) for p in points]
            return
        
        self.points = points if points is not None else []


@dataclass
class PathResult:
    """Path result information."""
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List[Path] = field(default_factory=list)

    def __init__(self, data: dict = None, record_id: str = "", obj_id: str = "", timestamp: int = 0, result: List[Path] = None):
        if data is not None:
            result = data.pop("result", [])
            self.__dict__.update(data)
            self.result = [Path(p) for p in result]
            return
        
        self.record_id = record_id
        self.obj_id = obj_id
        self.timestamp = timestamp
        self.result = result if result is not None else []


@dataclass
class GetPathResultsReq:
    """Request for getting path results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict = None, id: str = "", obj_id: str = ""):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        
        self.id = id
        self.obj_id = obj_id


@dataclass
class GetPathResultsRes:
    """Response for getting path results."""
    data: List[PathResult] = field(default_factory=list)

    def __init__(self, data: dict = None, data_list: List[PathResult] = None):
        if data is not None:
            data_list = data.pop("data", [])
            self.__dict__.update(data)
            self.data = [PathResult(d) for d in data_list]
            return
        
        self.data = data_list if data_list is not None else []


@dataclass
class ReferenceLine:
    """Reference line information."""
    points: List[PathPoint] = field(default_factory=list)
    line_ids: List[str] = field(default_factory=list)
    line_types: List[str] = field(default_factory=list)
    line_idxs: List[int] = field(default_factory=list)
    opposite: bool = False

    def __init__(self, data: dict = None, points: List[PathPoint] = None, line_ids: List[str] = None, line_types: List[str] = None, line_idxs: List[int] = None, opposite: bool = False):
        if data is not None:
            self.points = [PathPoint(**point) for point in data.get("points", [])]
            self.line_ids = data.get("line_ids", [])
            self.line_types = data.get("line_types", [])
            self.line_idxs = data.get("line_idxs", [])
            self.opposite = data.get("opposite", False)
            return
        
        self.points = points if points is not None else []
        self.line_ids = line_ids if line_ids is not None else []
        self.line_types = line_types if line_types is not None else []
        self.line_idxs = line_idxs if line_idxs is not None else []
        self.opposite = opposite


@dataclass
class ReferenceLineResult:
    """Reference line result information."""
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List[ReferenceLine] = field(default_factory=list)

    def __init__(self, data: dict = None, record_id: str = "", obj_id: str = "", timestamp: int = 0, result: List[ReferenceLine] = None):
        if data is not None:
            result = data.pop("result", [])
            self.__dict__.update(data)
            self.result = [ReferenceLine(item) for item in result]
            return
        
        self.record_id = record_id
        self.obj_id = obj_id
        self.timestamp = timestamp
        self.result = result if result is not None else []


@dataclass
class GetReferenceLineResultsReq:
    """Request for getting reference line results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict = None, id: str = "", obj_id: str = ""):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        
        self.id = id
        self.obj_id = obj_id


@dataclass
class GetReferenceLineResultsRes:
    """Response for getting reference line results."""
    data: List[ReferenceLineResult] = field(default_factory=list)

    def __init__(self, data: dict = None, data_list: List[ReferenceLineResult] = None):
        if data is not None:
            data_list = data.pop("data", [])
            self.__dict__.update(data)
            self.data = [ReferenceLineResult(d) for d in data_list]
            return
        
        self.data = data_list if data_list is not None else []
