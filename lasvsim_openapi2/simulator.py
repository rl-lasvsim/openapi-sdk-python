from typing import Optional, List
from lasvsim_openapi2.http_client import HttpClient
from lasvsim_openapi2.simulator_model import (
    SimulatorConfig,
    StepRes, StepReq,
    StopRes, StopReq,
    ResetRes, ResetReq,
    GetCurrentStageRes, GetCurrentStageReq,
    GetMovementSignalRes, GetMovementSignalReq,
    GetSignalPlanRes, GetSignalPlanReq,
    GetMovementListRes, GetMovementListReq,
    GetVehicleIdListRes, GetVehicleIdListReq,
    GetTestVehicleIdListRes, GetTestVehicleIdListReq,
    GetVehicleBaseInfoRes, GetVehicleBaseInfoReq,
    GetVehiclePositionRes, GetVehiclePositionReq,
    GetVehicleMovingInfoRes, GetVehicleMovingInfoReq,
    GetVehicleControlInfoRes, GetVehicleControlInfoReq,
    GetVehiclePerceptionInfoRes, GetVehiclePerceptionInfoReq,
    GetVehicleReferenceLinesRes, GetVehicleReferenceLinesReq,
    GetVehiclePlanningInfoRes, GetVehiclePlanningInfoReq,
    GetVehicleNavigationInfoRes, GetVehicleNavigationInfoReq,
    GetVehicleCollisionStatusRes, GetVehicleCollisionStatusReq,
    GetVehicleTargetSpeedRes, GetVehicleTargetSpeedReq,
    SetVehiclePlanningInfoRes, SetVehiclePlanningInfoReq,
    SetVehicleControlInfoRes, SetVehicleControlInfoReq,
    SetVehiclePositionRes, SetVehiclePositionReq,
    SetVehicleMovingInfoRes, SetVehicleMovingInfoReq,
    SetVehicleBaseInfoRes, SetVehicleBaseInfoReq,
    SetVehicleLinkNavRes, SetVehicleLinkNavReq,
    SetVehicleDestinationRes, SetVehicleDestinationReq,
    GetPedIdListRes, GetPedIdListReq,
    GetPedBaseInfoRes, GetPedBaseInfoReq,
    SetPedPositionRes, SetPedPositionReq,
    GetNMVIdListRes, GetNMVIdListReq,
    GetNMVBaseInfoRes, GetNMVBaseInfoReq,
    SetNMVPositionRes, SetNMVPositionReq,
    Point, ObjBaseInfo, DynamicInfo
)

class Simulator:
    http_client: HttpClient = None
    simulation_id: str = None
    def __init__(self, http_client: HttpClient, simulation_id: str = ""):
        self.http_client = http_client
        self.simulation_id = simulation_id

    @classmethod
    def from_config(cls, http_client: HttpClient, config: SimulatorConfig) -> Optional['Simulator']:
        """Initialize simulator from config"""
        response = http_client.post(
            "/openapi/cosim/v2/simulation/init",
            {
                "scen_id": config.scen_id,
                "scen_ver": config.scen_ver,
                "sim_record_id": config.sim_record_id
            }
        )
        http_client.headers["x-md-simulation_id"] = response["simulation_id"]
        http_client.headers["x-md-rl-direct-addr"] = response["simulation_addr"]
        return cls(http_client, response["simulation_id"])

    @classmethod
    def from_sim(cls, http_client: HttpClient, sim_id: str, addr: str) -> Optional['Simulator']:
        """Initialize simulator from existing simulation"""
        try:
            http_client.headers["x-md-simulation_id"] = sim_id
            http_client.headers["x-md-rl-direct-addr"] = addr
            sim = cls(http_client, sim_id)
            return sim
        except Exception as e:
            print(f"Error initializing simulator from existing simulation: {e}")
            return None

    # Core simulation control
    def step(self) -> Optional[StepRes]:
        """Advance simulation by one step"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/step",
                StepReq(simulation_id=self.simulation_id)
            )
            return StepRes(**response)
        except Exception as e:
            print(f"Error stepping simulation: {e}")
            return None

    def stop(self) -> bool:
        """Stop the simulation"""
        try:
            self.http_client.post(
                "/openapi/cosim/v2/simulation/stop",
                StopReq(simulation_id=self.simulation_id)
            )
            return True
        except Exception as e:
            print(f"Error stopping simulation: {e}")
            return False

    def reset(self, reset_traffic_flow: bool) -> Optional[ResetRes]:
        """Reset the simulation"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/reset",
                ResetReq(simulation_id=self.simulation_id, reset_traffic_flow=reset_traffic_flow)
            )
            return ResetRes(**response)
        except Exception as e:
            print(f"Error resetting simulation: {e}")
            return None

    # Map operations
    def get_current_stage(self, junction_id: str) -> Optional[GetCurrentStageRes]:
        """Get current traffic light stage for a junction"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/map/traffic_light/current_stage/get",
                GetCurrentStageReq(simulation_id=self.simulation_id, junction_id=junction_id)
            )
            return GetCurrentStageRes(**response)
        except Exception as e:
            print(f"Error getting current stage: {e}")
            return None

    def get_movement_signal(self, movement_id: str) -> Optional[GetMovementSignalRes]:
        """Get signal info for a movement"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/map/traffic_light/phase_info/get",
                GetMovementSignalReq(simulation_id=self.simulation_id, movement_id=movement_id)
            )
            return GetMovementSignalRes(**response)
        except Exception as e:
            print(f"Error getting movement signal: {e}")
            return None

    def get_signal_plan(self, junction_id: str) -> Optional[GetSignalPlanRes]:
        """Get signal plan for a junction"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/map/traffic_light/signal_plan/get",
                GetSignalPlanReq(simulation_id=self.simulation_id, junction_id=junction_id)
            )
            return GetSignalPlanRes(**response)
        except Exception as e:
            print(f"Error getting signal plan: {e}")
            return None

    def get_movement_list(self, junction_id: str) -> Optional[GetMovementListRes]:
        """Get movement list for a junction"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/map/movement/list/get",
                GetMovementListReq(simulation_id=self.simulation_id, junction_id=junction_id)
            )
            return GetMovementListRes(**response)
        except Exception as e:
            print(f"Error getting movement list: {e}")
            return None

    # Vehicle operations
    def get_vehicle_id_list(self) -> Optional[GetVehicleIdListRes]:
        """Get list of vehicle IDs"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/id_list/get",
                GetVehicleIdListReq(simulation_id=self.simulation_id)
            )
            return GetVehicleIdListRes(**response)
        except Exception as e:
            print(f"Error getting vehicle ID list: {e}")
            return None

    def get_test_vehicle_id_list(self) -> Optional[GetTestVehicleIdListRes]:
        """Get list of test vehicle IDs"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/test_vehicle/id_list/get",
                GetTestVehicleIdListReq(simulation_id=self.simulation_id)
            )
            return GetTestVehicleIdListRes(**response)
        except Exception as e:
            print(f"Error getting test vehicle ID list: {e}")
            return None

    def get_vehicle_base_info(self, vehicle_id_list: List[str]) -> Optional[GetVehicleBaseInfoRes]:
        """Get base info for vehicles"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/base_info/get",
                GetVehicleBaseInfoReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
            )
            return GetVehicleBaseInfoRes(**response)
        except Exception as e:
            print(f"Error getting vehicle base info: {e}")
            return None

    def get_vehicle_position(self, vehicle_id_list: List[str]) -> Optional[GetVehiclePositionRes]:
        """Get positions of vehicles"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/position/get",
                GetVehiclePositionReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
            )
            return GetVehiclePositionRes(**response)
        except Exception as e:
            print(f"Error getting vehicle positions: {e}")
            return None

    def get_vehicle_moving_info(self, vehicle_id_list: List[str]) -> Optional[GetVehicleMovingInfoRes]:
        """Get moving info for vehicles"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/moving_info/get",
                GetVehicleMovingInfoReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
            )
            return GetVehicleMovingInfoRes(**response)
        except Exception as e:
            print(f"Error getting vehicle moving info: {e}")
            return None

    def get_vehicle_control_info(self, vehicle_id_list: List[str]) -> Optional[GetVehicleControlInfoRes]:
        """Get control info for vehicles"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/control/get",
                GetVehicleControlInfoReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
            )
            return GetVehicleControlInfoRes(**response)
        except Exception as e:
            print(f"Error getting vehicle control info: {e}")
            return None

    def get_vehicle_perception_info(self, vehicle_id: str) -> Optional[GetVehiclePerceptionInfoRes]:
        """Get perception info for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/perception/get",
                GetVehiclePerceptionInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id)
            )
            return GetVehiclePerceptionInfoRes(**response)
        except Exception as e:
            print(f"Error getting vehicle perception info: {e}")
            return None

    def get_vehicle_reference_lines(self, vehicle_id: str) -> Optional[GetVehicleReferenceLinesRes]:
        """Get reference lines for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/reference_line/get",
                GetVehicleReferenceLinesReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id)
            )
            return GetVehicleReferenceLinesRes(**response)
        except Exception as e:
            print(f"Error getting vehicle reference lines: {e}")
            return None

    def get_vehicle_planning_info(self, vehicle_id: str) -> Optional[GetVehiclePlanningInfoRes]:
        """Get planning info for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/planning/get",
                GetVehiclePlanningInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id)
            )
            return GetVehiclePlanningInfoRes(**response)
        except Exception as e:
            print(f"Error getting vehicle planning info: {e}")
            return None

    def get_vehicle_navigation_info(self, vehicle_id: str) -> Optional[GetVehicleNavigationInfoRes]:
        """Get navigation info for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/navigation/get",
                GetVehicleNavigationInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id)
            )
            return GetVehicleNavigationInfoRes(**response)
        except Exception as e:
            print(f"Error getting vehicle navigation info: {e}")
            return None

    def get_vehicle_collision_status(self, vehicle_id: str) -> Optional[GetVehicleCollisionStatusRes]:
        """Get collision status for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/collision/get",
                GetVehicleCollisionStatusReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id)
            )
            return GetVehicleCollisionStatusRes(**response)
        except Exception as e:
            print(f"Error getting vehicle collision status: {e}")
            return None

    def get_vehicle_target_speed(self, vehicle_id: str) -> Optional[GetVehicleTargetSpeedRes]:
        """Get target speed for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/target_speed/get",
                GetVehicleTargetSpeedReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id)
            )
            return GetVehicleTargetSpeedRes(**response)
        except Exception as e:
            print(f"Error getting vehicle target speed: {e}")
            return None

    def set_vehicle_planning_info(self, vehicle_id: str, planning_path: List[Point]) -> Optional[SetVehiclePlanningInfoRes]:
        """Set planning info for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/planning/set",
                SetVehiclePlanningInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, planning_path=planning_path)
            )
            return SetVehiclePlanningInfoRes(**response)
        except Exception as e:
            print(f"Error setting vehicle planning info: {e}")
            return None

    def set_vehicle_control_info(self, vehicle_id: str, ste_wheel: Optional[float], lon_acc: Optional[float]) -> Optional[SetVehicleControlInfoRes]:
        """Set control info for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/control/set",
                SetVehicleControlInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, ste_wheel=ste_wheel, lon_acc=lon_acc)
            )
            return SetVehicleControlInfoRes(**response)
        except Exception as e:
            print(f"Error setting vehicle control info: {e}")
            return None

    def set_vehicle_position(self, vehicle_id: str, point: Point, phi: Optional[float]) -> Optional[SetVehiclePositionRes]:
        """Set position for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/position/set",
                SetVehiclePositionReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, point=point, phi=phi)
            )
            return SetVehiclePositionRes(**response)
        except Exception as e:
            print(f"Error setting vehicle position: {e}")
            return None

    def set_vehicle_moving_info(self, vehicle_id: str, u: Optional[float], v: Optional[float], w: Optional[float],
                              u_acc: Optional[float], v_acc: Optional[float], w_acc: Optional[float]) -> Optional[SetVehicleMovingInfoRes]:
        """Set moving info for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/moving_info/set",
                SetVehicleMovingInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id,
                                      u=u, v=v, w=w, u_acc=u_acc, v_acc=v_acc, w_acc=w_acc)
            )
            return SetVehicleMovingInfoRes(**response)
        except Exception as e:
            print(f"Error setting vehicle moving info: {e}")
            return None

    def set_vehicle_base_info(self, vehicle_id: str, base_info: ObjBaseInfo, dynamic_info: DynamicInfo) -> Optional[SetVehicleBaseInfoRes]:
        """Set base info for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/base_info/set",
                SetVehicleBaseInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id,
                                    base_info=base_info, dynamic_info=dynamic_info)
            )
            return SetVehicleBaseInfoRes(**response)
        except Exception as e:
            print(f"Error setting vehicle base info: {e}")
            return None

    def set_vehicle_link_nav(self, vehicle_id: str, link_nav: List[str]) -> Optional[SetVehicleLinkNavRes]:
        """Set link navigation for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/link_nav/set",
                SetVehicleLinkNavReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, link_nav=link_nav)
            )
            return SetVehicleLinkNavRes(**response)
        except Exception as e:
            print(f"Error setting vehicle link navigation: {e}")
            return None

    def set_vehicle_destination(self, vehicle_id: str, destination: Point) -> Optional[SetVehicleDestinationRes]:
        """Set destination for a vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/vehicle/destination/set",
                SetVehicleDestinationReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, destination=destination)
            )
            return SetVehicleDestinationRes(**response)
        except Exception as e:
            print(f"Error setting vehicle destination: {e}")
            return None

    # Pedestrian operations
    def get_ped_id_list(self) -> Optional[GetPedIdListRes]:
        """Get list of pedestrian IDs"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/ped/id_list/get",
                GetPedIdListReq(simulation_id=self.simulation_id)
            )
            return GetPedIdListRes(**response)
        except Exception as e:
            print(f"Error getting pedestrian ID list: {e}")
            return None

    def get_ped_base_info(self, ped_id_list: List[str]) -> Optional[GetPedBaseInfoRes]:
        """Get base info for pedestrians"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/ped/base_info/get",
                GetPedBaseInfoReq(simulation_id=self.simulation_id, ped_id_list=ped_id_list)
            )
            return GetPedBaseInfoRes(**response)
        except Exception as e:
            print(f"Error getting pedestrian base info: {e}")
            return None

    def set_ped_position(self, ped_id: str, point: Point, phi: Optional[float]) -> Optional[SetPedPositionRes]:
        """Set position for a pedestrian"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/ped/position/set",
                SetPedPositionReq(simulation_id=self.simulation_id, ped_id=ped_id, point=point, phi=phi)
            )
            return SetPedPositionRes(**response)
        except Exception as e:
            print(f"Error setting pedestrian position: {e}")
            return None

    # Non-motorized vehicle operations
    def get_nmv_id_list(self) -> Optional[GetNMVIdListRes]:
        """Get list of non-motorized vehicle IDs"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/nmv/id_list/get",
                GetNMVIdListReq(simulation_id=self.simulation_id)
            )
            return GetNMVIdListRes(**response)
        except Exception as e:
            print(f"Error getting NMV ID list: {e}")
            return None

    def get_nmv_base_info(self, nmv_id_list: List[str]) -> Optional[GetNMVBaseInfoRes]:
        """Get base info for non-motorized vehicles"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/nmv/base_info/get",
                GetNMVBaseInfoReq(simulation_id=self.simulation_id, nmv_id_list=nmv_id_list)
            )
            return GetNMVBaseInfoRes(**response)
        except Exception as e:
            print(f"Error getting NMV base info: {e}")
            return None

    def set_nmv_position(self, nmv_id: str, point: Point, phi: Optional[float]) -> Optional[SetNMVPositionRes]:
        """Set position for a non-motorized vehicle"""
        try:
            response = self.http_client.post(
                "/openapi/cosim/v2/simulation/nmv/position/set",
                SetNMVPositionReq(simulation_id=self.simulation_id, nmv_id=nmv_id, point=point, phi=phi)
            )
            return SetNMVPositionRes(**response)
        except Exception as e:
            print(f"Error setting NMV position: {e}")
            return None
