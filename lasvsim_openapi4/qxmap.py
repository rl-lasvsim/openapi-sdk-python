"""
HD map data structures.
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Point:
    """Point in 3D space."""
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


@dataclass
class DirectedPoint:
    """Point with direction."""
    point: Optional[Point] = None
    heading: float = 0.0
    roll: float = 0.0
    patch: float = 0.0


@dataclass
class Polygon:
    """Polygon shape."""
    points: List[Point] = field(default_factory=list)


@dataclass
class LineString:
    """Line string shape."""
    points: List[Point] = field(default_factory=list)


@dataclass
class Header:
    """Map header information."""
    north: float = 0.0
    south: float = 0.0
    east: float = 0.0
    west: float = 0.0
    source_type: int = 0  # Header_SourceType
    source_version: str = ""
    source_data: str = ""
    source_date: str = ""
    source_coordinate_system: str = ""
    source_projection: str = ""
    source_unit: str = ""


@dataclass
class Width:
    """Width information."""
    s: float = 0.0
    a: float = 0.0
    b: float = 0.0
    c: float = 0.0
    d: float = 0.0


@dataclass
class LaneTurn:
    """Lane turn information."""
    position: Optional[DirectedPoint] = None
    turn_code: str = ""


@dataclass
class SpeedLimit:
    """Speed limit information."""
    s: float = 0.0
    length: float = 0.0
    type: int = 0  # SpeedLimit_SpeedLimitType
    max_value: float = 0.0
    min_value: float = 0.0
    unit: str = ""
    source: str = ""


@dataclass
class Stopline:
    """Stop line information."""
    id: str = ""
    shape: Optional[LineString] = None


@dataclass
class LaneMark:
    """Lane mark information."""
    s: float = 0.0
    length: float = 0.0
    is_merge: bool = False
    style: int = 0  # LaneMark_LaneMarkStyle
    color: int = 0  # LaneMark_LaneMarkColor
    width: float = 0.0
    styles: List[int] = field(default_factory=list)  # List[LaneMark_LaneMarkStyle]
    colors: List[int] = field(default_factory=list)  # List[LaneMark_LaneMarkColor]


@dataclass
class CenterPoint:
    """Center point information."""
    s: float = 0.0
    heading: float = 0.0
    left_width: float = 0.0
    right_width: float = 0.0
    point: Optional[Point] = None


@dataclass
class Lane:
    """Lane information."""
    id: str = ""
    type: int = 0  # Lane_LaneType
    lane_num: int = 0
    link_id: str = ""
    lane_turn: Optional[LaneTurn] = None
    speed_limits: List[SpeedLimit] = field(default_factory=list)
    stopline: Optional[Stopline] = None
    widths: List[Width] = field(default_factory=list)
    center_line: List[CenterPoint] = field(default_factory=list)
    upstream_lane_ids: List[str] = field(default_factory=list)
    downstream_lane_ids: List[str] = field(default_factory=list)
    length: float = 0.0
    left_lane_marks: List[LaneMark] = field(default_factory=list)
    right_lane_marks: List[LaneMark] = field(default_factory=list)
    left_boundary: Optional[LineString] = None
    right_boundary: Optional[LineString] = None
    width: float = 0.0


@dataclass
class Link:
    """Link information."""
    id: str = ""
    map_id: str = ""
    name: str = ""
    type: int = 0  # Link_LinkType
    pair_ids: List[str] = field(default_factory=list)
    widths: List[Width] = field(default_factory=list)
    ordered_lanes: List[Lane] = field(default_factory=list)
    length: float = 0.0
    s_offset: float = 0.0
    link_num: int = 0
    parent_id: str = ""
    reference_line: List[ReferencePoint] = field(default_factory=list)
    upstream_link_ids: List[str] = field(default_factory=list)
    downstream_link_ids: List[str] = field(default_factory=list)
    left_boundary: Optional[LineString] = None
    right_boundary: Optional[LineString] = None


@dataclass
class Movement:
    """Movement information."""
    id: str = ""
    upstream_link_id: str = ""
    downstream_link_id: str = ""
    junction_id: str = ""
    flow_direction: int = 0  # Direction


@dataclass
class Connection:
    """Connection information."""
    id: str = ""
    junction_id: str = ""
    movement_id: str = ""
    upstream_lane_id: str = ""
    downstream_lane_id: str = ""
    flow_direction: int = 0  # Direction
    upstream_link_id: str = ""
    downstream_link_id: str = ""
    path: Optional[LineString] = None


@dataclass
class Crosswalk:
    """Crosswalk information."""
    id: str = ""
    heading: float = 0.0
    shape: Optional[Polygon] = None


@dataclass
class SignalPlan_MovementSignal_SignalOfGreen:
    """Signal of green information."""
    green_start: int = 0
    green_duration: int = 0
    yellow: int = 0
    red_clean: int = 0


@dataclass
class SignalPlan_MovementSignal:
    """Movement signal information."""
    movement_id: str = ""
    traffic_light_pole_id: str = ""
    position: Optional[DirectedPoint] = None
    signal_of_greens: List[SignalPlan_MovementSignal_SignalOfGreen] = field(default_factory=list)


@dataclass
class SignalPlan:
    """Signal plan information."""
    id: str = ""
    junction_id: str = ""
    cycle: int = 0
    offset: int = 0
    is_yellow: bool = False
    movement_signals: Dict[str, SignalPlan_MovementSignal] = field(default_factory=dict)


@dataclass
class Junction:
    """Junction information."""
    id: str = ""
    map_id: str = ""
    name: str = ""
    type: int = 0  # Junction_JunctionType
    shape: Optional[Polygon] = None
    upstream_segment_ids: List[str] = field(default_factory=list)
    downstream_segment_ids: List[str] = field(default_factory=list)
    movements: List[Movement] = field(default_factory=list)
    connections: List[Connection] = field(default_factory=list)
    crosswalks: List[Crosswalk] = field(default_factory=list)
    wait_areas: List[Link] = field(default_factory=list)
    roundabout: List[Link] = field(default_factory=list)
    links: List[Link] = field(default_factory=list)
    signal_plan: Optional[SignalPlan] = None


@dataclass
class TrafficSign:
    """Traffic sign information."""
    id: str = ""
    type: int = 0  # TrafficSign_TrafficSignType
    position: Optional[DirectedPoint] = None


@dataclass
class Segment:
    """Segment information."""
    id: str = ""
    map_id: str = ""
    name: str = ""
    start_junction_id: str = ""
    end_junction_id: str = ""
    pair_segment_ids: List[str] = field(default_factory=list)
    s_offset: float = 0.0
    road_id: str = ""
    length: float = 0.0
    ordered_links: List[Link] = field(default_factory=list)
    traffic_signs: List[TrafficSign] = field(default_factory=list)


@dataclass
class RoadPosition:
    """Road position information."""
    road_id: str = ""
    road_s: float = 0.0
    s: float = 0.0


@dataclass
class ControlPoint:
    """Control point information."""
    id: str = ""
    point: Optional[Point] = None


@dataclass
class ReferencePoint:
    """Reference point information."""
    s: float = 0.0
    heading: float = 0.0
    point: Optional[Point] = None
    height: float = 0.0
    cross_slope: float = 0.0


@dataclass
class Section:
    """Section information."""
    id: str = ""
    s: float = 0.0
    length: float = 0.0
    start_junction_id: str = ""
    end_junction_id: str = ""
    left_segment_id: str = ""
    right_segment_id: str = ""


@dataclass
class JunctionPosition:
    """Junction position information."""
    id: str = ""
    junction_id: str = ""
    s: float = 0.0
    length: float = 0.0


@dataclass
class Road:
    """Road information."""
    id: str = ""
    map_id: str = ""
    name: str = ""
    type: int = 0  # Road_RoadType
    length: float = 0.0
    neighbors: List[RoadPosition] = field(default_factory=list)
    control_points: List[ControlPoint] = field(default_factory=list)
    reference_line: List[ReferencePoint] = field(default_factory=list)
    sections: List[Section] = field(default_factory=list)
    junction_positions: List[JunctionPosition] = field(default_factory=list)


@dataclass
class Mapper:
    """Mapper information."""
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
    """Building information."""
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
    """Tree information."""
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
    """Lamp information."""
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
class Qxmap:
    """HD map information."""
    id: str = ""
    digest: str = ""
    header: Optional[Header] = None
    junctions: List[Junction] = field(default_factory=list)
    segments: List[Segment] = field(default_factory=list)
    roads: List[Road] = field(default_factory=list)
    mappers: List[Mapper] = field(default_factory=list)
    buildings: List[Building] = field(default_factory=list)
    trees: List[Tree] = field(default_factory=list)
    lamps: List[Lamp] = field(default_factory=list)
