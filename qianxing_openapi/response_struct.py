# -----------------------------地图相关结构--------------------------------
class Movement:
    map_id: int
    movement_id: str
    upstream_link_id: str
    downstream_link_id: str
    junction_id: str
    flow_direction: str

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


class Point:
    x: float
    y: float
    z: float

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


class Position:
    point: Point
    phi: float
    lane_id: str
    link_id: str
    junction_id: str
    segment_id: str
    dis_to_lane_end: float
    position_type: int

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        point = data.pop("point", None)

        self.__dict__ = data
        self.point = Point(point)


class NavigationInfo:
    link_nav: list[str]
    destination: Position

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        destination = data.pop("destination", None)

        self.__dict__ = data
        self.destination = Position(destination)


class LaneNav:
    nav = dict[int, str]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


class ReferenceLine:
    lane_ids: list[str]
    lane_types: list[str]
    points: list[Point]
    lane_idxes: list[int]
    opposite: bool

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        points = data.pop("points", None)

        self.__dict__ = data
        self.points = [Point(point) for point in points]


class Header:
    north: float
    south: float
    east: float
    west: float
    center_point: Point
    version: str
    zone: float
    use_bias: bool

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        point = data.pop("center_point", None)

        self.__dict__ = data
        self.points = Point(point)


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

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        shape = data.pop("shape", None)

        self.__dict__ = data
        self.shape = [Point(point) for point in shape]


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

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


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

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        start_point = data.pop("start_point", None)
        end_point = data.pop("end_point", None)
        left_boundary = data.pop("left_boundary", None)
        right_boundary = data.pop("right_boundary", None)

        self.__dict__ = data
        self.start_point = Point(start_point)
        self.end_point = Point(end_point)
        self.left_boundary = [Point(point) for point in left_boundary]
        self.right_boundary = [Point(point) for point in right_boundary]


class DirectionPoint:
    point: Point
    pitching: float
    heading: float
    rolling: float

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        point = data.pop("point", None)

        self.__dict__ = data
        self.point = Point(point)


class Turn:
    direction_point: DirectionPoint
    turn: str
    turn_mapping: dict[str, str]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        point = data.pop("direction_point", None)

        self.__dict__ = data
        self.direction_point = DirectionPoint(point)


class Speed:
    s: float
    length: float
    value: float
    uint: str
    source: str

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class LaneMarkAttribution:
    length: float
    s: float
    start_index: int
    end_index: int
    style: str
    color: str
    width: float

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class LaneMark:
    shape: list[Point]
    lane_mark_attrs: list[LaneMarkAttribution]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        shape = data.pop("shape", None)
        lane_mark_attrs = data.pop("lane_mark_attrs", None)

        self.__dict__ = data
        self.shape = [Point(point) for point in shape]
        self.lane_mark_attrs = [LaneMarkAttribution(la) for la in lane_mark_attrs]


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

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        turn = data.pop("turn", None)
        speeds = data.pop("speeds", None)
        center_line = data.pop("center_line", None)
        left_lane_mark = data.pop("left_lane_mark", None)
        right_lane_mark = data.pop("right_lane_mark", None)

        self.__dict__ = data
        self.turn = Turn(turn)
        self.speeds = [Speed(speed) for speed in speeds]
        self.center_line = [Point(point) for point in center_line]
        self.left_lane_mark = LaneMark(left_lane_mark)
        self.right_lane_mark = LaneMark(right_lane_mark)


class Turn:
    direction_point: DirectionPoint
    turn: str
    turn_mapping: dict[str, str]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        direction_point = data.pop("direction_point", None)

        self.__dict__ = data
        self.direction_point = DirectionPoint(direction_point)


class Crosswalk:
    map_id: int
    crosswalk_id: str
    heading: float
    shape: list[Point]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        shape = data.pop("shape", None)

        self.__dict__ = data
        self.shape = [Point(point) for point in shape]


class Stopline:
    map_id: int
    stopline_id: str
    shape: list[Point]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        shape = data.pop("shape", None)

        self.__dict__ = data
        self.shape = [Point(point) for point in shape]


class TrafficLight_MovementSignal_SignalOfGreen:
    green_start: int
    green_duration: int
    yellow: int
    redClean: int

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class TrafficLight_MovementSignal:
    movement_id: str
    traffic_light_pole_id: str
    signal_of_green: list[TrafficLight_MovementSignal_SignalOfGreen]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        signal_of_green = data.pop("signal_of_green", None)

        self.__dict__ = data
        self.signal_of_green = [
            TrafficLight_MovementSignal_SignalOfGreen(signal)
            for signal in signal_of_green
        ]


class TrafficLight:
    map_id: int
    traffic_light_id: str
    junction_id: str
    cycle: int
    offset: int
    is_yellow: bool
    movement_signals: dict[str, TrafficLight_MovementSignal]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        movement_signals = data.pop("movement_signals", None)

        self.__dict__ = data
        self.movement_signals = {
            key: TrafficLight_MovementSignal(value) for key, value in movement_signals
        }


class TrafficSign:
    map_id: int
    traffic_sign_id: str
    type: str
    direction_point: DirectionPoint

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        direction_point = data.pop("direction_point", None)

        self.__dict__ = data
        self.direction_point = DirectionPoint(direction_point)


class Connection:
    map_id: int
    connection_id: str
    junction_id: str
    movement_id: str
    upstream_lane_id: str
    downstream_lane_id: str
    path: list[Point]
    flow_direction: str
    upstream_link_id: str
    downstream_link_id: str
    type: str

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        path = data.pop("path", None)

        self.__dict__ = data
        self.path = [Point(point) for point in path]


# -------------------------车辆(物体)参数相关结构------------------------------------
class ObjBaseInfo:
    length: int
    width: int
    height: int
    weight: int

    def __init__(self, data: dict):
        self.__dict__ = data


class DynamicInfo:
    front_wheel_stiffness: float
    rear_wheel_stiffness: float
    front_axle_to_center: float
    rear_axle_to_center: float
    yaw_moment_of_inertia: float

    def __init__(self, data: dict):
        self.__dict__ = data


class ObjMovingInfo:
    u: float
    u_acc: float
    v: float
    v_acc: float
    w: float
    w_acc: float

    def __init__(self, data: dict):
        self.__dict__ = data


class ControlInfo:
    ste_wheel: float  # 方向盘转角[逆时针为正]
    lon_acc: float  # 纵向加速度[m/s^2]
    fl_torque: float  # 左前轮扭矩[N*m]
    fr_torque: float  # 右前轮扭矩[N*m]
    rl_torque: float  # 左后轮扭矩[N*m]
    rr_torque: float  # 右后轮扭矩[N*m]

    def __init__(self, data: dict):
        self.__dict__ = data


# -------------------------------------------------------------
class StepRes(object):
    code: int
    message: str

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class StopRes(object):
    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class ResetRes(object):
    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class GetCurrentStageRes(object):
    movement_ids: list[str]
    countdown: int

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class GetMovementSignalRes(object):
    current_signal: int
    countdown: int

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class GetSignalPlanRes_Stage(object):
    movement_ids: list[str]
    duration: int

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class GetSignalPlanRes(object):
    junction_id: str
    cycle: int
    offset: int
    stages: list[GetSignalPlanRes_Stage]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        stages = data.pop("stages", None)

        self.__dict__ = data
        self.stages = [GetSignalPlanRes_Stage(stage) for stage in stages]


class GetMovementListRes:
    list: list[Movement]  # type: ignore

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        list = data.pop("list", None)

        self.list = [Movement[movement] for movement in list]


class GetVehicleIdListRes:
    list: list[str]  # type: ignore

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class GetTestVehicleIdListRes:
    list: list[str]  # type: ignore

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class GetVehicleBaseInfoRes_VehicleBaseInfo:
    obj_base_info: ObjBaseInfo

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        base_info = data.pop("obj_base_info", None)
        # self.__dict__ = data
        self.obj_base_info = ObjBaseInfo(base_info)


class GetVehicleBaseInfoRes:
    info_dict: dict[str:GetVehicleBaseInfoRes_VehicleBaseInfo]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        info_dict = data.pop("info_dict", None)

        # self.__dict__ = data
        self.info_dict = {
            key: GetVehicleBaseInfoRes_VehicleBaseInfo(value)
            for key, value in info_dict.items()
        }


class GetVehiclePositionRes:
    position_dict = dict[str, Position]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        position_dict = data.pop("position_dict", None)

        # self.__dict__ = data
        self.position_dict = {
            key: Position(value) for key, value in position_dict.items()
        }


class GetVehicleMovingInfoRes:
    moving_info_dict: dict[str, ObjMovingInfo]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        moving_info_dict = data.pop("moving_info_dict", None)

        # self.__dict__ = data
        self.moving_info_dict = {
            key: ObjMovingInfo(value) for key, value in moving_info_dict.items()
        }


class GetVehicleControlInfoRes:
    control_info_dict: dict[str, ControlInfo]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        control_info_dict = data.pop("control_info_dict", None)

        # self.__dict__ = data
        self.control_info_dict = {
            key: ControlInfo(value) for key, value in control_info_dict.items()
        }


class GetVehiclePerceptionInfoRes_PerceptionObj:
    object_id: str
    base_info: ObjBaseInfo
    moving_info: ObjMovingInfo
    position: Position

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        base_info = data.pop("base_info", None)
        moving_info = data.pop("moving_info", None)
        position = data.pop("position", None)

        self.__dict__ = data
        self.base_info = ObjBaseInfo(base_info)
        self.moving_info = ObjMovingInfo(moving_info)
        self.position = Position(position)


class GetVehiclePerceptionInfoRes:
    list: list[GetVehiclePerceptionInfoRes_PerceptionObj]  # type: ignore

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        list = data.pop("list", None)

        self.list = [
            GetVehiclePerceptionInfoRes_PerceptionObj(percep) for percep in list
        ]


class GetVehicleReferenceLinesRes:
    reference_lines: list[ReferenceLine]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        reference_lines = data.pop("reference_lines", None)

        self.reference_lines = [ReferenceLine(lines) for lines in reference_lines]


class GetVehiclePlanningInfoRes:
    planning_path: list[Point]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        planning_path = data.pop("planning_path", None)

        self.planning_path = [Point(path) for path in planning_path]


class GetVehicleNavigationInfoRes:
    navigation_info: NavigationInfo

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        navigation_info = data.pop("navigation_info", None)

        self.navigation_info = NavigationInfo(navigation_info)


class GetVehicleCollisionStatusRes:
    collision_status: bool

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class SetVehiclePlanningInfoRes:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class SetVehicleControlInfoRes:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class SetVehiclePositionRes:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class SetVehicleMovingInfoRes:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class SetVehicleBaseInfoRes:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class SetVehicleRouteNavRes:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class SetVehicleLinkNavRes:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class SetVehicleLaneNavRes:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class SetVehicleDestinationRes:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class GetPedIdListRes:
    list: list[str]  # type: ignore

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class GetPedBaseInfoRes:
    base_info_dict: dict[str, ObjBaseInfo]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        base_info_dict = data.pop("base_info_dict", None)

        # self.__dict__ = data
        self.base_info_dict = {
            key: ObjBaseInfo(value) for key, value in base_info_dict.items()
        }


class SetPedPositionRes:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class GetNMVIdListRes:
    list: list[str]  # type: ignore

    def __init__(self, data: dict) -> None:
        self.__dict__ = data


class GetNMVBaseInfoRes:
    base_info_dict: dict[str, ObjBaseInfo]

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        base_info_dict = data.pop("base_info_dict", None)

        # self.__dict__ = data
        self.base_info_dict = {
            key: ObjBaseInfo(value) for key, value in base_info_dict.items()
        }


class SetNMVPositionRes:
    def __init__(self, data: dict) -> None:
        self.__dict__ = data
