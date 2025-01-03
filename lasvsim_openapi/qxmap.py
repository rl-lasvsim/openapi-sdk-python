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
    
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        for key, value in data.items():
            setattr(cls, key, value)
        return cls


@dataclass
class ReferencePoint:
    """Reference point information."""
    s: float = 0.0
    heading: float = 0.0
    point: Optional[Point] = None
    height: float = 0.0
    cross_slope: float = 0.0
    
    def __init__(self, s: float = 0.0, heading: float = 0.0, point: Optional[Point] = None, height: float = 0.0, cross_slope: float = 0.0):
        self.s = s
        self.heading = heading
        self.point = point
        self.height = height
        self.cross_slope = cross_slope
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        point = data.get("point")
        for key, value in data.items():
            if key != "point":
                setattr(cls, key, value)
        cls.point = None if point is None else Point.from_dict(point)
        return cls


@dataclass
class DirectedPoint:
    """Point with direction."""
    point: Optional[Point] = None
    heading: float = 0.0
    roll: float = 0.0
    patch: float = 0.0
    
    def __init__(self, point: Optional[Point] = None, heading: float = 0.0, roll: float = 0.0, patch: float = 0.0):
        self.point = point
        self.heading = heading
        self.roll = roll
        self.patch = patch
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        point = data.get("point")
        for key, value in data.items():
            if key != "point":
                setattr(cls, key, value)
        cls.point = None if point is None else Point.from_dict(point)
        return cls


@dataclass
class Polygon:
    """Polygon shape."""
    points: List[Point] = field(default_factory=list)
    
    def __init__(self, points: List[Point] = None):
        self.points = points if points is not None else []
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        points = data.get("points", [])
        cls.points = [Point.from_dict(p) for p in points]
        return cls


@dataclass
class LineString:
    """Line string shape."""
    points: List[Point] = field(default_factory=list)
    
    def __init__(self, points: List[Point] = None):
        self.points = points if points is not None else []
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        points = data.get("points", [])
        cls.points = [Point.from_dict(p) for p in points]
        return cls


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
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        for key, value in data.items():
            setattr(cls, key, value)
        return cls


@dataclass
class JunctionPosition:
    """Junction position information."""
    id: str = ""
    junction_id: str = ""
    s: float = 0.0
    length: float = 0.0
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        for key, value in data.items():
            setattr(cls, key, value)
        return cls


@dataclass
class RoadPosition:
    """Road position information."""
    road_id: str = ""
    road_s: float = 0.0
    s: float = 0.0
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        for key, value in data.items():
            setattr(cls, key, value)
        return cls


@dataclass
class ControlPoint:
    """Control point information."""
    id: str = ""
    point: Optional[Point] = None
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        point = data.get("point")
        for key, value in data.items():
            if key != "point":
                setattr(cls, key, value)
        cls.point = None if point is None else Point.from_dict(point)
        return cls


@dataclass
class Header:
    """Map header information."""
    north: float = 0.0
    south: float = 0.0
    east: float = 0.0
    west: float = 0.0
    source_type: int = 0
    source_version: str = ""
    source_data: str = ""
    source_date: str = ""
    source_coordinate_system: str = ""
    source_projection: str = ""
    source_unit: str = ""
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        for key, value in data.items():
            setattr(cls, key, value)
        return cls


@dataclass
class Width:
    """Width information."""
    s: float = 0.0
    a: float = 0.0
    b: float = 0.0
    c: float = 0.0
    d: float = 0.0
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        for key, value in data.items():
            setattr(cls, key, value)
        return cls


@dataclass
class LaneTurn:
    """Lane turn information."""
    position: Optional[DirectedPoint] = None
    turn_code: str = ""
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        position = data.get("position")
        for key, value in data.items():
            if key != "position":
                setattr(cls, key, value)
        cls.position = None if position is None else DirectedPoint.from_dict(position)
        return cls


@dataclass
class SpeedLimit:
    """Speed limit information."""
    s: float = 0.0
    length: float = 0.0
    type: int = 0
    max_value: float = 0.0
    min_value: float = 0.0
    unit: str = ""
    source: str = ""
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        for key, value in data.items():
            setattr(cls, key, value)
        return cls


@dataclass
class Stopline:
    """Stop line information."""
    id: str = ""
    shape: Optional[LineString] = None
    
    def __init__(self, id: str = "", shape: Optional[LineString] = None):
        self.id = id
        self.shape = shape
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        shape = data.get("shape")
        for key, value in data.items():
            if key != "shape":
                setattr(cls, key, value)
        cls.shape = None if shape is None else LineString.from_dict(shape)
        return cls


@dataclass
class LaneMark:
    """Lane mark information."""
    s: float = 0.0
    length: float = 0.0
    is_merge: bool = False
    style: int = 0
    color: int = 0
    width: float = 0.0
    styles: List[int] = field(default_factory=list)
    colors: List[int] = field(default_factory=list)
    
    def __init__(self, s: float = 0.0, length: float = 0.0):
        self.s = s
        self.length = length
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        for key, value in data.items():
            setattr(cls, key, value)
        return cls


@dataclass
class CenterPoint:
    """Center point information."""
    s: float = 0.0
    heading: float = 0.0
    left_width: float = 0.0
    right_width: float = 0.0
    point: Optional[Point] = None
    
    def __init__(self, s: float = 0.0, heading: float = 0.0, left_width: float = 0.0, right_width: float = 0.0, point: Optional[Point] = None):
        self.s = s
        self.heading = heading
        self.left_width = left_width
        self.right_width = right_width
        self.point = point
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        point = data.get("point")
        for key, value in data.items():
            if key != "point":
                setattr(cls, key, value)
        cls.point = None if point is None else Point.from_dict(point)
        return cls


@dataclass
class Lane:
    """Lane information."""
    id: str = ""
    type: int = 0
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
    
    def __init__(self):
        self.id = ""
        self.type = 0
        self.lane_num = 0
        self.link_id = ""
        self.lane_turn = None
        self.speed_limits = []
        self.stopline = None
        self.widths = []
        self.center_line = []
        self.upstream_lane_ids = []
        self.downstream_lane_ids = []
        self.length = 0.0
        self.left_lane_marks = []
        self.right_lane_marks = []
        self.left_boundary = None
        self.right_boundary = None
        self.width = 0.0

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        lane_turn = data.get("lane_turn")
        speed_limits = data.get("speed_limits", [])
        stopline = data.get("stopline")
        widths = data.get("widths", [])
        center_line = data.get("center_line", [])
        left_lane_marks = data.get("left_lane_marks", [])
        right_lane_marks = data.get("right_lane_marks", [])
        left_boundary = data.get("left_boundary")
        right_boundary = data.get("right_boundary")
        
        for key, value in data.items():
            if key not in ["lane_turn", "speed_limits", "stopline", "widths", "center_line", "left_lane_marks", "right_lane_marks", "left_boundary", "right_boundary"]:
                setattr(cls, key, value)
                
        cls.lane_turn = None if lane_turn is None else LaneTurn.from_dict(lane_turn)
        cls.speed_limits = [SpeedLimit.from_dict(s) for s in speed_limits]
        cls.stopline = None if stopline is None else Stopline.from_dict(stopline)
        cls.widths = [Width.from_dict(w) for w in widths]
        cls.center_line = [CenterPoint.from_dict(c) for c in center_line]
        cls.left_lane_marks = [LaneMark.from_dict(m) for m in left_lane_marks]
        cls.right_lane_marks = [LaneMark.from_dict(m) for m in right_lane_marks]
        cls.left_boundary = None if left_boundary is None else LineString.from_dict(left_boundary)
        cls.right_boundary = None if right_boundary is None else LineString.from_dict(right_boundary)
        return cls


@dataclass
class Link:
    """Link information."""
    id: str = ""
    map_id: str = ""
    name: str = ""
    type: int = 0
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

    def __init__(self):
        self.id = ""
        self.map_id = ""
        self.name = ""
        self.type = 0
        self.pair_ids = []
        self.widths = []
        self.ordered_lanes = []
        self.length = 0.0
        self.s_offset = 0.0
        self.link_num = 0
        self.parent_id = ""
        self.reference_line = []
        self.upstream_link_ids = []
        self.downstream_link_ids = []
        self.left_boundary = None
        self.right_boundary = None

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        widths = data.get("widths", [])
        ordered_lanes = data.get("ordered_lanes", [])
        reference_line = data.get("reference_line", [])
        left_boundary = data.get("left_boundary")
        right_boundary = data.get("right_boundary")

        for key, value in data.items():
            if key not in ["widths", "ordered_lanes", "reference_line", "left_boundary", "right_boundary"]:
                setattr(cls, key, value)

        cls.widths = [Width.from_dict(w) for w in widths]
        cls.ordered_lanes = [Lane.from_dict(l) for l in ordered_lanes]
        cls.reference_line = [ReferencePoint.from_dict(r) for r in reference_line]
        cls.left_boundary = None if left_boundary is None else LineString.from_dict(left_boundary)
        cls.right_boundary = None if right_boundary is None else LineString.from_dict(right_boundary)
        return cls


@dataclass
class Movement:
    """Movement information."""
    id: str = ""
    upstream_link_id: str = ""
    downstream_link_id: str = ""
    junction_id: str = ""
    flow_direction: int = 0
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        for key, value in data.items():
            setattr(cls, key, value)
        return cls


@dataclass
class Connection:
    """Connection information."""
    id: str = ""
    junction_id: str = ""
    movement_id: str = ""
    upstream_lane_id: str = ""
    downstream_lane_id: str = ""
    flow_direction: int = 0
    upstream_link_id: str = ""
    downstream_link_id: str = ""
    path: Optional[LineString] = None
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        path = data.get("path")
        for key, value in data.items():
            if key != "path":
                setattr(cls, key, value)
        cls.path = None if path is None else LineString.from_dict(path)
        return cls


@dataclass
class Crosswalk:
    """Crosswalk information."""
    id: str = ""
    heading: float = 0.0
    shape: Optional[Polygon] = None
    
    def __init__(self, id: str = "", heading: float = 0.0, shape: Optional[Polygon] = None):
        self.id = id
        self.heading = heading
        self.shape = shape
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        shape = data.get("shape")
        for key, value in data.items():
            if key != "shape":
                setattr(cls, key, value)
        cls.shape = None if shape is None else Polygon.from_dict(shape)
        return cls


@dataclass
class SignalPlan_MovementSignal_SignalOfGreen:
    """Signal of green information."""
    green_start: int = 0
    green_duration: int = 0
    yellow: int = 0
    red_clean: int = 0
    
    def __init__(self, green_start: int = 0, green_duration: int = 0, yellow: int = 0, red_clean: int = 0):
        self.green_start = green_start
        self.green_duration = green_duration
        self.yellow = yellow
        self.red_clean = red_clean
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        for key, value in data.items():
            setattr(cls, key, value)
        return cls


@dataclass
class SignalPlan_MovementSignal:
    """Movement signal information."""
    movement_id: str = ""
    traffic_light_pole_id: str = ""
    position: Optional[DirectedPoint] = None
    signal_of_greens: List[SignalPlan_MovementSignal_SignalOfGreen] = field(default_factory=list)
    
    def __init__(self, movement_id: str = "", traffic_light_pole_id: str = "", position: Optional[DirectedPoint] = None):
        self.movement_id = movement_id
        self.traffic_light_pole_id = traffic_light_pole_id
        self.position = position
        self.signal_of_greens = []
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        position = data.get("position")
        signal_of_greens = data.get("signal_of_greens", [])
        for key, value in data.items():
            if key not in ["position", "signal_of_greens"]:
                setattr(cls, key, value)
        cls.position = None if position is None else DirectedPoint.from_dict(position)
        cls.signal_of_greens = [SignalPlan_MovementSignal_SignalOfGreen.from_dict(s) for s in signal_of_greens]
        return cls


@dataclass
class SignalPlan:
    """Signal plan information."""
    id: str = ""
    junction_id: str = ""
    cycle: int = 0
    offset: int = 0
    is_yellow: bool = False
    movement_signals: Dict[str, SignalPlan_MovementSignal] = field(default_factory=dict)
    
    def __init__(self, id: str = "", junction_id: str = "", cycle: int = 0, offset: int = 0, is_yellow: bool = False):
        self.id = id
        self.junction_id = junction_id
        self.cycle = cycle
        self.offset = offset
        self.is_yellow = is_yellow
        self.movement_signals = {}
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        movement_signals = data.get("movement_signals", {})
        for key, value in data.items():
            if key != "movement_signals":
                setattr(cls, key, value)
        cls.movement_signals = {k: SignalPlan_MovementSignal.from_dict(v) for k, v in movement_signals.items()}
        return cls


@dataclass
class Junction:
    id: str = ""
    name: str = ""
    type: int = 0
    center: Point = None
    shape: Polygon = None
    movements: List[Movement] = None
    connections: List[Connection] = None
    crosswalks: List[Crosswalk] = None
    wait_areas: List[Link] = None
    roundabout: List[Link] = None
    links: List[Link] = None
    signal_plan: SignalPlan = None
    upstream_segment_ids: List[str] = None  # 添加这个字段
    downstream_segment_ids: List[str] = None  # 添加这个字段

    def __init__(self, id: str = "", name: str = "", type: int = 0, center: Point = None, shape: Polygon = None):
        self.id = id
        self.name = name
        self.type = type
        self.center = center
        self.shape = shape
        self.movements = []
        self.connections = []
        self.crosswalks = []
        self.wait_areas = []
        self.roundabout = []
        self.links = []
        self.signal_plan = None
        self.upstream_segment_ids = []  # 初始化为空列表
        self.downstream_segment_ids = []  # 初始化为空列表
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        shape = data.get("shape")
        movements = data.get("movements", [])
        connections = data.get("connections", [])
        crosswalks = data.get("crosswalks", [])
        wait_areas = data.get("wait_areas", [])
        roundabout = data.get("roundabout", [])
        links = data.get("links", [])
        signal_plan = data.get("signal_plan")
        center = data.get("center")
        
        for key, value in data.items():
            if key not in ["shape", "movements", "connections", "crosswalks", 
                         "wait_areas", "roundabout", "links", "signal_plan", "center"]:
                setattr(cls, key, value)
                
        cls.shape = None if shape is None else Polygon.from_dict(shape)
        cls.movements = [Movement(m) for m in movements]
        cls.connections = [Connection(c) for c in connections]
        cls.crosswalks = [Crosswalk(c) for c in crosswalks]
        cls.wait_areas = [Link(w) for w in wait_areas]
        cls.roundabout = [Link(r) for r in roundabout]
        cls.links = [Link(l) for l in links]
        cls.signal_plan = None if signal_plan is None else SignalPlan(signal_plan)
        cls.center = None if center is None else Point.from_dict(center)
        cls.upstream_segment_ids = data.get("upstream_segment_ids", [])
        cls.downstream_segment_ids = data.get("downstream_segment_ids", [])
        return cls


@dataclass
class TrafficSign:
    """Traffic sign information."""
    id: str = ""
    type: int = 0
    position: Optional[DirectedPoint] = None
    
    def __init__(self, id: str = "", type: int = 0, position: Optional[DirectedPoint] = None):
        self.id = id
        self.type = type
        self.position = position
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        position = data.get("position")
        for key, value in data.items():
            if key != "position":
                setattr(cls, key, value)
        cls.position = None if position is None else DirectedPoint.from_dict(position)
        return cls


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
    
    def __init__(self, id: str = "", map_id: str = "", name: str = "", start_junction_id: str = "", end_junction_id: str = "", pair_segment_ids: List[str] = None, s_offset: float = 0.0, road_id: str = "", length: float = 0.0):
        self.id = id
        self.map_id = map_id
        self.name = name
        self.start_junction_id = start_junction_id
        self.end_junction_id = end_junction_id
        self.pair_segment_ids = pair_segment_ids if pair_segment_ids is not None else []
        self.s_offset = s_offset
        self.road_id = road_id
        self.length = length
        self.ordered_links = []
        self.traffic_signs = []
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        ordered_links = data.get("ordered_links", [])
        traffic_signs = data.get("traffic_signs", [])
        for key, value in data.items():
            if key not in ["ordered_links", "traffic_signs"]:
                setattr(cls, key, value)
        cls.ordered_links = [Link.from_dict(l) for l in ordered_links]
        cls.traffic_signs = [TrafficSign.from_dict(t) for t in traffic_signs]
        return cls


@dataclass
class Road:
    """Road information."""
    id: str = ""
    map_id: str = ""
    name: str = ""
    type: int = 0
    length: float = 0.0
    neighbors: List[RoadPosition] = field(default_factory=list)
    control_points: List[ControlPoint] = field(default_factory=list)
    reference_line: List[ReferencePoint] = field(default_factory=list)
    sections: List[Section] = field(default_factory=list)
    junction_positions: List[JunctionPosition] = field(default_factory=list)
    
    def __init__(self, id: str = "", map_id: str = "", name: str = "", type: int = 0, length: float = 0.0):
        self.id = id
        self.map_id = map_id
        self.name = name
        self.type = type
        self.length = length
        self.neighbors = []
        self.control_points = []
        self.reference_line = []
        self.sections = []
        self.junction_positions = []
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        neighbors = data.get("neighbors", [])
        control_points = data.get("control_points", [])
        reference_line = data.get("reference_line", [])
        sections = data.get("sections", [])
        junction_positions = data.get("junction_positions", [])
        for key, value in data.items():
            if key not in ["neighbors", "control_points", "reference_line", "sections", "junction_positions"]:
                setattr(cls, key, value)
        cls.neighbors = [RoadPosition.from_dict(n) for n in neighbors]
        cls.control_points = [ControlPoint.from_dict(c) for c in control_points]
        cls.reference_line = [ReferencePoint.from_dict(r) for r in reference_line]
        cls.sections = [Section.from_dict(s) for s in sections]
        cls.junction_positions = [JunctionPosition.from_dict(j) for j in junction_positions]
        return cls


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
    
    def __init__(self, id: str = "", map_id: str = "", origin_xpath: Optional[str] = None, origin_elem_id: str = "", origin_elem_type: str = "", target_xpath: Optional[str] = None, target_elem_id: str = "", target_elem_type: str = ""):
        self.id = id
        self.map_id = map_id
        self.origin_xpath = origin_xpath
        self.origin_elem_id = origin_elem_id
        self.origin_elem_type = origin_elem_type
        self.target_xpath = target_xpath
        self.target_elem_id = target_elem_id
        self.target_elem_type = target_elem_type
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        for key, value in data.items():
            setattr(cls, key, value)
        return cls


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
    
    def __init__(self, id: str = "", pos: Optional[Point] = None, shape: Optional[Polygon] = None, heading: float = 0.0, height: float = 0.0, width: float = 0.0, length: float = 0.0, s: float = 0.0, t: float = 0.0, model_num: int = 0):
        self.id = id
        self.pos = pos
        self.shape = shape
        self.heading = heading
        self.height = height
        self.width = width
        self.length = length
        self.s = s
        self.t = t
        self.model_num = model_num
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        pos = data.get("pos")
        shape = data.get("shape")
        for key, value in data.items():
            if key not in ["pos", "shape"]:
                setattr(cls, key, value)
        cls.pos = None if pos is None else Point.from_dict(pos)
        cls.shape = None if shape is None else Polygon.from_dict(shape)
        return cls


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
    
    def __init__(self, id: str = "", pos: Optional[Point] = None, heading: float = 0.0, height: float = 0.0, width: float = 0.0, length: float = 0.0, s: float = 0.0, t: float = 0.0, model_num: int = 0):
        self.id = id
        self.pos = pos
        self.heading = heading
        self.height = height
        self.width = width
        self.length = length
        self.s = s
        self.t = t
        self.model_num = model_num
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        pos = data.get("pos")
        for key, value in data.items():
            if key != "pos":
                setattr(cls, key, value)
        cls.pos = None if pos is None else Point.from_dict(pos)
        return cls


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
    
    def __init__(self, id: str = "", pos: Optional[Point] = None, heading: float = 0.0, height: float = 0.0, width: float = 0.0, length: float = 0.0, s: float = 0.0, t: float = 0.0, model_num: int = 0):
        self.id = id
        self.pos = pos
        self.heading = heading
        self.height = height
        self.width = width
        self.length = length
        self.s = s
        self.t = t
        self.model_num = model_num
    
    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        pos = data.get("pos")
        for key, value in data.items():
            if key != "pos":
                setattr(cls, key, value)
        cls.pos = None if pos is None else Point.from_dict(pos)
        return cls


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

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        
        header = data.get("header")
        junctions = data.get("junctions", [])
        segments = data.get("segments", [])
        roads = data.get("roads", [])
        mappers = data.get("mappers", [])
        buildings = data.get("buildings", [])
        trees = data.get("trees", [])
        lamps = data.get("lamps", [])
        cls.id = data.get("id", "")

        cls.header = None if header is None else Header.from_dict(header)
        cls.junctions = [Junction.from_dict(j) for j in junctions]
        cls.segments = [Segment.from_dict(s) for s in segments]
        cls.roads = [Road.from_dict(r) for r in roads]
        cls.mappers = [Mapper.from_dict(m) for m in mappers]
        cls.buildings = [Building.from_dict(b) for b in buildings]
        cls.trees = [Tree.from_dict(t) for t in trees]
        cls.lamps = [Lamp.from_dict(l) for l in lamps]

        return cls
