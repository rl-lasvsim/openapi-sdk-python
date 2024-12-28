from typing import Optional
from .simulation_model import (
    SimulatorConfig,
    InitReq,
    InitRes,
    StopReq,
    StopRes,
    StepReq,
    StepRes,
    ResetReq,
    ResetRes,
    GetCurrentStageReq,
    GetCurrentStageRes,
    GetMovementSignalReq,
    GetMovementSignalRes,
    GetSignalPlanReq,
    GetSignalPlanRes,
    GetMovementListReq,
    GetMovementListRes,
    GetVehicleIdListReq,
    GetVehicleIdListRes,
    GetTestVehicleIdListReq,
    GetTestVehicleIdListRes,
    GetVehicleBaseInfoReq,
    GetVehicleBaseInfoRes,
    GetVehiclePositionReq,
    GetVehiclePositionRes,
    GetVehicleMovingInfoReq,
    GetVehicleMovingInfoRes,
    GetVehicleControlInfoReq,
    GetVehicleControlInfoRes,
    GetVehiclePerceptionInfoReq,
    GetVehiclePerceptionInfoRes,
    GetVehicleReferenceLinesReq,
    GetVehicleReferenceLinesRes,
    GetVehiclePlanningInfoReq,
    GetVehiclePlanningInfoRes,
    GetVehicleNavigationInfoReq,
    GetVehicleNavigationInfoRes,
    GetVehicleCollisionStatusReq,
    GetVehicleCollisionStatusRes,
    GetVehicleTargetSpeedReq,
    GetVehicleTargetSpeedRes,
    SetVehiclePlanningInfoReq,
    SetVehiclePlanningInfoRes,
    SetVehicleControlInfoReq,
    SetVehicleControlInfoRes,
    SetVehiclePositionReq,
    SetVehiclePositionRes,
    SetVehicleMovingInfoReq,
    SetVehicleMovingInfoRes,
    SetVehicleBaseInfoReq,
    SetVehicleBaseInfoRes,
    SetVehicleLinkNavReq,
    SetVehicleLinkNavRes,
    SetVehicleDestinationReq,
    SetVehicleDestinationRes,
    GetPedIdListReq,
    GetPedIdListRes,
    GetPedBaseInfoReq,
    GetPedBaseInfoRes,
    SetPedPositionReq,
    SetPedPositionRes,
    GetNMVIdListReq,
    GetNMVIdListRes,
    GetNMVBaseInfoReq,
    GetNMVBaseInfoRes,
    SetNMVPositionReq,
    SetNMVPositionRes,
    ObjBaseInfo,
    DynamicInfo,
    Position,
    Point,
    ObjMovingInfo,
    ControlInfo,
    ReferenceLine,
    NavigationInfo,
    Movement,
    LaneNav
)
from .httpclient import HttpClient
from .resource_model import Point

class Simulator:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client.clone()
        self.simulation_id = ""

    @classmethod
    def from_config(cls, http_client: HttpClient, config: SimulatorConfig) -> Optional['Simulator']:
        simulator = cls(http_client)
        simulator.init_from_config(config)
        return simulator

    @classmethod
    def from_sim(cls, http_client: HttpClient, sim_id: str, addr: str) -> Optional['Simulator']:
        simulator = cls(http_client)
        simulator.init_from_sim(sim_id, addr)
        return simulator

    def init_from_config(self, config: SimulatorConfig) -> None:
        response = self.http_client.post(
            "/openapi/cosim/v2/simulation/init",
            InitReq(
                scen_id=config.scen_id,
                scen_ver=config.scen_ver,
                sim_record_id=config.sim_record_id
            )
        )
        self.init_from_sim(response.simulation_id, response.simulation_addr)

    def init_from_sim(self, sim_id: str, addr: str) -> None:
        self.http_client.headers["x-md-simulation_id"] = sim_id
        self.http_client.headers["x-md-rl-direct-addr"] = addr
        self.simulation_id = sim_id

    def step(self) -> Optional[StepRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/step",
            StepReq(simulation_id=self.simulation_id)
        )

    def stop(self) -> None:
        self.http_client.post(
            "/openapi/cosim/v2/simulation/stop",
            StopReq(simulation_id=self.simulation_id)
        )

    def reset(self, reset_traffic_flow: bool) -> Optional[ResetRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/reset",
            ResetReq(
                simulation_id=self.simulation_id,
                reset_traffic_flow=reset_traffic_flow
            )
        )

    def get_current_stage(self, junction_id: str) -> Optional[GetCurrentStageRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/map/traffic_light/current_stage/get",
            GetCurrentStageReq(simulation_id=self.simulation_id, junction_id=junction_id)
        )

    def get_movement_signal(self, movement_id: str) -> Optional[GetMovementSignalRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/map/traffic_light/phase_info/get",
            GetMovementSignalReq(simulation_id=self.simulation_id, movement_id=movement_id)
        )

    def get_signal_plan(self, junction_id: str) -> Optional[GetSignalPlanRes]:
         return self.http_client.post(
            "/openapi/cosim/v2/simulation/map/traffic_light/signal_plan/get",
            GetSignalPlanReq(simulation_id=self.simulation_id, junction_id=junction_id)
        )

    def get_movement_list(self, junction_id: str) -> Optional[GetMovementListRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/map/movement/list/get",
            GetMovementListReq(simulation_id=self.simulation_id, junction_id=junction_id)
        )

    def get_vehicle_id_list(self) -> Optional[GetVehicleIdListRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/id_list/get",
            GetVehicleIdListReq(simulation_id=self.simulation_id)
        )

    def get_test_vehicle_id_list(self) -> Optional[GetTestVehicleIdListRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/test_vehicle/id_list/get",
            GetTestVehicleIdListReq(simulation_id=self.simulation_id)
        )

    def get_vehicle_base_info(self, id_list: List[str]) -> Optional[GetVehicleBaseInfoRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/base_info/get",
            GetVehicleBaseInfoReq(simulation_id=self.simulation_id, id_list=id_list)
        )

    def get_vehicle_position(self, id_list: List[str]) -> Optional[GetVehiclePositionRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/position/get",
            GetVehiclePositionReq(simulation_id=self.simulation_id, id_list=id_list)
        )

    def get_vehicle_moving_info(self, id_list: List[str]) -> Optional[GetVehicleMovingInfoRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/moving_info/get",
            GetVehicleMovingInfoReq(simulation_id=self.simulation_id, id_list=id_list)
        )

    def get_vehicle_control_info(self, id_list: List[str]) -> Optional[GetVehicleControlInfoRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/control/get",
            GetVehicleControlInfoReq(simulation_id=self.simulation_id, id_list=id_list)
        )

    def get_vehicle_perception_info(self, vehicle_id: str) -> Optional[GetVehiclePerceptionInfoRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/perception/get",
            GetVehiclePerceptionInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id)
        )

    def get_vehicle_reference_lines(self, vehicle_id: str) -> Optional[GetVehicleReferenceLinesRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/reference_line/get",
            GetVehicleReferenceLinesReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id)
        )

    def get_vehicle_planning_info(self, vehicle_id: str) -> Optional[GetVehiclePlanningInfoRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/planning/get",
            GetVehiclePlanningInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id)
        )

    def get_vehicle_navigation_info(self, vehicle_id: str) -> Optional[GetVehicleNavigationInfoRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/navigation/get",
            GetVehicleNavigationInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id)
        )

    def get_vehicle_collision_status(self, vehicle_id: str) -> Optional[GetVehicleCollisionStatusRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/collision/get",
            GetVehicleCollisionStatusReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id)
        )

    def get_vehicle_target_speed(self, vehicle_id: str) -> Optional[GetVehicleTargetSpeedRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/target_speed/get",
            GetVehicleTargetSpeedReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id)
        )

    def set_vehicle_planning_info(self, vehicle_id: str, planning_path: List[Point]) -> Optional[SetVehiclePlanningInfoRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/planning/set",
            SetVehiclePlanningInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, planning_path=planning_path)
        )

    def set_vehicle_control_info(self, vehicle_id: str, ste_wheel: Optional[float], lon_acc: Optional[float]) -> Optional[SetVehicleControlInfoRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/control/set",
            SetVehicleControlInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, ste_wheel=ste_wheel, lon_acc=lon_acc)
        )

    def set_vehicle_position(self, vehicle_id: str, point: Optional[Point], phi: Optional[float]) -> Optional[SetVehiclePositionRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/position/set",
            SetVehiclePositionReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, point=point, phi=phi)
        )

    def set_vehicle_moving_info(self, vehicle_id: str, u: Optional[float], v: Optional[float], w: Optional[float], u_acc: Optional[float], v_acc: Optional[float], w_acc: Optional[float]) -> Optional[SetVehicleMovingInfoRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/moving_info/set",
             SetVehicleMovingInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, u=u, v=v, w=w, u_acc=u_acc, v_acc=v_acc, w_acc=w_acc)
        )

    def set_vehicle_base_info(self, vehicle_id: str, base_info: Optional['ObjBaseInfo'], dynamic_info: Optional['DynamicInfo']) -> Optional[SetVehicleBaseInfoRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/base_info/set",
            SetVehicleBaseInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, base_info=base_info, dynamic_info=dynamic_info)
        )

    def set_vehicle_link_nav(self, vehicle_id: str, link_nav: List[str]) -> Optional[SetVehicleLinkNavRes]:
         return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/link_nav/set",
            SetVehicleLinkNavReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, link_nav=link_nav)
        )

    def set_vehicle_destination(self, vehicle_id: str, destination: Point) -> Optional[SetVehicleDestinationRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/destination/set",
            SetVehicleDestinationReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, destination=destination)
        )

    def get_ped_id_list(self) -> Optional[GetPedIdListRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/ped/id_list/get",
            GetPedIdListReq(simulation_id=self.simulation_id)
        )

    def get_ped_base_info(self, ped_id_list: List[str]) -> Optional[GetPedBaseInfoRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/ped/base_info/get",
            GetPedBaseInfoReq(simulation_id=self.simulation_id, ped_id_list=ped_id_list)
        )

    def set_ped_position(self, ped_id: str, point: Point, phi: float) -> Optional[SetPedPositionRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/ped/position/set",
            SetPedPositionReq(simulation_id=self.simulation_id, ped_id=ped_id, point=point, phi=phi)
        )

    def get_nmv_id_list(self) -> Optional[GetNMVIdListRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/nmv/id_list/get",
            GetNMVIdListReq(simulation_id=self.simulation_id)
        )

    def get_nmv_base_info(self, nmv_id_list: List[str]) -> Optional[GetNMVBaseInfoRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/nmv/base_info/get",
            GetNMVBaseInfoReq(simulation_id=self.simulation_id, nmv_id_list=nmv_id_list)
        )

    def set_nmv_position(self, nmv_id: str, point: Point, phi: float) -> Optional[SetNMVPositionRes]:
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/nmv/position/set",
            SetNMVPositionReq(simulation_id=self.simulation_id, nmv_id=nmv_id, point=point, phi=phi)
        )
