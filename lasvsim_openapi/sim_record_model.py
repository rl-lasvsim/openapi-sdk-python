from dataclasses import dataclass
from typing import List


# ----record_id----
@dataclass
class GetRecordIdsResp:
    ids: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


# ----GetTrackResultsResp----
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
class TrackResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: Track = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        result = data.pop("result", None)
        self.__dict__ = data

        self.result = None if result == None else Track(result)


@dataclass
class GetTrackResultsResp:
    data: List[TrackResult] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        result = data.pop("data", None)
        self.__dict__ = data

        self.data = None if result == None else [TrackResult(r) for r in result]


# ----GetSensorResultsResp----
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
class SensorResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List[SensorObj] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        result = data.pop("result", None)
        self.__dict__ = data

        self.result = None if result == None else [SensorObj(r) for r in result]


@dataclass
class GetSensorResultsResp:
    data: List[TrackResult] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        result = data.pop("data", None)
        self.__dict__ = data

        self.data = None if result == None else [SensorResult(r) for r in result]


# ----GetStepResultsResp----
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
    wcc: float = 0.0
    reference_speed: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


@dataclass
class StepResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: Step = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        result = data.pop("result", None)
        self.__dict__ = data

        self.result = None if result == None else Step(result)


@dataclass
class GetStepResultsResp:
    data: List[StepResult] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        result = data.pop("data", None)
        self.__dict__ = data

        self.data = None if result == None else [StepResult(r) for r in result]


# ----GetPathResultsResp----
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
class Path:
    point: List[PathPoint] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        result = data.pop("point", None)
        self.__dict__ = data

        self.point = None if result == None else [PathPoint(r) for r in result]


@dataclass
class PathResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List[Path] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        result = data.pop("result", None)
        self.__dict__ = data

        self.result = None if result == None else [Path(r) for r in result]


@dataclass
class GetPathResultsResp:
    data: List[PathResult] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        result = data.pop("data", None)
        self.__dict__ = data

        self.data = None if result == None else [PathResult(r) for r in result]


# ------ReferenceLineResult---------
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

        result = data.pop("points", None)
        self.__dict__ = data

        self.points = None if result == None else [PathPoint(r) for r in result]


@dataclass
class ReferenceLineResult:
    record_id: str = ""
    obj_id: str = ""
    timestamp: int = 0
    result: List[ReferenceLine] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        result = data.pop("result", None)
        self.__dict__ = data

        self.result = None if result == None else [ReferenceLine(r) for r in result]


@dataclass
class GetReferenceLineResultsResp:
    data: List[ReferenceLineResult] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        result = data.pop("data", None)
        self.__dict__ = data

        self.data = None if result == None else [ReferenceLineResult(r) for r in result]
