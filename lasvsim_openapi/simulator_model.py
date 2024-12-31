"""
Simulator model module for the lasvsim API.
"""
from typing import Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class Point:
    """Point information."""
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    
    def __init__(self, data: dict = None, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.x = x
        self.y = y
        self.z = z


@dataclass
class ObjBaseInfo:
    """Object base information."""
    width: float = 0.0
    height: float = 0.0
    length: float = 0.0
    weight: float = 0.0
    
    def __init__(self, data: dict = None, width: float = 0.0, height: float = 0.0, length: float = 0.0, weight: float = 0.0):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.width = width
        self.height = height
        self.length = length
        self.weight = weight


@dataclass
class DynamicInfo:
    """Dynamic information."""
    front_wheel_stiffness: float = 0.0
    rear_wheel_stiffness: float = 0.0
    front_axle_to_center: float = 0.0
    rear_axle_to_center: float = 0.0
    yaw_moment_of_inertia: float = 0.0
    
    def __init__(self, data: dict = None, front_wheel_stiffness: float = 0.0, rear_wheel_stiffness: float = 0.0, front_axle_to_center: float = 0.0, rear_axle_to_center: float = 0.0, yaw_moment_of_inertia: float = 0.0):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.front_wheel_stiffness = front_wheel_stiffness
        self.rear_wheel_stiffness = rear_wheel_stiffness
        self.front_axle_to_center = front_axle_to_center
        self.rear_axle_to_center = rear_axle_to_center
        self.yaw_moment_of_inertia = yaw_moment_of_inertia


@dataclass
class Position:
    """Position information."""
    point: Optional[Point] = None
    phi: float = 0.0
    lane_id: str = ""
    link_id: str = ""
    junction_id: str = ""
    segment_id: str = ""
    dis_to_lane_end: Optional[float] = None
    position_type: int = 0  # 1 - 地图外
    
    def __init__(self, data: dict = None, point: Optional[Point] = None, phi: float = 0.0, lane_id: str = "", link_id: str = "", junction_id: str = "", segment_id: str = "", dis_to_lane_end: Optional[float] = None, position_type: int = 0):
        if data is not None:
            _point = data.pop("point", None)
            _dis_to_lane_end = data.pop("dis_to_lane_end", None)
            for key, value in data.items():
                setattr(self, key, value)
            self.point = None if _point is None else Point(_point)
            self.dis_to_lane_end = _dis_to_lane_end
            return
        self.point = point
        self.phi = phi
        self.lane_id = lane_id
        self.link_id = link_id
        self.junction_id = junction_id
        self.segment_id = segment_id
        self.dis_to_lane_end = dis_to_lane_end
        self.position_type = position_type


@dataclass
class ObjMovingInfo:
    """Object moving information."""
    u: float = 0.0
    u_acc: float = 0.0
    v: float = 0.0
    v_acc: float = 0.0
    w: float = 0.0
    w_acc: float = 0.0
    
    def __init__(self, data: dict = None, u: float = 0.0, u_acc: float = 0.0, v: float = 0.0, v_acc: float = 0.0, w: float = 0.0, w_acc: float = 0.0):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.u = u
        self.u_acc = u_acc
        self.v = v
        self.v_acc = v_acc
        self.w = w
        self.w_acc = w_acc


@dataclass
class ControlInfo:
    """Control information."""
    ste_wheel: float = 0.0
    lon_acc: float = 0.0
    fl_torque: float = 0.0
    fr_torque: float = 0.0
    rl_torque: float = 0.0
    rr_torque: float = 0.0
    
    def __init__(self, data: dict = None, ste_wheel: float = 0.0, lon_acc: float = 0.0, fl_torque: float = 0.0, fr_torque: float = 0.0, rl_torque: float = 0.0, rr_torque: float = 0.0):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.ste_wheel = ste_wheel
        self.lon_acc = lon_acc
        self.fl_torque = fl_torque
        self.fr_torque = fr_torque
        self.rl_torque = rl_torque
        self.rr_torque = rr_torque


@dataclass
class ReferenceLine:
    """Reference line information."""
    lane_ids: List[str] = field(default_factory=list)
    lane_types: List[str] = field(default_factory=list)
    points: List[Point] = field(default_factory=list)
    lane_idxes: List[int] = field(default_factory=list)
    opposite: bool = False
    
    def __init__(self, data: dict = None, lane_ids: List[str] = None, lane_types: List[str] = None, points: List[Point] = None, lane_idxes: List[int] = None, opposite: bool = False):
        if data is not None:
            self.lane_ids = []
            self.lane_types = []
            self.points = []
            self.lane_idxes = []
            for key, value in data.items():
                if key == "points":
                    value = [Point(point) for point in value]
                setattr(self, key, value)
            return
        self.lane_ids = lane_ids if lane_ids is not None else []
        self.lane_types = lane_types if lane_types is not None else []
        self.points = points if points is not None else []
        self.lane_idxes = lane_idxes if lane_idxes is not None else []
        self.opposite = opposite


@dataclass
class NavigationInfo:
    """Navigation information."""
    link_nav: List[str] = field(default_factory=list)
    destination: Optional[Position] = None

    def __init__(self, data: dict = None, link_nav: List[str] = None, destination: Optional[Position] = None):
        if data is not None:
            self.link_nav = []
            _destination = data.pop("destination", None)
            for key, value in data.items():
                setattr(self, key, value)
            self.destination = None if _destination is None else Position(_destination)
            return
        self.link_nav = link_nav if link_nav is not None else []
        self.destination = destination


@dataclass
class Movement:
    """Movement information."""
    map_id: int = 0
    movement_id: str = ""
    upstream_link_id: str = ""
    downstream_link_id: str = ""
    junction_id: str = ""
    flow_direction: str = ""

    def __init__(self, data: dict = None, map_id: int = 0, movement_id: str = "", upstream_link_id: str = "", downstream_link_id: str = "", junction_id: str = "", flow_direction: str = ""):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.map_id = map_id
        self.movement_id = movement_id
        self.upstream_link_id = upstream_link_id
        self.downstream_link_id = downstream_link_id
        self.junction_id = junction_id
        self.flow_direction = flow_direction


@dataclass
class LaneNav:
    """Lane navigation information."""
    nav: Dict[int, str] = field(default_factory=dict)


@dataclass
class SimulatorConfig:
    """Simulator configuration."""
    scen_id: str = ""
    scen_ver: str = ""
    sim_record_id: str = ""

    def __init__(self, data: dict = None, scen_id: str = "", scen_ver: str = "", sim_record_id: str = ""):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.scen_id = scen_id
        self.scen_ver = scen_ver
        self.sim_record_id = sim_record_id


@dataclass
class InitReq:
    """Request for initializing simulator."""
    scen_id: str = ""
    scen_ver: str = ""
    sim_record_id: str = ""

    def __init__(self, data: dict = None, scen_id: str = "", scen_ver: str = "", sim_record_id: str = ""):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.scen_id = scen_id
        self.scen_ver = scen_ver
        self.sim_record_id = sim_record_id


@dataclass
class InitRes:
    """Response for initializing simulator."""
    simulation_id: str = ""
    simulation_addr: str = ""

    def __init__(self, data: dict = None, simulation_id: str = "", simulation_addr: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.simulation_addr = simulation_addr


@dataclass
class StopReq:
    """Request for stopping simulator."""
    simulation_id: str = ""

    def __init__(self, data: dict = None, simulation_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id


@dataclass
class StopRes:
    """Response for stopping simulator."""
    pass


@dataclass
class StepReq:
    """Request for stepping simulator."""
    simulation_id: str = ""

    def __init__(self, data: dict = None, simulation_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id


@dataclass
class StepRes:
    def __init__(self, data: dict = None) -> None:
        pass


@dataclass
class GetCurrentStageReq:
    """Request for getting current stage."""
    simulation_id: str = ""  # 仿真ID
    junction_id: str = ""  # movementId

    def __init__(self, data: dict = None, simulation_id: str = "", junction_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.junction_id = junction_id


@dataclass
class GetCurrentStageRes:
    """Response for getting current stage."""
    movement_ids: List[str] = field(default_factory=list)  # 当前阶段包含的绿灯流向
    countdown: int = 0  # 倒计时(s)

    def __init__(self, data: dict = None, movement_ids: List[str] = None, countdown: int = 0):
        if data is not None:
            self.movement_ids = []
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.movement_ids = movement_ids if movement_ids is not None else []
        self.countdown = countdown


@dataclass
class GetMovementSignalReq:
    """Request for getting movement signal."""
    simulation_id: str = ""  # 仿真ID
    movement_id: str = ""  # movementId

    def __init__(self, data: dict = None, simulation_id: str = "", movement_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.movement_id = movement_id


@dataclass
class GetMovementSignalRes:
    """Response for getting movement signal."""
    current_signal: int = 0  # 当前灯色
    countdown: int = 0  # 倒计时(s)

    def __init__(self, data: dict = None, current_signal: int = 0, countdown: int = 0):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.current_signal = current_signal
        self.countdown = countdown


@dataclass
class GetSignalPlanRes_Stage:
    """Stage information in signal plan."""
    movement_ids: List[str] = field(default_factory=list)
    duration: int = 0  # 时长(s)

    def __init__(self, data: dict = None, movement_ids: List[str] = None, duration: int = 0):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.movement_ids = movement_ids if movement_ids is not None else []
        self.duration = duration


@dataclass
class GetSignalPlanReq:
    """Request for getting signal plan."""
    simulation_id: str = ""
    junction_id: str = ""

    def __init__(self, data: dict = None, simulation_id: str = "", junction_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.junction_id = junction_id


@dataclass
class GetSignalPlanRes:
    """Response for getting signal plan."""
    junction_id: str = ""
    cycle: int = 0
    offset: int = 0
    stages: List[GetSignalPlanRes_Stage] = field(default_factory=list)

    def __init__(self, data: dict = None, junction_id: str = "", cycle: int = 0, offset: int = 0, stages: List[GetSignalPlanRes_Stage] = None):
        if data is not None:
            self.stages = []
            _stages = data.pop("stages", [])
            for key, value in data.items():
                setattr(self, key, value)
            self.stages = [GetSignalPlanRes_Stage(stage) for stage in _stages]
            return
        self.junction_id = junction_id
        self.cycle = cycle
        self.offset = offset
        self.stages = stages if stages is not None else []


@dataclass
class GetMovementListReq:
    """Request for getting movement list."""
    simulation_id: str = ""
    junction_id: str = ""

    def __init__(self, data: dict = None, simulation_id: str = "", junction_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.junction_id = junction_id


@dataclass
class GetMovementListRes:
    """Response for getting movement list."""
    list: List[Movement] = field(default_factory=list)  # movement 列表

    def __init__(self, data: dict = None, list: List[Movement] = None):
        if data is not None:
            self.list = []
            for key, value in data.items():
                if key == "list":
                    value = [Movement(item) for item in value]
                setattr(self, key, value)
            return
        self.list = list if list is not None else []


@dataclass
class GetVehicleIdListReq:
    """Request for getting vehicle ID list."""
    simulation_id: str = ""  # 仿真ID

    def __init__(self, data: dict = None, simulation_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id


@dataclass
class GetVehicleIdListRes:
    """Response for getting vehicle ID list."""
    list: List[str] = field(default_factory=list)  # 车辆ID列表

    def __init__(self, data: dict = None, list: List[str] = None):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.list = list if list is not None else []


@dataclass
class GetTestVehicleIdListReq:
    """Request for getting test vehicle ID list."""
    simulation_id: str = ""  # 仿真ID

    def __init__(self, data: dict = None, simulation_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id


@dataclass
class GetTestVehicleIdListRes:
    """Response for getting test vehicle ID list."""
    list: List[str] = field(default_factory=list)

    def __init__(self, data: dict = None, list: List[str] = None):
        if data is not None:
            self.list = []
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.list = list if list is not None else []


@dataclass
class GetVehicleBaseInfoReq:
    """Request for getting vehicle base information."""
    simulation_id: str = ""
    id_list: List[str] = field(default_factory=list)

    def __init__(self, data: dict = None, simulation_id: str = "", id_list: List[str] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.id_list = id_list if id_list is not None else []


@dataclass
class GetVehicleBaseInfoRes_VehicleBaseInfo:
    """Vehicle base information."""
    base_info: Optional[ObjBaseInfo] = None
    dynamic_info: Optional[DynamicInfo] = None

    def __init__(self, data: dict = None, base_info: Optional[ObjBaseInfo] = None, dynamic_info: Optional[DynamicInfo] = None):
        if data is not None:
            base_info = data.pop("base_info", None)
            dynamic_info = data.pop("dynamic_info", None)
            for key, value in data.items():
                setattr(self, key, value)
            self.base_info = None if base_info is None else ObjBaseInfo(base_info)
            self.dynamic_info = None if dynamic_info is None else DynamicInfo(dynamic_info)
            return
        self.base_info = base_info
        self.dynamic_info = dynamic_info


@dataclass
class GetVehicleBaseInfoRes:
    """Response for getting vehicle base information."""
    info_dict: Dict[str, GetVehicleBaseInfoRes_VehicleBaseInfo] = field(default_factory=dict)

    def __init__(self, data: dict = None, info_dict: Dict[str, GetVehicleBaseInfoRes_VehicleBaseInfo] = None):
        if data is not None:
            info_dict = data.pop("info_dict", {})
            for key, value in data.items():
                setattr(self, key, value)
            self.info_dict = {k: GetVehicleBaseInfoRes_VehicleBaseInfo(v) for k, v in info_dict.items()}
            return
        self.info_dict = info_dict if info_dict is not None else {}


@dataclass
class GetVehiclePositionReq:
    """Request for getting vehicle position."""
    simulation_id: str = ""
    id_list: List[str] = field(default_factory=list)

    def __init__(self, data: dict = None, simulation_id: str = "", id_list: List[str] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.id_list = id_list if id_list is not None else []


@dataclass
class GetVehiclePositionRes:
    """Response for getting vehicle position."""
    position_dict: Dict[str, Position] = field(default_factory=dict)

    def __init__(self, data: dict = None, position_dict: Dict[str, Position] = None):
        if data is not None:
            self.position_dict = {}
            _position_dict = data.pop("position_dict", {})
            for key, value in data.items():
                setattr(self, key, value)
            self.position_dict = {k: Position(v) for k, v in _position_dict.items()}
            return
        self.position_dict = position_dict if position_dict is not None else {}


@dataclass
class GetVehicleMovingInfoReq:
    """Request for getting vehicle moving information."""
    simulation_id: str = ""
    id_list: List[str] = field(default_factory=list)

    def __init__(self, data: dict = None, simulation_id: str = "", id_list: List[str] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.id_list = id_list if id_list is not None else []


@dataclass
class GetVehicleMovingInfoRes:
    """Response for getting vehicle moving information."""
    moving_info_dict: Dict[str, ObjMovingInfo] = field(default_factory=dict)

    def __init__(self, data: dict = None, moving_info_dict: Dict[str, ObjMovingInfo] = None):
        if data is not None:
            moving_info_dict = data.pop("moving_info_dict", {})
            for key, value in data.items():
                setattr(self, key, value)
            self.moving_info_dict = {k: ObjMovingInfo(v) for k, v in moving_info_dict.items()}
            return
        self.moving_info_dict = moving_info_dict if moving_info_dict is not None else {}


@dataclass
class GetVehicleControlInfoReq:
    """Request for getting vehicle control information."""
    simulation_id: str = ""
    id_list: List[str] = field(default_factory=list)

    def __init__(self, data: dict = None, simulation_id: str = "", id_list: List[str] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.id_list = id_list if id_list is not None else []


@dataclass
class GetVehicleControlInfoRes:
    """Response for getting vehicle control information."""
    control_info_dict: Dict[str, ControlInfo] = field(default_factory=dict)

    def __init__(self, data: dict = None, control_info_dict: Dict[str, ControlInfo] = None):
        if data is not None:
            self.control_info_dict = {}
            _control_info_dict = data.pop("control_info_dict", {})
            for key, value in data.items():
                setattr(self, key, value)
            self.control_info_dict = {k: ControlInfo(v) for k, v in _control_info_dict.items()}
            return
        self.control_info_dict = control_info_dict if control_info_dict is not None else {}


@dataclass
class GetVehiclePerceptionInfoReq:
    """Request for getting vehicle perception information."""
    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id


@dataclass
class GetVehiclePerceptionInfoRes_PerceptionObj:
    """Perception object information."""
    obj_id: str = ""
    base_info: Optional[ObjBaseInfo] = None
    moving_info: Optional[ObjMovingInfo] = None
    position: Optional[Position] = None

    def __init__(self, data: dict = None, obj_id: str = "", base_info: Optional[ObjBaseInfo] = None, moving_info: Optional[ObjMovingInfo] = None, position: Optional[Position] = None):
        if data is not None:
            base_info = data.pop("base_info", None)
            moving_info = data.pop("moving_info", None)
            position = data.pop("position", None)
            for key, value in data.items():
                setattr(self, key, value)
            self.base_info = None if base_info is None else ObjBaseInfo(base_info)
            self.moving_info = None if moving_info is None else ObjMovingInfo(moving_info)
            self.position = None if position is None else Position(position)
            return
        self.obj_id = obj_id
        self.base_info = base_info
        self.moving_info = moving_info
        self.position = position


@dataclass
class GetVehiclePerceptionInfoRes:
    """Response for getting vehicle perception information."""
    list: List[GetVehiclePerceptionInfoRes_PerceptionObj] = field(default_factory=list)

    def __init__(self, data: dict = None, list: List[GetVehiclePerceptionInfoRes_PerceptionObj] = None):
        if data is not None:
            self.list = []
            _list = data.pop("list", [])
            for key, value in data.items():
                setattr(self, key, value)
            self.list = [GetVehiclePerceptionInfoRes_PerceptionObj(item) for item in _list]
            return
        self.list = list if list is not None else []


@dataclass
class GetVehicleReferenceLinesReq:
    """Request for getting vehicle reference lines."""
    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id


@dataclass
class GetVehicleReferenceLinesRes:
    """Response for getting vehicle reference lines."""
    reference_lines: List[ReferenceLine] = field(default_factory=list)

    def __init__(self, data: dict = None, reference_lines: List[ReferenceLine] = None):
        if data is not None:
            reference_lines = data.pop("reference_lines", [])
            for key, value in data.items():
                setattr(self, key, value)
            self.reference_lines = [ReferenceLine(item) for item in reference_lines]
            return
        self.reference_lines = reference_lines if reference_lines is not None else []


@dataclass
class GetVehiclePlanningInfoReq:
    """Request for getting vehicle planning information."""
    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id


@dataclass
class GetVehiclePlanningInfoRes:
    """Response for getting vehicle planning information."""
    planning_path: List[Point] = field(default_factory=list)

    def __init__(self, data: dict = None, planning_path: List[Point] = None):
        if data is not None:
            planning_path = data.pop("planning_path", [])
            for key, value in data.items():
                setattr(self, key, value)
            self.planning_path = [Point(item) for item in planning_path]
            return
        self.planning_path = planning_path if planning_path is not None else []


@dataclass
class GetVehicleNavigationInfoReq:
    """Request for getting vehicle navigation information."""
    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id


@dataclass
class GetVehicleNavigationInfoRes:
    """Response for getting vehicle navigation information."""
    navigation_info: Optional[NavigationInfo] = None

    def __init__(self, data: dict = None, navigation_info: Optional[NavigationInfo] = None):
        if data is not None:
            _navigation_info = data.pop("navigation_info", None)
            for key, value in data.items():
                setattr(self, key, value)
            self.navigation_info = None if _navigation_info is None else NavigationInfo(_navigation_info)
            return
        self.navigation_info = navigation_info


@dataclass
class GetVehicleCollisionStatusReq:
    """Request for getting vehicle collision status."""
    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id


@dataclass
class GetVehicleCollisionStatusRes:
    """Response for getting vehicle collision status."""
    collision_status: bool = False

    def __init__(self, data: dict = None, collision_status: bool = False):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.collision_status = collision_status


@dataclass
class GetVehicleTargetSpeedReq:
    """Request for getting vehicle target speed."""
    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id


@dataclass
class GetVehicleTargetSpeedRes:
    """Response for getting vehicle target speed."""
    target_speed: float = 0.0

    def __init__(self, data: dict = None, target_speed: float = 0.0):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.target_speed = target_speed


@dataclass
class SetVehiclePlanningInfoReq:
    """Request for setting vehicle planning information."""
    simulation_id: str = ""
    vehicle_id: str = ""
    planning_path: List[Point] = field(default_factory=list)

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = "", planning_path: List[Point] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.planning_path = planning_path if planning_path is not None else []


@dataclass
class SetVehiclePlanningInfoRes:
    """Response for setting vehicle planning information."""
    pass


@dataclass
class SetVehicleControlInfoReq:
    """Request for setting vehicle control information."""
    simulation_id: str = ""
    vehicle_id: str = ""
    ste_wheel: Optional[float] = None
    lon_acc: Optional[float] = None

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = "", ste_wheel: Optional[float] = None, lon_acc: Optional[float] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.ste_wheel = ste_wheel
        self.lon_acc = lon_acc


@dataclass
class SetVehicleControlInfoRes:
    """Response for setting vehicle control information."""
    pass


@dataclass
class SetVehiclePositionReq:
    """Request for setting vehicle position."""
    simulation_id: str = ""
    vehicle_id: str = ""
    point: Optional[Point] = None
    phi: Optional[float] = None

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = "", point: Optional[Point] = None, phi: Optional[float] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.point = point
        self.phi = phi


@dataclass
class SetVehiclePositionRes:
    """Response for setting vehicle position."""
    pass


@dataclass
class SetVehicleMovingInfoReq:
    """Request for setting vehicle moving information."""
    simulation_id: str = ""
    vehicle_id: str = ""
    u: Optional[float] = None
    v: Optional[float] = None
    w: Optional[float] = None
    u_acc: Optional[float] = None
    v_acc: Optional[float] = None
    w_acc: Optional[float] = None

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = "", u: Optional[float] = None, v: Optional[float] = None, w: Optional[float] = None, u_acc: Optional[float] = None, v_acc: Optional[float] = None, w_acc: Optional[float] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.u = u
        self.v = v
        self.w = w
        self.u_acc = u_acc
        self.v_acc = v_acc
        self.w_acc = w_acc


@dataclass
class SetVehicleMovingInfoRes:
    """Response for setting vehicle moving information."""
    pass


@dataclass
class SetVehicleBaseInfoReq:
    """Request for setting vehicle base information."""
    simulation_id: str = ""
    vehicle_id: str = ""
    base_info: Optional[ObjBaseInfo] = None
    dynamic_info: Optional[DynamicInfo] = None

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = "", base_info: Optional[ObjBaseInfo] = None, dynamic_info: Optional[DynamicInfo] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.base_info = base_info
        self.dynamic_info = dynamic_info


@dataclass
class SetVehicleBaseInfoRes:
    """Response for setting vehicle base information."""
    pass


@dataclass
class SetVehicleRouteNavReq:
    """Request for setting vehicle route navigation."""
    simulation_id: str = ""
    vehicle_id: str = ""
    route_nav: List[str] = field(default_factory=list)

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = "", route_nav: List[str] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.route_nav = route_nav if route_nav is not None else []


@dataclass
class SetVehicleRouteNavRes:
    """Response for setting vehicle route navigation."""
    pass


@dataclass
class SetVehicleLinkNavReq:
    """Request for setting vehicle link navigation."""
    simulation_id: str = ""
    vehicle_id: str = ""
    link_nav: List[str] = field(default_factory=list)

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = "", link_nav: List[str] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.link_nav = link_nav if link_nav is not None else []


@dataclass
class SetVehicleLinkNavRes:
    """Response for setting vehicle link navigation."""
    pass


@dataclass
class SetVehicleLaneNavReq:
    """Request for setting vehicle lane navigation."""
    simulation_id: str = ""
    vehicle_id: str = ""
    lane_nav: List[LaneNav] = field(default_factory=list)

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = "", lane_nav: List[LaneNav] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.lane_nav = lane_nav if lane_nav is not None else []


@dataclass
class SetVehicleLaneNavRes:
    """Response for setting vehicle lane navigation."""
    pass


@dataclass
class SetVehicleDestinationReq:
    """Request for setting vehicle destination."""
    simulation_id: str = ""
    vehicle_id: str = ""
    destination: Optional[Point] = None

    def __init__(self, data: dict = None, simulation_id: str = "", vehicle_id: str = "", destination: Optional[Point] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.destination = destination


@dataclass
class SetVehicleDestinationRes:
    """Response for setting vehicle destination."""
    pass


@dataclass
class GetPedIdListReq:
    """Request for getting pedestrian ID list."""
    simulation_id: str = ""  # 仿真ID

    def __init__(self, data: dict = None, simulation_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id


@dataclass
class GetPedIdListRes:
    """Response for getting pedestrian ID list."""
    list: List[str] = field(default_factory=list)  # 行人ID列表

    def __init__(self, data: dict = None, list: List[str] = None):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.list = list if list is not None else []


@dataclass
class GetPedBaseInfoReq:
    """Request for getting pedestrian base information."""
    simulation_id: str = ""
    ped_id_list: List[str] = field(default_factory=list)

    def __init__(self, data: dict = None, simulation_id: str = "", ped_id_list: List[str] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.ped_id_list = ped_id_list if ped_id_list is not None else []


@dataclass
class GetPedBaseInfoRes:
    """Response for getting pedestrian base information."""
    base_info_dict: Dict[str, ObjBaseInfo] = field(default_factory=dict)

    def __init__(self, data: dict = None, base_info_dict: Dict[str, ObjBaseInfo] = None):
        if data is not None:
            base_info_dict = data.pop("base_info_dict", {})
            for key, value in data.items():
                setattr(self, key, value)
            self.base_info_dict = {k: ObjBaseInfo(v) for k, v in base_info_dict.items()}
            return
        self.base_info_dict = base_info_dict if base_info_dict is not None else {}


@dataclass
class SetPedPositionReq:
    """Request for setting pedestrian position."""
    simulation_id: str = ""
    ped_id: str = ""
    point: Optional[Point] = None
    phi: Optional[float] = None

    def __init__(self, data: dict = None, simulation_id: str = "", ped_id: str = "", point: Optional[Point] = None, phi: Optional[float] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.ped_id = ped_id
        self.point = point
        self.phi = phi


@dataclass
class SetPedPositionRes:
    """Response for setting pedestrian position."""
    pass


@dataclass
class GetNMVIdListReq:
    """Request for getting non-motor vehicle ID list."""
    simulation_id: str = ""  # 仿真ID

    def __init__(self, data: dict = None, simulation_id: str = ""):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id


@dataclass
class GetNMVIdListRes:
    """Response for getting non-motor vehicle ID list."""
    list: List[str] = field(default_factory=list)  # 非机动车ID列表

    def __init__(self, data: dict = None, list: List[str] = None):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
            return
        self.list = list if list is not None else []


@dataclass
class GetNMVBaseInfoReq:
    """Request for getting non-motor vehicle base information."""
    simulation_id: str = ""
    nmv_id_list: List[str] = field(default_factory=list)

    def __init__(self, data: dict = None, simulation_id: str = "", nmv_id_list: List[str] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.nmv_id_list = nmv_id_list if nmv_id_list is not None else []


@dataclass
class GetNMVBaseInfoRes:
    """Response for getting non-motor vehicle base information."""
    base_info_dict: Dict[str, ObjBaseInfo] = field(default_factory=dict)

    def __init__(self, data: dict = None, base_info_dict: Dict[str, ObjBaseInfo] = None):
        if data is not None:
            base_info_dict = data.pop("base_info_dict", {})
            for key, value in data.items():
                setattr(self, key, value)
            self.base_info_dict = {k: ObjBaseInfo(v) for k, v in base_info_dict.items()}
            return
        self.base_info_dict = base_info_dict if base_info_dict is not None else {}


@dataclass
class SetNMVPositionReq:
    """Request for setting non-motor vehicle position."""
    simulation_id: str = ""
    nmv_id: str = ""
    point: Optional[Point] = None
    phi: Optional[float] = None

    def __init__(self, data: dict = None, simulation_id: str = "", nmv_id: str = "", point: Optional[Point] = None, phi: Optional[float] = None):
        if data is not None:
            self.__dict__.update(data)
            return
        self.simulation_id = simulation_id
        self.nmv_id = nmv_id
        self.point = point
        self.phi = phi


@dataclass
class SetNMVPositionRes:
    """Response for setting non-motor vehicle position."""
    pass
