# -----------------------------地图相关结构--------------------------------
class Movement:
    map_id: int
    movement_id: str
    upstream_link_id: str
    downstream_link_id: str
    junction_id: str
    flow_direction: str

    def __init__(self):
        self.map_id = None
        self.movement_id = None
        self.upstream_link_id = None
        self.downstream_link_id = None
        self.junction_id = None
        self.flow_direction = None


class Point:
    x: float
    y: float
    z: float

    def __init__(self):
        self.x = None
        self.y = None
        self.z = None


class Position:
    point: Point
    phi: float
    lane_id: str
    link_id: str
    junction_id: str
    segment_id: str
    dis_to_lane_end: float
    position_type: int

    def __init__(self):
        self.point = None
        self.phi = None
        self.lane_id = None
        self.link_id = None
        self.junction_id = None
        self.segment_id = None
        self.dis_to_lane_end = None
        self.position_type = None


class NavigationInfo:
    link_nav: list[str]
    destination: Position

    def __init__(self) -> None:
        self.link_nav = None
        self.destination = None


class LaneNav:
    nav = dict[int, str]

    def __init__(self) -> None:
        self.nav = None


class ReferenceLine:
    lane_ids: list[str]
    lane_types: list[str]
    points: list[Point]
    lane_idxes: list[int]
    opposite: bool

    def __init__(self) -> None:
        self.lane_ids = None
        self.lane_types = None
        self.points = None
        self.lane_idxes = None
        self.opposite = None


class Header:
    north: float
    south: float
    east: float
    west: float
    center_point: Point
    version: str
    zone: float
    use_bias: bool

    def __init__(self) -> None:
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.center_point = None
        self.version = None
        self.zone = None
        self.use_bias = None


class Junction:
    map_id: int
    junction_id: str
    name: str
    type: str
    link_ids: list[str]
    shape: list[Point]
    traffic_light_id: str
    in_segment_ids: list[str]
    out_segment_ids: list[str]

    def __init__(self) -> None:
        self.map_id = None
        self.junction_id = None
        self.name = None
        self.type = None
        self.link_ids = None
        self.shape = None
        self.traffic_light_id = None
        self.in_segment_ids = None
        self.out_segment_ids = None


class Segment:
    map_id: int
    segment_id: str
    name: str
    ordered_link_ids: list[str]
    start_junction_id: str
    end_junction_id: str
    length: float
    heading: float
    traffic_light_pole_id: str
    s_offset: float

    def __init__(self) -> None:
        self.map_id = None
        self.segment_id = None
        self.name = None
        self.ordered_link_ids = None
        self.start_junction_id = None
        self.end_junction_id = None
        self.length = None
        self.heading = None
        self.traffic_light_pole_id = None
        self.s_offset = None


class Link:
    map_id: int
    link_id: str
    pair_id: str
    width: float
    ordered_lane_ids: list[str]
    lane_num: int
    start_point: Point
    end_point: Point
    gradient: float
    segment_id: str
    length: float
    type: str
    heading: float
    link_order: int
    left_boundary: list[Point]
    right_boundary: list[Point]
    road_type: str
    s_offset: float

    def __init__(self) -> None:
        self.map_id = None
        self.link_id = None
        self.pair_id = None
        self.width = None
        self.ordered_lane_ids = None
        self.lane_num = None
        self.start_point = None
        self.end_point = None
        self.gradient = None
        self.segment_id = None
        self.length = None
        self.type = None
        self.heading = None
        self.link_order = None
        self.left_boundary = None
        self.right_boundary = None
        self.road_type = None
        self.s_offset = None


class DirectionPoint:
    point: Point
    pitching: float
    heading: float
    rolling: float

    def __init__(self) -> None:
        self.point = None
        self.pitching = None
        self.heading = None
        self.rolling = None


class Turn:
    direction_point: DirectionPoint
    turn: str
    turn_mapping: dict[str, str]

    def __init__(self) -> None:
        self.direction_point = None
        self.turn = None
        self.turn_mapping = None


class Speed:
    s: float
    length: float
    value: float
    uint: str
    source: str

    def __init__(self) -> None:
        self.s = None
        self.length = None
        self.value = None
        self.uint = None
        self.source = None


class LaneMarkAttribution:
    length: float
    s: float
    start_index: int
    end_index: int
    style: str
    color: str
    width: float

    def __init__(self) -> None:
        self.length = None
        self.s = None
        self.start_index = None
        self.end_index = None
        self.style = None
        self.color = None
        self.width = None


class LaneMark:
    shape: list[Point]
    lane_mark_attrs: list[LaneMarkAttribution]

    def __init__(self) -> None:
        self.shape = None
        self.lane_mark_attrs = None


class Lane:
    map_id: int
    lane_id: str
    type: str
    lane_offset: int
    link_id: str
    turn: Turn
    speeds: list[Speed]
    stopline_id: str
    width: float
    center_line: list[Point]
    connect_link_ids: list[str]
    left_lane_mark: LaneMark
    right_lane_mark: LaneMark
    upstream_link_ids: list[str]
    downstream_link_ids: list[str]
    cut_s_list: list[float]
    length: float


# -------------------------车辆(物体)参数相关结构------------------------------------
class ObjBaseInfo:
    length: int
    width: int
    height: int
    weight: int

    def __init__(self):
        self.length = None
        self.width = None
        self.height = None
        self.weight = None


class DynamicInfo:
    front_wheel_stiffness: float
    rear_wheel_stiffness: float
    front_axle_to_center: float
    rear_axle_to_center: float
    yaw_moment_of_inertia: float

    def __init__(self):
        self.front_wheel_stiffness = None
        self.rear_wheel_stiffness = None
        self.front_axle_to_center = None
        self.rear_axle_to_center = None
        self.yaw_moment_of_inertia = None


class ObjMovingInfo:
    u: float
    u_acc: float
    v: float
    v_acc: float
    w: float
    w_acc: float

    def __init__(self):
        self.u = None
        self.u_acc = None
        self.v = None
        self.v_acc = None
        self.w = None
        self.w_acc = None


class ControlInfo:
    ste_wheel: float  # 方向盘转角[逆时针为正]
    lon_acc: float  # 纵向加速度[m/s^2]
    fl_torque: float  # 左前轮扭矩[N*m]
    fr_torque: float  # 右前轮扭矩[N*m]
    rl_torque: float  # 左后轮扭矩[N*m]
    rr_torque: float  # 右后轮扭矩[N*m]

    def __init__(self):
        self.ste_wheel = None
        self.lon_acc = None
        self.fl_torque = None
        self.fr_torque = None
        self.rl_torque = None
        self.rr_torque = None


class ControlInfo:
    # 方向盘转角[逆时针为正]
    ste_wheel: float  # 使用Optional来模拟omitempty的行为
    # 纵向加速度[m/s^2]
    lon_acc: float
    # 左前轮扭矩[N*m]
    fl_torque: float
    # 右前轮扭矩[N*m]
    fr_torque: float
    # 左后轮扭矩[N*m]
    rl_torque: float
    # 右后轮扭矩[N*m]
    rr_torque: float

    def __init__(self) -> None:
        self.ste_wheel = None
        self.lon_acc = None
        self.fl_torque = None
        self.fr_torque = None
        self.rl_torque = None
        self.rr_torque = None


# -------------------------------------------------------------
class StepRes(object):
    code: int
    message: str

    def __init__(self):
        self.code = None
        self.message = None


class StopRes(object):
    def __init__(self):
        pass


class ResetRes(object):
    def __init__(self):
        pass


class GetCurrentStageRes(object):
    movement_ids: list[str]
    countdown: int

    def __init__(self):
        self.movement_ids = None
        self.countdown = None


class GetMovementSignalRes(object):
    current_signal: int
    countdown: int

    def __init__(self):
        self.current_signal = None
        self.countdown = None


class GetSignalPlanRes_Stage(object):
    movement_ids: list[str]
    duration: int

    def __init__(self):
        self.movement_ids = None
        self.duration = None


class GetSignalPlanRes(object):
    junction_id: str
    cycle: int
    offset: int
    stages: list[GetSignalPlanRes_Stage]

    def __init__(self):
        self.junction_id = None
        self.cycle = None
        self.offset = None
        self.stages = None


class GetMovementListRes:
    list: list[Movement]  # type: ignore

    def __int__(self):
        self.list = None


class GetVehicleIdListRes:
    list: list[str]  # type: ignore

    def __init__(self):
        self.list = None


class GetTestVehicleIdListRes:
    list: list[str]  # type: ignore

    def __init__(self):
        self.list = None


class GetVehicleBaseInfoRes_VehicleBaseInfo:
    obj_base_info: ObjBaseInfo

    def __init__(self):
        self.obj_base_info = None


class GetVehicleBaseInfoRes:
    info_dict: dict[str:GetVehicleBaseInfoRes_VehicleBaseInfo]

    def __init__(self):
        self.info_dict = None


class GetVehiclePositionRes:
    position_dict = dict[str, Position]

    def __init__(self):
        self.position_dict = None
