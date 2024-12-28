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
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        for key, value in data.items():
            setattr(self, key, value)


@dataclass
class ReferencePoint:
    """Reference point information."""
    s: float = 0.0
    heading: float = 0.0
    point: Optional[Point] = None
    height: float = 0.0
    cross_slope: float = 0.0
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        point = data.get("point")
        for key, value in data.items():
            if key != "point":
                setattr(self, key, value)
        self.point = None if point is None else Point(point)


@dataclass
class DirectedPoint:
    """Point with direction."""
    point: Optional[Point] = None
    heading: float = 0.0
    roll: float = 0.0
    patch: float = 0.0
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        point = data.get("point")
        for key, value in data.items():
            if key != "point":
                setattr(self, key, value)
        self.point = None if point is None else Point(point)


@dataclass
class Polygon:
    """Polygon shape."""
    points: List[Point] = field(default_factory=list)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.points = []
            return
        points = data.get("points", [])
        for key, value in data.items():
            if key != "points":
                setattr(self, key, value)
        self.points = [Point(p) for p in points]


@dataclass
class LineString:
    """Line string shape."""
    points: List[Point] = field(default_factory=list)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.points = []
            return
        points = data.get("points", [])
        for key, value in data.items():
            if key != "points":
                setattr(self, key, value)
        self.points = [Point(p) for p in points]


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
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        for key, value in data.items():
            setattr(self, key, value)


@dataclass
class Width:
    """Width information."""
    s: float = 0.0
    a: float = 0.0
    b: float = 0.0
    c: float = 0.0
    d: float = 0.0
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        for key, value in data.items():
            setattr(self, key, value)


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
    type: int = 0
    max_value: float = 0.0
    min_value: float = 0.0
    unit: str = ""
    source: str = ""
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        for key, value in data.items():
            setattr(self, key, value)


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
    style: int = 0
    color: int = 0
    width: float = 0.0
    styles: List[int] = field(default_factory=list)
    colors: List[int] = field(default_factory=list)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.styles = []
            self.colors = []
            return
        for key, value in data.items():
            setattr(self, key, value)


@dataclass
class CenterPoint:
    """Center point information."""
    s: float = 0.0
    heading: float = 0.0
    left_width: float = 0.0
    right_width: float = 0.0
    point: Optional[Point] = None
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        point = data.get("point")
        for key, value in data.items():
            if key != "point":
                setattr(self, key, value)
        self.point = None if point is None else Point(point)


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
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.speed_limits = []
            self.widths = []
            self.center_line = []
            self.upstream_lane_ids = []
            self.downstream_lane_ids = []
            self.left_lane_marks = []
            self.right_lane_marks = []
            return
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
                setattr(self, key, value)
        self.lane_turn = None if lane_turn is None else LaneTurn(lane_turn)
        self.speed_limits = [SpeedLimit(s) for s in speed_limits]
        self.stopline = None if stopline is None else Stopline(stopline)
        self.widths = [Width(w) for w in widths]
        self.center_line = [CenterPoint(c) for c in center_line]
        self.left_lane_marks = [LaneMark(m) for m in left_lane_marks]
        self.right_lane_marks = [LaneMark(m) for m in right_lane_marks]
        self.left_boundary = None if left_boundary is None else LineString(left_boundary)
        self.right_boundary = None if right_boundary is None else LineString(right_boundary)


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
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.pair_ids = []
            self.widths = []
            self.ordered_lanes = []
            self.reference_line = []
            self.upstream_link_ids = []
            self.downstream_link_ids = []
            return
        widths = data.get("widths", [])
        ordered_lanes = data.get("ordered_lanes", [])
        reference_line = data.get("reference_line", [])
        left_boundary = data.get("left_boundary")
        right_boundary = data.get("right_boundary")
        for key, value in data.items():
            if key not in ["widths", "ordered_lanes", "reference_line", "left_boundary", "right_boundary"]:
                setattr(self, key, value)
        self.widths = [Width(w) for w in widths]
        self.ordered_lanes = [Lane(l) for l in ordered_lanes]
        self.reference_line = [ReferencePoint(r) for r in reference_line]
        self.left_boundary = None if left_boundary is None else LineString(left_boundary)
        self.right_boundary = None if right_boundary is None else LineString(right_boundary)


@dataclass
class Movement:
    """Movement information."""
    id: str = ""
    upstream_link_id: str = ""
    downstream_link_id: str = ""
    junction_id: str = ""
    flow_direction: int = 0


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


@dataclass
class Crosswalk:
    """Crosswalk information."""
    id: str = ""
    heading: float = 0.0
    shape: Optional[Polygon] = None
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        shape = data.get("shape")
        for key, value in data.items():
            if key != "shape":
                setattr(self, key, value)
        self.shape = None if shape is None else Polygon(shape)


@dataclass
class SignalPlan_MovementSignal_SignalOfGreen:
    """Signal of green information."""
    green_start: int = 0
    green_duration: int = 0
    yellow: int = 0
    red_clean: int = 0
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        for key, value in data.items():
            setattr(self, key, value)


@dataclass
class SignalPlan_MovementSignal:
    """Movement signal information."""
    movement_id: str = ""
    traffic_light_pole_id: str = ""
    position: Optional[DirectedPoint] = None
    signal_of_greens: List[SignalPlan_MovementSignal_SignalOfGreen] = field(default_factory=list)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.signal_of_greens = []
            return
        position = data.get("position")
        signal_of_greens = data.get("signal_of_greens", [])
        for key, value in data.items():
            if key not in ["position", "signal_of_greens"]:
                setattr(self, key, value)
        self.position = None if position is None else DirectedPoint(position)
        self.signal_of_greens = [SignalPlan_MovementSignal_SignalOfGreen(s) for s in signal_of_greens]


@dataclass
class SignalPlan:
    """Signal plan information."""
    id: str = ""
    junction_id: str = ""
    cycle: int = 0
    offset: int = 0
    is_yellow: bool = False
    movement_signals: Dict[str, SignalPlan_MovementSignal] = field(default_factory=dict)
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.movement_signals = {}
            return
        movement_signals = data.get("movement_signals", {})
        for key, value in data.items():
            if key != "movement_signals":
                setattr(self, key, value)
        self.movement_signals = {k: SignalPlan_MovementSignal(v) for k, v in movement_signals.items()}


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

    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.movements = []
            self.connections = []
            self.crosswalks = []
            self.wait_areas = []
            self.roundabout = []
            self.links = []
            self.upstream_segment_ids = []  # 初始化为空列表
            self.downstream_segment_ids = []  # 初始化为空列表
            return
        
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
                setattr(self, key, value)
                
        self.shape = None if shape is None else Polygon(shape)
        self.movements = [Movement(m) for m in movements]
        self.connections = [Connection(c) for c in connections]
        self.crosswalks = [Crosswalk(c) for c in crosswalks]
        self.wait_areas = [Link(w) for w in wait_areas]
        self.roundabout = [Link(r) for r in roundabout]
        self.links = [Link(l) for l in links]
        self.signal_plan = None if signal_plan is None else SignalPlan(signal_plan)
        self.center = None if center is None else Point(center)
        self.upstream_segment_ids = data.get("upstream_segment_ids", [])
        self.downstream_segment_ids = data.get("downstream_segment_ids", [])

@dataclass
class TrafficSign:
    """Traffic sign information."""
    id: str = ""
    type: int = 0
    position: Optional[DirectedPoint] = None
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        position = data.get("position")
        for key, value in data.items():
            if key != "position":
                setattr(self, key, value)
        self.position = None if position is None else DirectedPoint(position)


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
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.pair_segment_ids = []
            self.ordered_links = []
            self.traffic_signs = []
            return
        ordered_links = data.get("ordered_links", [])
        traffic_signs = data.get("traffic_signs", [])
        for key, value in data.items():
            if key not in ["ordered_links", "traffic_signs"]:
                setattr(self, key, value)
        self.ordered_links = [Link(l) for l in ordered_links]
        self.traffic_signs = [TrafficSign(t) for t in traffic_signs]


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
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.neighbors = []
            self.control_points = []
            self.reference_line = []
            self.sections = []
            self.junction_positions = []
            return
        neighbors = data.get("neighbors", [])
        control_points = data.get("control_points", [])
        reference_line = data.get("reference_line", [])
        sections = data.get("sections", [])
        junction_positions = data.get("junction_positions", [])
        for key, value in data.items():
            if key not in ["neighbors", "control_points", "reference_line", "sections", "junction_positions"]:
                setattr(self, key, value)
        self.neighbors = [RoadPosition(n) for n in neighbors]
        self.control_points = [ControlPoint(c) for c in control_points]
        self.reference_line = [ReferencePoint(r) for r in reference_line]
        self.sections = [Section(s) for s in sections]
        self.junction_positions = [JunctionPosition(j) for j in junction_positions]


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
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        for key, value in data.items():
            setattr(self, key, value)


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
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        pos = data.get("pos")
        shape = data.get("shape")
        for key, value in data.items():
            if key not in ["pos", "shape"]:
                setattr(self, key, value)
        self.pos = None if pos is None else Point(pos)
        self.shape = None if shape is None else Polygon(shape)


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
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        pos = data.get("pos")
        for key, value in data.items():
            if key != "pos":
                setattr(self, key, value)
        self.pos = None if pos is None else Point(pos)


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
    
    def __init__(self, data: dict = None) -> None:
        if data is None:
            return
        pos = data.get("pos")
        for key, value in data.items():
            if key != "pos":
                setattr(self, key, value)
        self.pos = None if pos is None else Point(pos)


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
    def __init__(self, data: dict = None) -> None:
        if data is None:
            self.junctions = []
            self.segments = []
            self.roads = []
            self.mappers = []
            self.buildings = []
            self.trees = []
            self.lamps = []
            return
        header = data.get("header")
        junctions = data.get("junctions", [])
        segments = data.get("segments", [])
        roads = data.get("roads", [])
        mappers = data.get("mappers", [])
        buildings = data.get("buildings", [])
        trees = data.get("trees", [])
        lamps = data.get("lamps", [])
        for key, value in data.items():
            if key not in ["header", "junctions", "segments", "roads", "mappers", "buildings", "trees", "lamps"]:
                setattr(self, key, value)
        self.header = None if header is None else Header(header)
        self.junctions = [Junction(j) for j in junctions]
        self.segments = [Segment(s) for s in segments]
        self.roads = [Road(r) for r in roads]
        self.mappers = [Mapper(m) for m in mappers]
        self.buildings = [Building(b) for b in buildings]
        self.trees = [Tree(t) for t in trees]
        self.lamps = [Lamp(l) for l in lamps]
