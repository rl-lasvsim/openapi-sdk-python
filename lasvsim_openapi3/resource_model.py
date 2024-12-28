from dataclasses import dataclass
from typing import List, Optional, Dict
from enum import Enum

class HeaderSourceType(Enum):
    SOURCE_QXMAP = 0
    SOURCE_APOLLO = 1
    SOURCE_OPENDRIVE = 2
    SOURCE_ROAD_EDITOR = 3

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

@dataclass
class Header:
    north: float = 0.0
    south: float = 0.0
    east: float = 0.0
    west: float = 0.0
    center_point: Optional[Point] = None
    version: str = ""
    zone: float = 0.0
    use_bias: bool = False
    source: HeaderSourceType = HeaderSourceType.SOURCE_QXMAP
    check_version: str = ""

class JunctionType(Enum):
    JUNCTION_TYPE_UNKNOWN = 0
    JUNCTION_TYPE_DEAD_END = 1
    JUNCTION_TYPE_CROSSING = 2
    JUNCTION_TYPE_ROUNDABOUT = 3
    JUNCTION_TYPE_RAMP_IN = 4
    JUNCTION_TYPE_RAMP_OUT = 5
    JUNCTION_TYPE_VIRTUAL = 6

@dataclass
class Polygon:
    points: List[Point] = None

@dataclass
class Junction:
    id: str = ""
    map_id: str = ""
    name: str = ""
    type: JunctionType = JunctionType.JUNCTION_TYPE_UNKNOWN
    shape: Optional[Polygon] = None
    upstream_segment_ids: List[str] = None
    downstream_segment_ids: List[str] = None
    movements: List['Movement'] = None
    connections: List['Connection'] = None
    crosswalks: List['Crosswalk'] = None
    wait_areas: List['Link'] = None
    roundabout: List['Link'] = None
    links: List['Link'] = None
    signal_plan: Optional['SignalPlan'] = None

@dataclass
class Qxmap:
    id: str = ""
    digest: str = ""
    header: Optional[Header] = None
    junctions: List[Junction] = None
    segments: List['Segment'] = None
    roads: List['Road'] = None
    mappers: List['Mapper'] = None
    buildings: List['Building'] = None
    trees: List['Tree'] = None
    lamps: List['Lamp'] = None

@dataclass
class GetHdMapReq:
    scen_id: str
    scen_ver: str

@dataclass
class GetHdMapRes:
    data: Optional['Qxmap'] = None

class Direction(Enum):
    DIRECTION_UNKNOWN = 0
    DIRECTION_STRAIGHT = 1
    DIRECTION_LEFT = 2
    DIRECTION_RIGHT = 3
    DIRECTION_U_TURN = 4

@dataclass
class Movement:
    id: str = ""
    upstream_link_id: str = ""
    downstream_link_id: str = ""
    junction_id: str = ""
    flow_direction: Direction = Direction.DIRECTION_UNKNOWN

@dataclass
class Connection:
    id: str = ""
    junction_id: str = ""
    movement_id: str = ""
    upstream_lane_id: str = ""
    downstream_lane_id: str = ""
    flow_direction: Direction = Direction.DIRECTION_UNKNOWN
    upstream_link_id: str = ""
    downstream_link_id: str = ""
    path: Optional['LineString'] = None

@dataclass
class LineString:
    points: List[Point] = None

@dataclass
class Crosswalk:
    id: str = ""
    heading: float = 0.0
    shape: Optional[Polygon] = None

class LinkType(Enum):
    LINK_TYPE_UNKNOWN = 0
    LINK_TYPE_WAIT_AREA = 1
    LINK_TYPE_ROUNDABOUT = 2
    LINK_TYPE_SEGMENT = 3
    LINK_TYPE_JUNCTION = 4
    LINK_TYPE_PRE_TURN_RIGHT = 5
    LINK_TYPE_PRE_U_TURN = 6

@dataclass
class Link:
    id: str = ""
    map_id: str = ""
    name: str = ""
    type: LinkType = LinkType.LINK_TYPE_UNKNOWN
    pair_ids: List[str] = None
    widths: List['Width'] = None
    ordered_lanes: List['Lane'] = None
    length: float = 0.0
    s_offset: float = 0.0
    link_num: int = 0
    parent_id: str = ""
    reference_line: List['ReferencePoint'] = None
    upstream_link_ids: List[str] = None
    downstream_link_ids: List[str] = None
    left_boundary: Optional['LineString'] = None
    right_boundary: Optional['LineString'] = None

@dataclass
class Width:
    s: float = 0.0
    a: float = 0.0
    b: float = 0.0
    c: float = 0.0
    d: float = 0.0

@dataclass
class LaneTurn:
    position: Optional['DirectedPoint'] = None
    turn_code: str = ""

@dataclass
class DirectedPoint:
    point: Optional[Point] = None
    heading: float = 0.0
    roll: float = 0.0
    patch: float = 0.0

class SpeedLimitType(Enum):
    SPEED_LIMIT_UNLIMITED = 0
    SPEED_LIMIT_LIMITED = 1
    SPEED_LIMIT_MAX_LIMITED = 2
    SPEED_LIMIT_MIN_LIMITED = 3

@dataclass
class SpeedLimit:
    s: float = 0.0
    length: float = 0.0
    type: SpeedLimitType = SpeedLimitType.SPEED_LIMIT_UNLIMITED
    max_value: float = 0.0
    min_value: float = 0.0
    unit: str = ""
    source: str = ""

@dataclass
class Stopline:
    id: str = ""
    shape: Optional['LineString'] = None

class LaneMarkStyle(Enum):
    LANE_MARK_STYLE_UNKNOWN = 0
    LANE_MARK_STYLE_NONE = 1
    LANE_MARK_STYLE_SOLID = 2
    LANE_MARK_STYLE_BROKEN = 3
    LANE_MARK_STYLE_DOUBLE_SOLID = 4
    LANE_MARK_STYLE_DOUBLE_BROKEN = 5

class LaneMarkColor(Enum):
    LANE_MARK_COLOR_UNKNOWN = 0
    LANE_MARK_COLOR_WHITE = 1
    LANE_MARK_COLOR_YELLOW = 2

@dataclass
class LaneMark:
    s: float = 0.0
    length: float = 0.0
    is_merge: bool = False
    style: LaneMarkStyle = LaneMarkStyle.LANE_MARK_STYLE_UNKNOWN
    color: LaneMarkColor = LaneMarkColor.LANE_MARK_COLOR_UNKNOWN
    width: float = 0.0
    styles: List[LaneMarkStyle] = None
    colors: List[LaneMarkColor] = None

@dataclass
class CenterPoint:
    s: float = 0.0
    heading: float = 0.0
    left_width: float = 0.0
    right_width: float = 0.0
    point: Optional[Point] = None

class LaneType(Enum):
    LANE_TYPE_UNKNOWN = 0
    LANE_TYPE_DRIVING = 1
    LANE_TYPE_BIKING = 2
    LANE_TYPE_SIDEWALK = 3
    LANE_TYPE_PARKING = 4
    LANE_TYPE_BORDER = 5
    LANE_TYPE_MEDIAN = 6
    LANE_TYPE_BUSING = 7
    LANE_TYPE_CURB = 8
    LANE_TYPE_ENTRY = 10
    LANE_TYPE_EXIT = 11
    LANE_TYPE_RAMP_IN = 12
    LANE_TYPE_RAMP_OUT = 13

@dataclass
class Lane:
    id: str = ""
    type: LaneType = LaneType.LANE_TYPE_UNKNOWN
    lane_num: int = 0
    link_id: str = ""
    lane_turn: Optional[LaneTurn] = None
    speed_limits: List[SpeedLimit] = None
    stopline: Optional[Stopline] = None
    widths: List[Width] = None
    center_line: List[CenterPoint] = None
    upstream_lane_ids: List[str] = None
    downstream_lane_ids: List[str] = None
    length: float = 0.0
    left_lane_marks: List[LaneMark] = None
    right_lane_marks: List[LaneMark] = None
    left_boundary: Optional[LineString] = None
    right_boundary: Optional[LineString] = None
    width: float = 0.0

@dataclass
class ReferencePoint:
    s: float = 0.0
    heading: float = 0.0
    point: Optional[Point] = None
    height: float = 0.0
    cross_slope: float = 0.0

class TrafficSignType(Enum):
    SIGN_TYPE_UNKNOWN = 0
    SIGN_TYPE_SPEED_LIMIT = 1
    SIGN_TYPE_GUIDE_SIGN = 2
    SIGN_TYPE_TRAFFIC_LIGHT_POLE = 3

@dataclass
class TrafficSign:
    id: str = ""
    type: TrafficSignType = TrafficSignType.SIGN_TYPE_UNKNOWN
    position: Optional[DirectedPoint] = None

@dataclass
class Section:
    id: str = ""
    s: float = 0.0
    length: float = 0.0
    start_junction_id: str = ""
    end_junction_id: str = ""
    left_segment_id: str = ""
    right_segment_id: str = ""

@dataclass
class JunctionPosition:
    id: str = ""
    junction_id: str = ""
    s: float = 0.0
    length: float = 0.0

class RoadType(Enum):
    ROAD_TYPE_UNKNOWN = 0
    ROAD_TYPE_RAMP = 1

@dataclass
class RoadPosition:
    road_id: str = ""
    road_s: float = 0.0
    s: float = 0.0

@dataclass
class ControlPoint:
    id: str = ""
    point: Optional[Point] = None

@dataclass
class Road:
    id: str = ""
    map_id: str = ""
    name: str = ""
    type: RoadType = RoadType.ROAD_TYPE_UNKNOWN
    length: float = 0.0
    neighbors: List['RoadPosition'] = None
    control_points: List['ControlPoint'] = None
    reference_line: List['ReferencePoint'] = None
    sections: List['Section'] = None
    junction_positions: List['JunctionPosition'] = None

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
    ordered_links: List['Link'] = None
    traffic_signs: List['TrafficSign'] = None

@dataclass
class Mapper:
    id: str = ""
    map_id: str = ""
    origin_xpath: Optional[str] = None
    origin_elem_id: str = ""
    origin_elem_type: str = ""
    target_xpath: Optional[str] = None
    target_elem_id: str = ""
    target_elem_type: str = ""

@dataclass
class Building:
    id: str = ""
    pos: Optional[Point] = None
    shape: Optional[Polygon] = None
    heading: float = 0.0
    height: float = 0.0
    width: float = 0.0
    length: float = 0.0
    s: float = 0.0
    t: float = 0.0
    model_num: int = 0

@dataclass
class Tree:
    id: str = ""
    pos: Optional[Point] = None
    heading: float = 0.0
    height: float = 0.0
    width: float = 0.0
    length: float = 0.0
    s: float = 0.0
    t: float = 0.0
    model_num: int = 0

@dataclass
class Lamp:
    id: str = ""
    pos: Optional[Point] = None
    heading: float = 0.0
    height: float = 0.0
    width: float = 0.0
    length: float = 0.0
    s: float = 0.0
    t: float = 0.0
    model_num: int = 0

@dataclass
class SignalPlan_MovementSignal_SignalOfGreen:
    green_start: int = None
    green_duration: int = None
    yellow: int = None
    redClean: int = None

@dataclass
class SignalPlan_MovementSignal:
    movement_id: str = None
    traffic_light_pole_id: str = None
    position: Optional['DirectedPoint'] = None
    signal_of_green: List['SignalPlan_MovementSignal_SignalOfGreen'] = None

@dataclass
class SignalPlan:
    id: str = None
    junction_id: str = None
    cycle: int = None
    offset: int = None
    is_yellow: bool = None
    movement_signals: Dict[str, 'SignalPlan_MovementSignal'] = None
