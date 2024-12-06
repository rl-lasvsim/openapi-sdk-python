from dataclasses import dataclass


# -----------------------------地图相关结构--------------------------------
@dataclass
class Movement:
    map_id: int = None
    movement_id: str = None
    upstream_link_id: str = None
    downstream_link_id: str = None
    junction_id: str = None
    flow_direction: str = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


@dataclass
class Point:
    x: float = None
    y: float = None
    z: float = 0

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data


@dataclass
class Position:
    point: Point = None
    phi: float = None
    lane_id: str = None
    link_id: str = None
    junction_id: str = None
    segment_id: str = None
    dis_to_lane_end: float = None
    position_type: int = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        point = data.pop("point", None)

        self.__dict__ = data
        self.point = None if point == None else Point(point)


@dataclass
class NavigationInfo:
    link_nav: list[str] = None
    destination: Position = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        destination = data.pop("destination", None)

        self.__dict__ = data
        self.destination = None if destination == None else Position(destination)


@dataclass
class LaneNav:
    nav: dict[int, str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class ReferenceLine:
    lane_ids: list[str] = None
    lane_types: list[str] = None
    points: list[Point] = None
    lane_idxes: list[int] = None
    opposite: bool = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        points = data.pop("points", None)

        self.__dict__ = data
        self.points = None if points == None else [Point(point) for point in points]


@dataclass
class Header:
    north: float = None
    south: float = None
    east: float = None
    west: float = None
    center_point: Point = None
    version: str = None
    zone: float = None
    use_bias: bool = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        center_point = data.pop("center_point", None)

        self.__dict__ = data
        self.center_point = None if center_point == None else Point(center_point)


@dataclass
class Junction:
    map_id: int = None
    junction_id: str = None
    name: str = None
    type: str = None
    link_ids: list[str] = None
    shape: list[Point] = None
    traffic_light_id: str = None
    in_segment_ids: list[str] = None
    out_segment_ids: list[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        shape = data.pop("shape", None)

        self.__dict__ = data
        self.shape = None if shape == None else [Point(point) for point in shape]


@dataclass
class Segment:
    map_id: int = None
    segment_id: str = None
    name: str = None
    ordered_link_ids: list[str] = None
    start_junction_id: str = None
    end_junction_id: str = None
    length: float = None
    heading: float = None
    traffic_light_pole_id: str = None
    s_offset: float = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class Link:
    map_id: int = None
    link_id: str = None
    pair_id: str = None
    width: float = None
    ordered_lane_ids: list[str] = None
    lane_num: int = None
    start_point: Point = None
    end_point: Point = None
    gradient: float = None
    segment_id: str = None
    length: float = None
    type: str = None
    heading: float = None
    link_order: int = None
    left_boundary: list[Point] = None
    right_boundary: list[Point] = None
    road_type: str = None
    s_offset: float = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        start_point = data.pop("start_point", None)
        end_point = data.pop("end_point", None)
        left_boundary = data.pop("left_boundary", None)
        right_boundary = data.pop("right_boundary", None)

        self.__dict__ = data
        self.start_point = None if start_point == None else Point(start_point)
        self.end_point = None if end_point == None else Point(end_point)
        self.left_boundary = (
            None if left_boundary == None else [Point(point) for point in left_boundary]
        )
        self.right_boundary = (
            None
            if right_boundary == None
            else [Point(point) for point in right_boundary]
        )


@dataclass
class DirectionPoint:
    point: Point = None
    pitching: float = None
    heading: float = None
    rolling: float = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        point = data.pop("point", None)

        self.__dict__ = data
        self.point = None if point == None else Point(point)


@dataclass
class Turn:
    direction_point: DirectionPoint = None
    turn: str = None
    turn_mapping: dict[str, str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        direction_point = data.pop("direction_point", None)

        self.__dict__ = data
        self.direction_point = (
            None if direction_point == None else DirectionPoint(direction_point)
        )


@dataclass
class Speed:
    s: float = None
    length: float = None
    value: float = None
    uint: str = None
    source: str = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class LaneMarkAttribution:
    length: float = None
    s: float = None
    start_index: int = None
    end_index: int = None
    style: str = None
    color: str = None
    width: float = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class LaneMark:
    shape: list[Point] = None
    lane_mark_attrs: list[LaneMarkAttribution] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        shape = data.pop("shape", None)
        lane_mark_attrs = data.pop("lane_mark_attrs", None)

        self.__dict__ = data
        self.shape = None if shape == None else [Point(point) for point in shape]
        self.lane_mark_attrs = (
            None
            if lane_mark_attrs == None
            else [LaneMarkAttribution(la) for la in lane_mark_attrs]
        )


@dataclass
class Lane:
    map_id: int = None
    lane_id: str = None
    type: str = None
    lane_offset: int = None
    link_id: str = None
    turn: Turn = None
    speeds: list[Speed] = None
    stopline_id: str = None
    width: float = None
    center_line: list[Point] = None
    connect_link_ids: list[str] = None
    left_lane_mark: LaneMark = None
    right_lane_mark: LaneMark = None
    upstream_link_ids: list[str] = None
    downstream_link_ids: list[str] = None
    cut_s_list: list[float] = None
    length: float = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        turn = data.pop("turn", None)
        speeds = data.pop("speeds", None)
        center_line = data.pop("center_line", None)
        left_lane_mark = data.pop("left_lane_mark", None)
        right_lane_mark = data.pop("right_lane_mark", None)

        self.__dict__ = data
        self.turn = None if turn == None else Turn(turn)
        self.speeds = None if speeds == None else [Speed(speed) for speed in speeds]
        self.center_line = (
            None if center_line == None else [Point(point) for point in center_line]
        )
        self.left_lane_mark = (
            None if left_lane_mark == None else LaneMark(left_lane_mark)
        )
        self.right_lane_mark = (
            None if right_lane_mark == None else LaneMark(right_lane_mark)
        )


@dataclass
class Turn:
    direction_point: DirectionPoint = None
    turn: str = None
    turn_mapping: dict[str, str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        direction_point = data.pop("direction_point", None)

        self.__dict__ = data
        self.direction_point = (
            None if direction_point == None else DirectionPoint(direction_point)
        )


@dataclass
class Crosswalk:
    map_id: int = None
    crosswalk_id: str = None
    heading: float = None
    shape: list[Point] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        shape = data.pop("shape", None)

        self.__dict__ = data
        self.shape = None if shape == None else [Point(point) for point in shape]


@dataclass
class Stopline:
    map_id: int = None
    stopline_id: str = None
    shape: list[Point] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        shape = data.pop("shape", None)

        self.__dict__ = data
        self.shape = None if shape == None else [Point(point) for point in shape]


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
class TrafficLight_MovementSignal:
    movement_id: str = None
    traffic_light_pole_id: str = None
    signal_of_green: list[TrafficLight_MovementSignal_SignalOfGreen] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        signal_of_green = data.pop("signal_of_green", None)

        self.__dict__ = data
        self.signal_of_green = (
            None
            if signal_of_green == None
            else [
                TrafficLight_MovementSignal_SignalOfGreen(signal)
                for signal in signal_of_green
            ]
        )


@dataclass
class TrafficLight:
    map_id: int = None
    traffic_light_id: str = None
    junction_id: str = None
    cycle: int = None
    offset: int = None
    is_yellow: bool = None
    movement_signals: dict[str, TrafficLight_MovementSignal] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        movement_signals = data.pop("movement_signals", None)

        self.__dict__ = data
        self.movement_signals = (
            None
            if movement_signals == None
            else {
                key: TrafficLight_MovementSignal(value)
                for key, value in movement_signals
            }
        )


@dataclass
class TrafficSign:
    map_id: int = None
    traffic_sign_id: str = None
    type: str = None
    direction_point: DirectionPoint = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        direction_point = data.pop("direction_point", None)

        self.__dict__ = data
        self.direction_point = (
            None if direction_point == None else DirectionPoint(direction_point)
        )


@dataclass
class Connection:
    map_id: int = None
    connection_id: str = None
    junction_id: str = None
    movement_id: str = None
    upstream_lane_id: str = None
    downstream_lane_id: str = None
    path: list[Point] = None
    flow_direction: str = None
    upstream_link_id: str = None
    downstream_link_id: str = None
    type: str = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        path = data.pop("path", None)

        self.__dict__ = data
        self.path = None if path == None else [Point(point) for point in path]


# -------------------------车辆(物体)参数相关结构------------------------------------
@dataclass
class ObjBaseInfo:
    length: int = None
    width: int = None
    height: int = None
    weight: int = None

    def __init__(self, data: dict):
        if data == None:
            return
        self.__dict__ = data


@dataclass
class DynamicInfo:
    front_wheel_stiffness: float = None
    rear_wheel_stiffness: float = None
    front_axle_to_center: float = None
    rear_axle_to_center: float = None
    yaw_moment_of_inertia: float = None

    def __init__(self, data: dict):
        if data == None:
            return
        self.__dict__ = data


@dataclass
class ObjMovingInfo:
    u: float = None
    u_acc: float = None
    v: float = None
    v_acc: float = None
    w: float = None
    w_acc: float = None

    def __init__(self, data: dict):
        if data == None:
            return
        self.__dict__ = data


@dataclass
class ControlInfo:
    ste_wheel: float = None  # 方向盘转角[逆时针为正]
    lon_acc: float = None  # 纵向加速度[m/s^2]
    fl_torque: float = None  # 左前轮扭矩[N*m]
    fr_torque: float = None  # 右前轮扭矩[N*m]
    rl_torque: float = None  # 左后轮扭矩[N*m]
    rr_torque: float = None  # 右后轮扭矩[N*m]

    def __init__(self, data: dict):
        if data == None:
            return
        self.__dict__ = data


# -------------------------------------------------------------
@dataclass
class StepRes(object):
    code: int = None
    message: str = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class StopRes(object):
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class ResetRes(object):
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class GetCurrentStageRes(object):
    movement_ids: list[str] = None
    countdown: int = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class GetMovementSignalRes(object):
    current_signal: int = None
    countdown: int = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class GetSignalPlanRes_Stage(object):
    movement_ids: list[str] = None
    duration: int = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class GetSignalPlanRes(object):
    junction_id: str = None
    cycle: int = None
    offset: int = None
    stages: list[GetSignalPlanRes_Stage] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        stages = data.pop("stages", None)

        self.__dict__ = data
        self.stages = (
            None
            if stages == None
            else [GetSignalPlanRes_Stage(stage) for stage in stages]
        )


@dataclass
class GetMovementListRes:
    list: list[Movement]  # type: ignore

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        list = data.pop("list", None)

        self.list = None if list == None else [Movement[movement] for movement in list]


@dataclass
class GetVehicleIdListRes:
    list: list[str]  # type: ignore

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.list = data.get("list", None)


@dataclass
class GetTestVehicleIdListRes:
    list: list[str]  # type: ignore

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data
        # self.list = data.get("list", None) 两种写法都可以


@dataclass
class GetVehicleBaseInfoRes_VehicleBaseInfo:
    base_info: ObjBaseInfo = None
    dynamic_info: DynamicInfo = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        base_info = data.pop("base_info", None)
        dynamic_info = data.pop("dynamic_info", None)
        # self.__dict__ = data
        # base_info
        self.base_info = None if base_info == None else ObjBaseInfo(base_info)
        # dynamic_info
        self.dynamic_info = None if dynamic_info == None else DynamicInfo(dynamic_info)


@dataclass
class GetVehicleBaseInfoRes:
    info_dict: dict[str:GetVehicleBaseInfoRes_VehicleBaseInfo] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        info_dict = data.pop("info_dict", None)
        # self.__dict__ = data
        self.info_dict = (
            None
            if info_dict == None
            else {
                key: GetVehicleBaseInfoRes_VehicleBaseInfo(value)
                for key, value in info_dict.items()
            }
        )


@dataclass
class GetVehiclePositionRes:
    position_dict: dict[str, Position] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        position_dict = data.pop("position_dict", None)

        # self.__dict__ = data
        self.position_dict = (
            None
            if position_dict == None
            else {key: Position(value) for key, value in position_dict.items()}
        )


@dataclass
class GetVehicleMovingInfoRes:
    moving_info_dict: dict[str, ObjMovingInfo] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        moving_info_dict = data.pop("moving_info_dict", None)
        # self.__dict__ = data
        self.moving_info_dict = (
            None
            if moving_info_dict == None
            else {key: ObjMovingInfo(value) for key, value in moving_info_dict.items()}
        )


@dataclass
class GetVehicleControlInfoRes:
    control_info_dict: dict[str, ControlInfo] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        control_info_dict = data.pop("control_info_dict", None)

        # self.__dict__ = data
        self.control_info_dict = (
            None
            if control_info_dict == None
            else {key: ControlInfo(value) for key, value in control_info_dict.items()}
        )


@dataclass
class GetVehiclePerceptionInfoRes_PerceptionObj:
    object_id: str = None
    base_info: ObjBaseInfo = None
    moving_info: ObjMovingInfo = None
    position: Position = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        base_info = data.pop("base_info", None)
        moving_info = data.pop("moving_info", None)
        position = data.pop("position", None)

        self.__dict__ = data
        self.base_info = None if base_info == None else ObjBaseInfo(base_info)
        self.moving_info = None if moving_info == None else ObjMovingInfo(moving_info)
        self.position = None if position == None else Position(position)


@dataclass
class GetVehiclePerceptionInfoRes:
    list: list[GetVehiclePerceptionInfoRes_PerceptionObj]  # type: ignore

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        list = data.pop("list", None)

        self.list = (
            None
            if list == None
            else [GetVehiclePerceptionInfoRes_PerceptionObj(percep) for percep in list]
        )


@dataclass
class GetVehicleReferenceLinesRes:
    reference_lines: list[ReferenceLine] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        reference_lines = data.pop("reference_lines", None)

        self.reference_lines = (
            None
            if reference_lines == None
            else [ReferenceLine(lines) for lines in reference_lines]
        )


@dataclass
class GetVehiclePlanningInfoRes:
    planning_path: list[Point] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        planning_path = data.pop("planning_path", None)

        self.planning_path = (
            None if planning_path == None else [Point(path) for path in planning_path]
        )


@dataclass
class GetVehicleNavigationInfoRes:
    navigation_info: NavigationInfo

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        navigation_info = data.pop("navigation_info", None)

        self.navigation_info = (
            None if navigation_info == None else NavigationInfo(navigation_info)
        )


@dataclass
class GetVehicleCollisionStatusRes:
    collision_status: bool = False

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class SetVehiclePlanningInfoRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class SetVehicleControlInfoRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class SetVehiclePositionRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class SetVehicleMovingInfoRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class SetVehicleBaseInfoRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class SetVehicleRouteNavRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class SetVehicleLinkNavRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class SetVehicleLaneNavRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class SetVehicleDestinationRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class GetPedIdListRes:
    list: list[str]  # type: ignore

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.list = data.get("list", None)


@dataclass
class GetPedBaseInfoRes:
    base_info_dict: dict[str, ObjBaseInfo] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        base_info_dict = data.pop("base_info_dict", None)

        # self.__dict__ = data
        self.base_info_dict = (
            None
            if base_info_dict == None
            else {key: ObjBaseInfo(value) for key, value in base_info_dict.items()}
        )


@dataclass
class SetPedPositionRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class GetNMVIdListRes:
    list: list[str]  # type: ignore

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.list = data.get("list", None)


@dataclass
class GetNMVBaseInfoRes:
    base_info_dict: dict[str, ObjBaseInfo] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        base_info_dict = data.pop("base_info_dict", None)

        # self.__dict__ = data
        self.base_info_dict = (
            None
            if base_info_dict == None
            else {key: ObjBaseInfo(value) for key, value in base_info_dict.items()}
        )


@dataclass
class SetNMVPositionRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data


@dataclass
class GetVehicleTargetSpeedRes:
    target_speed: float

    def __init__(self, data: dict):
        if data == None:
            return
        self.__dict__ = data
