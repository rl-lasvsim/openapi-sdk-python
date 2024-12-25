from dataclasses import dataclass
from typing import List
from typing import Dict


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
    x: float = None
    y: float = None
    z: float = None
    phi: float = None
    lane_id: str = None
    position_type: str = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


@dataclass
class TrackResult:
    record_id: str = None
    obj_id: str = None
    timestamp: int = None
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
    id: str = None
    speed: float = None
    x: float = None
    y: float = None
    z: float = None
    length: float = None
    width: float = None
    height: float = None
    phi: float = None
    exterior_light: str = None
    risk_2_ego: int = None
    lon_acc: float = None
    v: float = None
    lat_acc: float = None
    w: float = None
    w_acc: float = None
    lane_id: str = None
    position_type: str = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


@dataclass
class SensorResult:
    record_id: str = None
    obj_id: str = None
    timestamp: int = None
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
    speed: float = None
    acc: float = None
    mileage: float = None
    ste_wheel: float = None
    turn_signal: str = None
    v: float = None
    lat_acc: float = None
    w: float = None
    wcc: float = None
    reference_speed: float = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


@dataclass
class StepResult:
    record_id: str = None
    obj_id: str = None
    timestamp: int = None
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
    x: float = None
    y: float = None
    z: float = None

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
    record_id: str = None
    obj_id: str = None
    timestamp: int = None
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
    opposite: bool = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        result = data.pop("points", None)
        self.__dict__ = data

        self.points = None if result == None else [PathPoint(r) for r in result]


@dataclass
class ReferenceLineResult:
    record_id: str = None
    obj_id: str = None
    timestamp: int = None
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
