"""
Simulation record model module for the lasvsim API.
"""
from typing import List, Optional
from dataclasses import dataclass, field
from lasvsim_openapi4.simulator_model import Position


@dataclass
class GetRecordIdsReq:
    """Request for getting record IDs."""
    scen_id: str = ""
    scen_ver: str = ""

    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        self.__dict__.update(data)


@dataclass
class GetRecordIdsRes:
    """Response for getting record IDs."""
    record_ids: List[str] = field(default_factory=list)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.record_ids = []
            return
        self.__dict__.update(data)


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
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        position = data.pop("position", None)
        self.__dict__.update(data)
        self.position = None if position is None else Position(position)


@dataclass
class TrackResult:
    """Track result information."""
    record_id: str = ""  # 记录的业务ID
    obj_id: str = ""  # 对象ID
    timestamp: int = 0  # 时间戳
    result: Optional[Track] = None  # 轨迹信息

    def __init__(self, data: dict = None):
        if data is None:
            return
        result = data.pop("result", None)
        self.__dict__.update(data)
        self.result = None if result is None else Track(result)


@dataclass
class GetTrackResultsReq:
    """Request for getting track results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        self.__dict__.update(data)


@dataclass
class GetTrackResultsRes:
    """Response for getting track results."""
    data: List[TrackResult] = field(default_factory=list)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.data = []
            return
        data_list = data.pop("data", [])
        self.__dict__.update(data)
        self.data = [TrackResult(d) for d in data_list]


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
    exterior_light: str = ""  # 最低位起置1表示灯光点亮:近光灯(0) 远光灯(1) 左转向灯(2) 右转向灯(3) 紧急报警灯(4) 刹车灯(5)
    risk_2_ego: int = 0  # 0(无风险); 1(低风险); 2(高风险)
    lon_acc: float = 0.0  # 纵向加速度
    lat_speed: float = 0.0  # 横向速度
    obj_id: str = ""
    obj_type: int = 0
    position: Optional[Position] = None
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        position = data.pop("position", None)
        self.__dict__.update(data)
        self.position = None if position is None else Position(position)


@dataclass
class SensorResult:
    """Sensor result information."""
    record_id: str = ""  # 记录的业务ID
    obj_id: str = ""  # 对象ID
    timestamp: int = 0  # 时间戳
    result: List[SensorObj] = field(default_factory=list)  # 传感器信息

    def __init__(self, data: dict = None):
        if data is None:
            self.result = []
            return
        result = data.pop("result", [])
        self.__dict__.update(data)
        self.result = [SensorObj(item) for item in result]


@dataclass
class GetSensorResultsReq:
    """Request for getting sensor results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        self.__dict__.update(data)


@dataclass
class GetSensorResultsRes:
    """Response for getting sensor results."""
    data: List[SensorResult] = field(default_factory=list)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.data = []
            return
        data_list = data.pop("data", [])
        self.__dict__.update(data)
        self.data = [SensorResult(d) for d in data_list]


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
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        position = data.pop("position", None)
        self.__dict__.update(data)
        self.position = None if position is None else Position(position)


@dataclass
class StepResult:
    """Step result information."""
    record_id: str = ""  # 记录的业务ID
    obj_id: str = ""  # 对象ID
    timestamp: int = 0  # 时间戳
    result: Optional[Step] = None

    def __init__(self, data: dict = None):
        if data is None:
            return
        result = data.pop("result", None)
        self.__dict__.update(data)
        self.result = None if result is None else Step(result)


@dataclass
class GetStepResultsReq:
    """Request for getting step results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        self.__dict__.update(data)


@dataclass
class GetStepResultsRes:
    """Response for getting step results."""
    data: List[StepResult] = field(default_factory=list)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.data = []
            return
        data_list = data.pop("data", [])
        self.__dict__.update(data)
        self.data = [StepResult(d) for d in data_list]


@dataclass
class PathPoint:
    """Path point information."""
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


@dataclass
class Path:
    """Path information."""
    points: List[PathPoint] = field(default_factory=list)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.points = []
            return
        points = data.pop("points", [])
        self.__dict__.update(data)
        self.points = [PathPoint(p) for p in points]


@dataclass
class PathResult:
    """Path result information."""
    record_id: str = ""  # 记录的业务ID
    obj_id: str = ""  # 对象ID
    timestamp: int = 0  # 时间戳
    result: List[Path] = field(default_factory=list)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.result = []
            return
        result = data.pop("result", [])
        self.__dict__.update(data)
        self.result = [Path(p) for p in result]


@dataclass
class GetPathResultsReq:
    """Request for getting path results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        self.__dict__.update(data)


@dataclass
class GetPathResultsRes:
    """Response for getting path results."""
    data: List[PathResult] = field(default_factory=list)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.data = []
            return
        data_list = data.pop("data", [])
        self.__dict__.update(data)
        self.data = [PathResult(d) for d in data_list]


@dataclass
class ReferenceLine:
    """Reference line information."""
    points: List[PathPoint] = field(default_factory=list)
    line_ids: List[str] = field(default_factory=list)
    line_types: List[str] = field(default_factory=list)
    line_idxs: List[int] = field(default_factory=list)
    opposite: bool = False

    def __init__(self, data: dict = None):
        if data is None:
            self.points = []
            self.line_ids = []
            self.line_types = []
            self.line_idxs = []
            return
        self.points = [PathPoint(**point) for point in data.get("points", [])]
        self.line_ids = data.get("line_ids", [])
        self.line_types = data.get("line_types", [])
        self.line_idxs = data.get("line_idxs", [])
        self.opposite = data.get("opposite", False)


@dataclass
class ReferenceLineResult:
    """Reference line result information."""
    record_id: str = ""  # 记录的业务ID
    obj_id: str = ""  # 对象ID
    timestamp: int = 0  # 时间戳
    result: List[ReferenceLine] = field(default_factory=list)

    def __init__(self, data: dict = None):
        if data is None:
            self.result = []
            return
        result = data.pop("result", [])
        self.__dict__.update(data)
        self.result = [ReferenceLine(item) for item in result]


@dataclass
class GetReferenceLineResultsReq:
    """Request for getting reference line results."""
    id: str = ""
    obj_id: str = ""

    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        self.__dict__.update(data)


@dataclass
class GetReferenceLineResultsRes:
    """Response for getting reference line results."""
    data: List[ReferenceLineResult] = field(default_factory=list)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.data = []
            return
        data_list = data.pop("data", [])
        self.__dict__.update(data)
        self.data = [ReferenceLineResult(d) for d in data_list]
