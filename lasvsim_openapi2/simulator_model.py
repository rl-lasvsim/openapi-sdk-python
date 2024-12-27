from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class InitReq:
    scen_id: str = ""
    scen_ver: str = ""
    sim_record_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class InitRes:
    simulation_id: str = ""
    simulation_addr: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class StopReq:
    simulation_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class StopRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class StepReq:
    simulation_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class StepRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class ResetReq:
    simulation_id: str = ""
    reset_traffic_flow: bool = False

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class ResetRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetCurrentStageReq:
    simulation_id: str = ""
    junction_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetCurrentStageRes:
    movement_ids: List[str] = None
    countdown: int = 0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetMovementSignalReq:
    simulation_id: str = ""
    movement_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetMovementSignalRes:
    current_signal: int = 0
    countdown: int = 0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetSignalPlanReq:
    simulation_id: str = ""
    junction_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetSignalPlanRes:
    junction_id: str = ""
    cycle: int = 0
    offset: int = 0
    stages: List['GetSignalPlanRes_Stage'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetSignalPlanRes_Stage:
    movement_ids: List[str] = None
    duration: int = 0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetMovementListReq:
    simulation_id: str = ""
    junction_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetMovementListRes:
    list: List['Movement'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class NextStageReq:
    simulation_id: str = ""
    junction_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class NextStageRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleIdListReq:
    simulation_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleIdListRes:
    list: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetTestVehicleIdListReq:
    simulation_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetTestVehicleIdListRes:
    list: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleBaseInfoReq:
    simulation_id: str = ""
    id_list: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleBaseInfoRes:
    info_dict: Dict[str, 'GetVehicleBaseInfoRes_VehicleBaseInfo'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleBaseInfoRes_VehicleBaseInfo:
    base_info: Optional['ObjBaseInfo'] = None
    dynamic_info: Optional['DynamicInfo'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class ObjBaseInfo:
    width: float = 0.0
    height: float = 0.0
    length: float = 0.0
    weight: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class DynamicInfo:
    front_wheel_stiffness: float = 0.0
    rear_wheel_stiffness: float = 0.0
    front_axle_to_center: float = 0.0
    rear_axle_to_center: float = 0.0
    yaw_moment_of_inertia: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class Position:
    point: Optional['Point'] = None
    phi: float = 0.0
    lane_id: str = ""
    link_id: str = ""
    junction_id: str = ""
    segment_id: str = ""
    dis_to_lane_end: Optional[float] = None
    position_type: int = 0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class ObjMovingInfo:
    u: float = 0.0
    u_acc: float = 0.0
    v: float = 0.0
    v_acc: float = 0.0
    w: float = 0.0
    w_acc: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class ControlInfo:
    ste_wheel: float = 0.0
    lon_acc: float = 0.0
    fl_torque: float = 0.0
    fr_torque: float = 0.0
    rl_torque: float = 0.0
    rr_torque: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class ReferenceLine:
    lane_ids: List[str] = None
    lane_types: List[str] = None
    points: List[Point] = None
    lane_idxes: List[int] = None
    opposite: bool = False

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class NavigationInfo:
    link_nav: List[str] = None
    destination: Optional[Position] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class Movement:
    map_id: int = 0
    movement_id: str = ""
    upstream_link_id: str = ""
    downstream_link_id: str = ""
    junction_id: str = ""
    flow_direction: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class LaneNav:
    nav: Dict[int, str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehiclePositionReq:
    simulation_id: str = ""
    id_list: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehiclePositionRes:
    position_dict: Dict[str, Position] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleMovingInfoReq:
    simulation_id: str = ""
    id_list: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleMovingInfoRes:
    moving_info_dict: Dict[str, ObjMovingInfo] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleControlInfoReq:
    simulation_id: str = ""
    id_list: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleControlInfoRes:
    control_info_dict: Dict[str, ControlInfo] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehiclePerceptionInfoReq:
    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehiclePerceptionInfoRes:
    list: List['GetVehiclePerceptionInfoRes_PerceptionObj'] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehiclePerceptionInfoRes_PerceptionObj:
    obj_id: str = ""
    base_info: Optional[ObjBaseInfo] = None
    moving_info: Optional[ObjMovingInfo] = None
    position: Optional[Position] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleReferenceLinesReq:
    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleReferenceLinesRes:
    reference_lines: List[ReferenceLine] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehiclePlanningInfoReq:
    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehiclePlanningInfoRes:
    planning_path: List[Point] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleNavigationInfoReq:
    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleNavigationInfoRes:
    navigation_info: Optional[NavigationInfo] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleCollisionStatusReq:
    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleCollisionStatusRes:
    collision_status: bool = False

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleTargetSpeedReq:
    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetVehicleTargetSpeedRes:
    target_speed: float = 0.0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class SetVehiclePlanningInfoReq:
    simulation_id: str = ""
    vehicle_id: str = ""
    planning_path: List[Point] = None

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
class SetVehicleControlInfoReq:
    simulation_id: str = ""
    vehicle_id: str = ""
    ste_wheel: Optional[float] = None
    lon_acc: Optional[float] = None

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
class SetVehiclePositionReq:
    simulation_id: str = ""
    vehicle_id: str = ""
    point: Optional[Point] = None
    phi: Optional[float] = None

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
class SetVehicleMovingInfoReq:
    simulation_id: str = ""
    vehicle_id: str = ""
    u: Optional[float] = None
    v: Optional[float] = None
    w: Optional[float] = None
    u_acc: Optional[float] = None
    v_acc: Optional[float] = None
    w_acc: Optional[float] = None

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
class SetVehicleBaseInfoReq:
    simulation_id: str = ""
    vehicle_id: str = ""
    base_info: Optional[ObjBaseInfo] = None
    dynamic_info: Optional[DynamicInfo] = None

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
class SetVehicleRouteNavReq:
    simulation_id: str = ""
    vehicle_id: str = ""
    route_nav: List[str] = None

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
class SetVehicleLinkNavReq:
    simulation_id: str = ""
    vehicle_id: str = ""
    link_nav: List[str] = None

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
class SetVehicleLaneNavReq:
    simulation_id: str = ""
    vehicle_id: str = ""
    lane_nav: List[LaneNav] = None

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
class SetVehicleDestinationReq:
    simulation_id: str = ""
    vehicle_id: str = ""
    destination: Optional[Point] = None

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
class GetPedIdListReq:
    simulation_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetPedIdListRes:
    list: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetPedBaseInfoReq:
    simulation_id: str = ""
    ped_id_list: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetPedBaseInfoRes:
    base_info_dict: Dict[str, ObjBaseInfo] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class SetPedPositionReq:
    simulation_id: str = ""
    ped_id: str = ""
    point: Optional[Point] = None
    phi: Optional[float] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class SetPedPositionRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetNMVIdListReq:
    simulation_id: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetNMVIdListRes:
    list: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetNMVBaseInfoReq:
    simulation_id: str = ""
    nmv_id_list: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetNMVBaseInfoRes:
    base_info_dict: Dict[str, ObjBaseInfo] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class SetNMVPositionReq:
    simulation_id: str = ""
    nmv_id: str = ""
    point: Optional[Point] = None
    phi: Optional[float] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class SetNMVPositionRes:
    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data
