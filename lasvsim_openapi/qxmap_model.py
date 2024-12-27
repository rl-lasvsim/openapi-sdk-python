from lasvsim_openapi import response_model
from dataclasses import dataclass
from typing import List
from typing import Dict


@dataclass
class Header:
    north: float = 0.0
    south: float = 0.0
    east: float = 0.0
    west: float = 0.0
    center_point: response_model.Point = None
    version: str = ""
    zone: float = 0.0
    use_bias: bool = False
    source: int = 0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        center_point = data.pop("center_point", None)

        self.__dict__ = data
        self.center_point = (
            None if center_point == None else response_model.Point(center_point)
        )


@dataclass
class Polygon:
    points: List[response_model.Point] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        points = data.pop("points", None)

        self.points = (
            None
            if points == None
            else [response_model.Point(point) for point in points]
        )


@dataclass
class LineString:
    points: List[response_model.Point] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        points = data.pop("points", None)

        self.points = (
            None
            if points == None
            else [response_model.Point(point) for point in points]
        )


@dataclass
class Movement:
    id: str = ""
    upstream_link_id: str = ""
    downstream_link_id: str = ""
    junction_id: str = ""
    flow_direction: int = 0

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


@dataclass
class Connection:
    id: int = 0
    junction_id: str = ""
    movement_id: str = ""
    upstream_lane_id: str = ""
    downstream_lane_id: str = ""
    flow_direction: int = 0
    upstream_link_id: str = ""
    downstream_link_id: str = ""
    path: LineString = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        path = data.pop("path", None)

        self.__dict__ = data
        self.path = None if path == None else LineString(path)


@dataclass
class Crosswalk:
    id: str = ""
    heading: float = 0.0
    shape: Polygon = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        shape = data.pop("shape", None)

        self.__dict__ = data
        self.shape = None if shape == None else Polygon(shape)


@dataclass
class Width:
    s: float = 0.0
    a: float = 0.0
    b: float = 0.0
    c: float = 0.0
    d: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class DirectedPoint:
    point: response_model.Point = None
    heading: float = 0.0
    roll: float = 0.0
    patch: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        point = data.pop("point", None)

        self.__dict__ = data
        self.point = response_model.Point(point)


@dataclass
class LaneTurn:
    position: DirectedPoint = None
    turn_code: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        position = data.pop("position", None)

        self.__dict__ = data
        self.position = DirectedPoint(position)


@dataclass
class SpeedLimit:
    s: float = 0.0
    length: float = 0.0
    type: int = 0
    max_value: float = 0.0
    min_value: float = 0.0
    unit: str = ""
    source: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class Stopline:
    id: str = ""
    shape: LineString = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        shape = data.pop("shape", None)

        self.__dict__ = data
        self.shape = LineString(shape)


@dataclass
class CenterPoint:
    s: float = 0.0
    heading: float = 0.0
    left_width: float = 0.0
    right_width: float = 0.0
    point: response_model.Point = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        point = data.pop("point", None)

        self.__dict__ = data
        self.point = response_model.Point(point)


@dataclass
class LaneMark:
    s: float = 0.0
    length: float = 0.0
    is_merge: bool = False
    style: int = 0
    color: int = 0
    width: float = 0.0
    styles: List[int] = None
    colors: List[int] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class Lane:
    id: str = None
    type: int = None
    lane_num: int = None
    link_id: int = None
    lane_turn: LaneTurn = None
    speed_limits: List[SpeedLimit] = None
    stopline: Stopline = None
    widths: List[Width] = None
    center_line: List[CenterPoint] = None
    upstream_lane_ids: List[str] = None
    downstream_lane_ids: List[str] = None
    length: float = None
    left_lane_marks: List[LaneMark] = None
    right_lane_marks: List[LaneMark] = None
    left_boundary: LineString = None
    right_boundary: LineString = None
    width: float = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        lane_turn = data.pop("lane_turn", None)
        speed_limits = data.pop("speed_limits", None)
        stopline = data.pop("stopline", None)
        widths = data.pop("widths", None)
        center_line = data.pop("center_line", None)
        left_lane_marks = data.pop("left_lane_marks", None)
        right_lane_marks = data.pop("right_lane_marks", None)
        left_boundary = data.pop("left_boundary", None)
        right_boundary = data.pop("right_boundary", None)

        self.__dict__ = data
        self.lane_turn = None if lane_turn == None else LaneTurn(lane_turn)
        self.speed_limits = (
            None if speed_limits == None else [SpeedLimit(sl) for sl in speed_limits]
        )
        self.stopline = None if stopline == None else Stopline(stopline)
        self.widths = None if widths == None else [Width(width) for width in widths]
        self.center_line = (
            None if center_line == None else [CenterPoint(cl) for cl in center_line]
        )
        self.left_lane_marks = (
            None if left_lane_marks == None else [LaneMark(l) for l in left_lane_marks]
        )
        self.right_lane_marks = (
            None
            if right_lane_marks == None
            else [LaneMark(l) for l in right_lane_marks]
        )
        self.left_boundary = (
            None if left_boundary == None else LineString(left_boundary)
        )
        self.right_boundary = (
            None if right_boundary == None else LineString(right_boundary)
        )


@dataclass
class ReferencePoint:
    s: float = 0.0
    heading: float = 0.0
    point: response_model.Point = None
    height: float = 0.0
    cross_slope: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        point = data.pop("point", None)

        self.__dict__ = data
        self.point = None if point == None else response_model.Point(point)


@dataclass
class Link:
    id: str = ""
    map_id: int = 0
    name: str = ""
    type: int = 0
    pair_ids: List[str] = None
    widths: List[Width] = None
    ordered_lanes: List[Lane] = None
    length: float = 0.0
    s_offset: float = 0.0
    link_num: int = 0
    parent_id: str = ""
    reference_line: List[ReferencePoint] = None
    upstream_link_ids: List[str] = None
    downstream_link_ids: List[str] = None
    left_boundary: LineString = None
    right_boundary: LineString = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        widths = data.pop("widths", None)
        ordered_lanes = data.pop("ordered_lanes", None)
        reference_line = data.pop("reference_line", None)
        left_boundary = data.pop("left_boundary", None)
        right_boundary = data.pop("right_boundary", None)

        self.__dict__ = data
        self.widths = None if widths == None else [Width(width) for width in widths]
        self.ordered_lanes = (
            None if ordered_lanes == None else [Lane(ol) for ol in ordered_lanes]
        )
        self.reference_line = (
            None
            if reference_line == None
            else [ReferencePoint(rl) for rl in reference_line]
        )
        self.left_boundary = (
            None if left_boundary == None else LineString(left_boundary)
        )
        self.right_boundary = (
            None if right_boundary == None else LineString(right_boundary)
        )


@dataclass
class TrafficLight_MovementSignal_SignalOfGreen:
    green_start: int = None
    green_duration: int = None
    yellow: int = None
    redClean: int = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class SignalPlan_MovementSignal:
    movement_id: str = None
    traffic_light_pole_id: str = None
    position: DirectedPoint = None
    signal_of_green: List[TrafficLight_MovementSignal_SignalOfGreen] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        position = data.pop("position", None)
        signal_of_green = data.pop("signal_of_green", None)

        self.__dict__ = data
        self.position = None if position == None else DirectedPoint(position)
        self.signal_of_green = (
            None
            if signal_of_green == None
            else [
                TrafficLight_MovementSignal_SignalOfGreen(signal)
                for signal in signal_of_green
            ]
        )


@dataclass
class SignalPlan:
    id: str = None
    junction_id: str = None
    cycle: int = None
    offset: int = None
    is_yellow: bool = None
    movement_signals: Dict[str, SignalPlan_MovementSignal] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        movement_signals = data.pop("movement_signals", None)

        self.__dict__ = data
        movement_signals = (
            None
            if movement_signals == None
            else {
                key: SignalPlan_MovementSignal(value)
                for key, value in movement_signals.items()
            }
        )


@dataclass
class Junction:
    id: str = ""
    map_id: str = ""
    name: str = ""
    type: int = 0
    shape: Polygon = None
    upstream_segment_ids: List[str] = None
    downstream_segment_ids: List[str] = None
    movements: List[Movement] = None
    connections: List[Connection] = None
    crosswalks: List[Crosswalk] = None
    wait_areas: List[Link] = None
    roundabout: List[Link] = None
    links: List[Link] = None
    signal_plan: SignalPlan = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        shape = data.pop("shape", None)
        movements = data.pop("movements", None)
        connections = data.pop("connections", None)
        crosswalks = data.pop("crosswalks", None)
        wait_areas = data.pop("wait_areas", None)
        roundabout = data.pop("roundabout", None)
        links = data.pop("links", None)
        signal_plan = data.pop("signal_plan", None)

        self.__dict__ = data
        self.shape = None if shape == None else Polygon(shape)
        self.movements = None if movements == None else [Movement(m) for m in movements]
        self.connections = (
            None if connections == None else [Connection(c) for c in connections]
        )
        self.crosswalks = (
            None if crosswalks == None else [Crosswalk(c) for c in crosswalks]
        )
        self.wait_areas = (
            None if wait_areas == None else [Link(wa) for wa in wait_areas]
        )
        self.roundabout = (
            None if roundabout == None else [Link(wa) for wa in roundabout]
        )
        self.links = None if links == None else [Link(l) for l in links]
        self.signal_plan = None if signal_plan == None else SignalPlan(signal_plan)


@dataclass
class TrafficSign:
    id: str = ""
    type: int = 0
    position: DirectedPoint = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        position = data.pop("position", None)

        self.__dict__ = data
        self.position = None if position == None else DirectedPoint(position)


@dataclass
class Segment:
    id: str = ""
    map_id: str = ""
    name: str = ""
    start_junction_id: str = ""
    end_junction_id: str = ""
    pair_segment_ids: List[str] = None
    s_offset: float = 0.0
    road_id: str = ""
    length: float = 0.0
    ordered_links: List[Link] = None
    traffic_signs: List[TrafficSign] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        ordered_links = data.pop("ordered_links", None)
        traffic_signs = data.pop("traffic_signs", None)

        self.__dict__ = data
        self.ordered_links = (
            None if ordered_links == None else [Link(ol) for ol in ordered_links]
        )
        self.traffic_signs = (
            None if traffic_signs == None else [TrafficSign(ts) for ts in traffic_signs]
        )


@dataclass
class RoadPosition:
    road_id: str = ""
    road_s: float = 0.0
    s: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class ControlPoint:
    id: str = ""
    point: response_model.Point = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        point = data.pop("point", None)

        self.__dict__ = data
        self.point = None if point == None else response_model.Point(point)


@dataclass
class Section:
    id: str = ""
    s: float = 0.0
    length: float = 0.0
    start_junction_id: str = ""
    end_junction_id: str = ""
    left_segment_id: str = ""
    right_segment_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


@dataclass
class JunctionPosition:
    id: str = None
    junction_id: str = None
    s: float = None
    length: float = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


@dataclass
class Road:
    id: str = ""
    map_id: str = ""
    name: str = ""
    type: int = 0
    length: float = 0.0
    neighbors: List[RoadPosition] = None
    control_points: List[ControlPoint] = None
    reference_line: List[ReferencePoint] = None
    sections: List[Section] = None
    junction_positions: List[JunctionPosition] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        neighbors = data.pop("neighbors", None)
        control_points = data.pop("control_points", None)
        reference_line = data.pop("reference_line", None)
        sections = data.pop("sections", None)
        junction_positions = data.pop("junction_positions", None)

        self.__dict__ = data
        self.neighbors = (
            None if neighbors == None else [RoadPosition(n) for n in neighbors]
        )
        self.control_points = (
            None
            if control_points == None
            else [ControlPoint(cp) for cp in control_points]
        )
        self.reference_line = (
            None
            if reference_line == None
            else [ReferencePoint(n) for n in reference_line]
        )
        self.sections = None if sections == None else [Section(s) for s in sections]
        self.junction_positions = (
            None
            if junction_positions == None
            else [JunctionPosition(jp) for jp in junction_positions]
        )


@dataclass
class Mapper:
    id: str = None
    map_id: str = None
    origin_xpath: str = None
    origin_elem_id: str = None
    origin_elem_type: str = None
    target_xpath: str = None
    target_elem_id: str = None
    target_elem_type: str = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class Building:
    id: str = None
    pos: response_model.Point = None
    shape: Polygon = None
    heading: float = None
    height: float = None
    width: float = None
    length: float = None
    s: float = None
    t: float = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        pos = data.pop("pos", None)
        shape = data.pop("shape", None)

        self.__dict__ = data
        self.pos = None if pos == None else response_model.Point(pos)
        self.shape = None if shape == None else Polygon(shape)


@dataclass
class Tree:
    id: str = None
    pos: response_model.Point = None
    heading: float = None
    height: float = None
    width: float = None
    length: float = None
    s: float = None
    t: float = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        pos = data.pop("pos", None)

        self.__dict__ = data
        self.pos = None if pos == None else response_model.Point(pos)


@dataclass
class Lamp:
    id: str = None
    pos: response_model.Point = None
    heading: float = None
    height: float = None
    width: float = None
    length: float = None
    s: float = None
    t: float = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        pos = data.pop("pos", None)

        self.__dict__ = data
        self.pos = None if pos == None else response_model.Point(pos)


@dataclass
class Qxmap:
    id: str = None
    digest: str = None
    header: Header = None
    junctions: List[Junction] = None
    segments: List[Segment] = None
    roads: List[Road] = None
    mappers: List[Mapper] = None
    buildings: List[Building] = None
    trees: List[Tree] = None
    lamps: List[Lamp] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        header = data.pop("header", None)
        junctions = data.pop("junctions", None)
        segments = data.pop("segments", None)
        roads = data.pop("roads", None)
        mappers = data.pop("mappers", None)
        buildings = data.pop("buildings", None)
        trees = data.pop("trees", None)
        lamps = data.pop("lamps", None)

        self.__dict__ = data
        self.header = None if header == None else Header(header)
        self.junctions = None if junctions == None else [Junction(j) for j in junctions]
        self.segments = None if segments == None else [Segment(s) for s in segments]
        self.roads = None if roads == None else [Road(r) for r in roads]
        self.mappers = None if mappers == None else [Mapper(m) for m in mappers]
        self.buildings = None if buildings == None else [Building(m) for m in buildings]
        self.trees = None if trees == None else [Tree(t) for t in trees]
        self.lamps = None if lamps == None else [Lamp(l) for l in lamps]
