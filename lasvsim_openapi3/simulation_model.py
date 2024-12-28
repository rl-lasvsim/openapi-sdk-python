from dataclasses import dataclass
from typing import List, Optional, Dict
from .resource_model import Point

@dataclass
class SimulatorConfig:
    scen_id: str
    scen_ver: str
    sim_record_id: str

@dataclass
class InitReq:
    scen_id: str
    scen_ver: str
    sim_record_id: str

@dataclass
class InitRes:
    simulation_id: str
    simulation_addr: str

@dataclass
class StopReq:
    simulation_id: str

@dataclass
class StopRes:
    pass

@dataclass
class StepReq:
    simulation_id: str

@dataclass
class StepRes:
    pass

@dataclass
class ResetReq:
    simulation_id: str
    reset_traffic_flow: bool

@dataclass
class ResetRes:
    pass

@dataclass
class GetCurrentStageReq:
    simulation_id: str
    junction_id: str

@dataclass
class GetCurrentStageRes:
    movement_ids: List[str]
    countdown: int

@dataclass
class GetMovementSignalReq:
    simulation_id: str
    movement_id: str

@dataclass
class GetMovementSignalRes:
    current_signal: int
    countdown: int

@dataclass
class GetSignalPlanReq:
    simulation_id: str
    junction_id: str

@dataclass
class GetSignalPlanRes:
    junction_id: str
    cycle: int
    offset: int
    stages: List[GetSignalPlanRes_Stage]

@dataclass
class GetSignalPlanRes_Stage:
    movement_ids: List[str]
    duration: int

@dataclass
class GetMovementListReq:
    simulation_id: str
    junction_id: str

@dataclass
class GetMovementListRes:
    list: List[Movement]

@dataclass
class NextStageReq:
    simulation_id: str
    junction_id: str

@dataclass
class NextStageRes:
    pass

@dataclass
class GetVehicleIdListReq:
    simulation_id: str

@dataclass
class GetVehicleIdListRes:
    list: List[str]

@dataclass
class GetTestVehicleIdListReq:
    simulation_id: str

@dataclass
class GetTestVehicleIdListRes:
    list: List[str]

@dataclass
class GetVehicleBaseInfoReq:
    simulation_id: str
    id_list: List[str]

@dataclass
class GetVehicleBaseInfoRes:
    info_dict: Dict[str, GetVehicleBaseInfoRes_VehicleBaseInfo]

@dataclass
class GetVehicleBaseInfoRes_VehicleBaseInfo:
    base_info: ObjBaseInfo
    dynamic_info: DynamicInfo

@dataclass
class GetVehiclePositionReq:
    simulation_id: str
    id_list: List[str]

@dataclass
class GetVehiclePositionRes:
    position_dict: Dict[str, Position]

@dataclass
class GetVehicleMovingInfoReq:
    simulation_id: str
    id_list: List[str]

@dataclass
class GetVehicleMovingInfoRes:
    moving_info_dict: Dict[str, ObjMovingInfo]

@dataclass
class GetVehicleControlInfoReq:
    simulation_id: str
    id_list: List[str]

@dataclass
class GetVehicleControlInfoRes:
    control_info_dict: Dict[str, ControlInfo]

@dataclass
class GetVehiclePerceptionInfoReq:
    simulation_id: str
    vehicle_id: str

@dataclass
class GetVehiclePerceptionInfoRes:
    list: List[GetVehiclePerceptionInfoRes_PerceptionObj]

@dataclass
class GetVehiclePerceptionInfoRes_PerceptionObj:
    obj_id: str
    base_info: ObjBaseInfo
    moving_info: ObjMovingInfo
    position: Position

@dataclass
class GetVehicleReferenceLinesReq:
    simulation_id: str
    vehicle_id: str

@dataclass
class GetVehicleReferenceLinesRes:
    reference_lines: List[ReferenceLine]

@dataclass
class GetVehiclePlanningInfoReq:
    simulation_id: str
    vehicle_id: str

@dataclass
class GetVehiclePlanningInfoRes:
    planning_path: List[Point]

@dataclass
class GetVehicleNavigationInfoReq:
    simulation_id: str
    vehicle_id: str

@dataclass
class GetVehicleNavigationInfoRes:
    navigation_info: Optional[NavigationInfo]

@dataclass
class GetVehicleCollisionStatusReq:
    simulation_id: str
    vehicle_id: str

@dataclass
class GetVehicleCollisionStatusRes:
    collision_status: bool

@dataclass
class GetVehicleTargetSpeedReq:
    simulation_id: str
    vehicle_id: str

@dataclass
class GetVehicleTargetSpeedRes:
    target_speed: float

@dataclass
class SetVehiclePlanningInfoReq:
    simulation_id: str
    vehicle_id: str
    planning_path: List[Point]

@dataclass
class SetVehiclePlanningInfoRes:
    pass

@dataclass
class SetVehicleControlInfoReq:
    simulation_id: str
    vehicle_id: str
    ste_wheel: Optional[float]
    lon_acc: Optional[float]

@dataclass
class SetVehicleControlInfoRes:
    pass

@dataclass
class SetVehiclePositionReq:
    simulation_id: str
    vehicle_id: str
    point: Optional[Point]
    phi: Optional[float]

@dataclass
class SetVehiclePositionRes:
    pass

@dataclass
class SetVehicleMovingInfoReq:
    simulation_id: str
    vehicle_id: str
    u: Optional[float]
    v: Optional[float]
    w: Optional[float]
    u_acc: Optional[float]
    v_acc: Optional[float]
    w_acc: Optional[float]

@dataclass
class SetVehicleMovingInfoRes:
    pass

@dataclass
class SetVehicleBaseInfoReq:
    simulation_id: str
    vehicle_id: str
    base_info: Optional[ObjBaseInfo]
    dynamic_info: Optional[DynamicInfo]

@dataclass
class SetVehicleBaseInfoRes:
    pass

@dataclass
class SetVehicleRouteNavReq:
    simulation_id: str
    vehicle_id: str
    route_nav: List[str]

@dataclass
class SetVehicleRouteNavRes:
    pass

@dataclass
class SetVehicleLinkNavReq:
    simulation_id: str
    vehicle_id: str
    link_nav: List[str]

@dataclass
class SetVehicleLinkNavRes:
    pass

@dataclass
class SetVehicleLaneNavReq:
    simulation_id: str
    vehicle_id: str
    lane_nav: List[LaneNav]

@dataclass
class SetVehicleLaneNavRes:
    pass

@dataclass
class SetVehicleDestinationReq:
    simulation_id: str
    vehicle_id: str
    destination: Optional[Point]

@dataclass
class SetVehicleDestinationRes:
    pass

@dataclass
class GetPedIdListReq:
    simulation_id: str

@dataclass
class GetPedIdListRes:
    list: List[str]

@dataclass
class GetPedBaseInfoReq:
    simulation_id: str
    ped_id_list: List[str]

@dataclass
class GetPedBaseInfoRes:
    base_info_dict: Dict[str, ObjBaseInfo]

@dataclass
class SetPedPositionReq:
    simulation_id: str
    ped_id: str
    point: Optional[Point]
    phi: Optional[float]

@dataclass
class SetPedPositionRes:
    pass

@dataclass
class GetNMVIdListReq:
    simulation_id: str

@dataclass
class GetNMVIdListRes:
    list: List[str]

@dataclass
class GetNMVBaseInfoReq:
    simulation_id: str
    nmv_id_list: List[str]

@dataclass
class GetNMVBaseInfoRes:
    base_info_dict: Dict[str, ObjBaseInfo]

@dataclass
class SetNMVPositionReq:
    simulation_id: str
    nmv_id: str
    point: Optional[Point]
    phi: Optional[float]

@dataclass
class SetNMVPositionRes:
    pass

@dataclass
class ObjBaseInfo:
    width: float
    height: float
    length: float
    weight: float

@dataclass
class DynamicInfo:
    front_wheel_stiffness: float
    rear_wheel_stiffness: float
    front_axle_to_center: float
    rear_axle_to_center: float
    yaw_moment_of_inertia: float

@dataclass
class Position:
    point: Optional[Point]
    phi: float
    lane_id: str
    link_id: str
    junction_id: str
    segment_id: str
    dis_to_lane_end: Optional[float]
    position_type: int

@dataclass
class ObjMovingInfo:
    u: float
    u_acc: float
    v: float
    v_acc: float
    w: float
    w_acc: float

@dataclass
class ControlInfo:
    ste_wheel: float
    lon_acc: float
    fl_torque: float
    fr_torque: float
    rl_torque: float
    rr_torque: float

@dataclass
class ReferenceLine:
    lane_ids: List[str]
    lane_types: List[str]
    points: List[Point]
    lane_idxes: List[int]
    opposite: bool

@dataclass
class NavigationInfo:
    link_nav: List[str]
    destination: Optional[Position]

@dataclass
class Movement:
    map_id: int
    movement_id: str
    upstream_link_id: str
    downstream_link_id: str
    junction_id: str
    flow_direction: str

@dataclass
class LaneNav:
    nav: Dict[int, str]
