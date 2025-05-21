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

    def __init__(self, scen_id: str = "", scen_ver: str = ""):
        self.scen_id = scen_id
        self.scen_ver = scen_ver

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class GetRecordIdsRes:
    """Response for getting record IDs."""
    ids: List[str] = field(default_factory=list)
    
    def __init__(self, ids: List[str] = None):
        self.ids = ids if ids is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(ids=data.get("ids", []))


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
    
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, phi: float = 0.0, lane_id: str = "", position_type: str = "", timestamp: int = 0, position: Optional[Position] = None):
        self.x = x
        self.y = y
        self.z = z
        self.phi = phi
        self.lane_id = lane_id
        self.position_type = position_type
        self.timestamp = timestamp
        self.position = position

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        position = data.pop("position", None)
        instance = cls(**data)
        instance.position = None if position is None else Position.from_dict(position)
        return instance


@dataclass
class TrackResult:
    """Track result information."""
    record_id: str = ""  # 记录的业务ID
    obj_id: str = ""  # 对象ID
    timestamp: int = 0  # 时间戳
    result: Optional[Track] = None  # 轨迹信息

    def __init__(self, record_id: str = "", obj_id: str = "", timestamp: int = 0, result: Optional[Track] = None):
        self.record_id = record_id
        self.obj_id = obj_id
        self.timestamp = timestamp
        self.result = result

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        result = data.pop("result", None)
        instance = cls(**data)
        instance.result = None if result is None else Track.from_dict(result)
        return instance


@dataclass
class GetTrackResultsReq:
    """Request for getting track results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, id: str = "", obj_id: str = ""):
        self.id = id
        self.obj_id = obj_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class GetTrackResultsRes:
    """Response for getting track results."""
    data: List[TrackResult] = field(default_factory=list)

    def __init__(self, data_list: List[TrackResult] = None):
        self.data = data_list if data_list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        data_list = data.pop("data", [])
        instance = cls()
        instance.data = [TrackResult.from_dict(d) for d in data_list]
        return instance


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
    # 最低位起置1表示灯光点亮:近光灯(0) 远光灯(1) 左转向灯(2) 右转向灯(3)
    # 紧急报警灯(4) 刹车灯(5) e.g. "000001" 近光灯; "100000" 刹车灯; "111111"
    # 全亮
    exterior_light: str = ""
    # 0(无风险); 1(低风险); 2(高风险)
    risk_2_ego: int = 0
    # 纵向加速度
    lon_acc: float = 0.0
    # 横向速度
    v: float = 0.0
    # 横向加速度
    lat_acc: float = 0.0
    # 横摆角速度
    w: float = 0.0
    # 横摆角加速度
    w_acc: float = 0.0
    # 车道ID，允许为空
    lane_id: str = ""
    # POSITION_TYPE_UNKNOWN = 0;
    # 1. 在车道内
    # POSITION_TYPE_IN_LANE = 1;
    # 2. 在路口内
    # POSITION_TYPE_IN_JUNCTION = 2;
    # 3. 在道路外
    # POSITION_TYPE_OUT_ROAD = 3;
    position_type: str = ""
    position: Optional[Position] = None

    def __init__(self, id: str = "", speed: float = 0.0, x: float = 0.0, y: float = 0.0, z: float = 0.0, length: float = 0.0, width: float = 0.0, height: float = 0.0, phi: float = 0.0, exterior_light: str = "", risk_2_ego: int = 0, lon_acc: float = 0.0, v: float = 0.0, lat_acc: float = 0.0, w: float = 0.0, w_acc: float = 0.0, lane_id: str = "", position_type: str = "", position: Optional[Position] = None):
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
        self.v = v
        self.lat_acc = lat_acc
        self.w = w
        self.w_acc = w_acc
        self.lane_id = lane_id
        self.position_type = position_type
        self.position = position

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        position = data.pop("position", None)
        instance = cls(**data)
        instance.position = None if position is None else Position.from_dict(position)
        return instance


@dataclass
class SensorResult:
    """Sensor result information."""
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List[SensorObj] = field(default_factory=list)

    def __init__(self, record_id: str = "", obj_id: str = "", timestamp: int = 0, result: List[SensorObj] = None):
        self.record_id = record_id
        self.obj_id = obj_id
        self.timestamp = timestamp
        self.result = result if result is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        result = data.pop("result", [])
        instance = cls(**data)
        instance.result = [SensorObj.from_dict(item) for item in result]
        return instance


@dataclass
class GetSensorResultsReq:
    """Request for getting sensor results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, id: str = "", obj_id: str = ""):
        self.id = id
        self.obj_id = obj_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class GetSensorResultsRes:
    """Response for getting sensor results."""
    data: List[SensorResult] = field(default_factory=list)

    def __init__(self, data_list: List[SensorResult] = None):
        self.data = data_list if data_list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        data_list = data.pop("data", [])
        instance = cls()
        instance.data = [SensorResult.from_dict(d) for d in data_list]
        return instance


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
    u: float = 0.0
    u_acc: float = 0.0
    reference_speed: float = 0.0
    timestamp: int = 0
    position: Optional[Position] = None
    distance_to_front: float = 0.0

    def __init__(self, speed: float = 0.0, acc: float = 0.0, mileage: float = 0.0, ste_wheel: float = 0.0, turn_signal: str = "", v: float = 0.0, lat_acc: float = 0.0, w: float = 0.0, w_acc: float = 0.0, reference_speed: float = 0.0, timestamp: int = 0, position: Optional[Position] = None,u: float = 0.0,u_acc: float = 0.0,distance_to_front: float = 0.0):
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
        self.u = u
        self.u_acc = u_acc
        self.distance_to_front = distance_to_front

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        position = data.pop("position", None)
        instance = cls()
        instance.__dict__.update(data)
        instance.position = None if position is None else Position.from_dict(position)
        return instance


@dataclass
class StepResult:
    """Step result information."""
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: Optional[Step] = None

    def __init__(self, record_id: str = "", obj_id: str = "", timestamp: int = 0, result: Optional[Step] = None):
        self.record_id = record_id
        self.obj_id = obj_id
        self.timestamp = timestamp
        self.result = result

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        result = data.pop("result", None)
        instance = cls(**data)
        instance.result = None if result is None else Step.from_dict(result)
        return instance


@dataclass
class GetStepResultsReq:
    """Request for getting step results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, id: str = "", obj_id: str = ""):
        self.id = id
        self.obj_id = obj_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class GetStepResultsRes:
    """Response for getting step results."""
    data: List[StepResult] = field(default_factory=list)

    def __init__(self, data_list: List[StepResult] = None):
        self.data = data_list if data_list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        data_list = data.pop("data", [])
        instance = cls()
        instance.data = [StepResult.from_dict(d) for d in data_list]
        return instance


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

    def __init__(self, points: List[PathPoint] = None):
        self.points = points if points is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        points = data.get("points", [])
        instance = cls()
        instance.points = [PathPoint(**point) for point in points]
        return instance


@dataclass
class PathResult:
    """Path result information."""
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List[Path] = field(default_factory=list)

    def __init__(self, record_id: str = "", obj_id: str = "", timestamp: int = 0, result: List[Path] = None):
        self.record_id = record_id
        self.obj_id = obj_id
        self.timestamp = timestamp
        self.result = result if result is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        result = data.pop("result", [])
        instance = cls(**data)
        instance.result = [Path.from_dict(item) for item in result]
        return instance


@dataclass
class GetPathResultsReq:
    """Request for getting path results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, id: str = "", obj_id: str = ""):
        self.id = id
        self.obj_id = obj_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class GetPathResultsRes:
    """Response for getting path results."""
    data: List[PathResult] = field(default_factory=list)

    def __init__(self, data_list: List[PathResult] = None):
        self.data = data_list if data_list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        data_list = data.pop("data", [])
        instance = cls()
        instance.data = [PathResult.from_dict(d) for d in data_list]
        return instance


@dataclass
class ReferenceLine:
    """Reference line information."""
    points: List[PathPoint] = field(default_factory=list)
    line_ids: List[str] = field(default_factory=list)
    line_types: List[str] = field(default_factory=list)
    line_idxs: List[int] = field(default_factory=list)
    opposite: bool = False

    def __init__(self, points: List[PathPoint] = None, line_ids: List[str] = None, line_types: List[str] = None, line_idxs: List[int] = None, opposite: bool = False):
        self.points = points if points is not None else []
        self.line_ids = line_ids if line_ids is not None else []
        self.line_types = line_types if line_types is not None else []
        self.line_idxs = line_idxs if line_idxs is not None else []
        self.opposite = opposite

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        instance = cls()
        instance.points = [PathPoint(**point) for point in data.get("points", [])]
        instance.line_ids = data.get("line_ids", [])
        instance.line_types = data.get("line_types", [])
        instance.line_idxs = data.get("line_idxs", [])
        instance.opposite = data.get("opposite", False)
        return instance


@dataclass
class ReferenceLineResult:
    """Reference line result information."""
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List[ReferenceLine] = field(default_factory=list)

    def __init__(self, record_id: str = "", obj_id: str = "", timestamp: int = 0, result: List[ReferenceLine] = None):
        self.record_id = record_id
        self.obj_id = obj_id
        self.timestamp = timestamp
        self.result = result if result is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        result = data.pop("result", [])
        instance = cls(**data)
        instance.result = [ReferenceLine.from_dict(item) for item in result]
        return instance


@dataclass
class GetReferenceLineResultsReq:
    """Request for getting reference line results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, id: str = "", obj_id: str = ""):
        self.id = id
        self.obj_id = obj_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(**data)


@dataclass
class GetReferenceLineResultsRes:
    """Response for getting reference line results."""
    data: List[ReferenceLineResult] = field(default_factory=list)

    def __init__(self, data_list: List[ReferenceLineResult] = None):
        self.data = data_list if data_list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        data_list = data.pop("data", [])
        instance = cls()
        instance.data = [ReferenceLineResult.from_dict(d) for d in data_list]
        return instance
