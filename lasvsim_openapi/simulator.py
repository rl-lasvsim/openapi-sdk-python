"""
Simulator module for the lasvsim API.
"""
from typing import Dict, List, Optional

from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.simulator_model import (
    Point,
    ObjBaseInfo,
    DynamicInfo,
    SimulatorConfig,
    InitReq,
    InitRes,
    StopReq,
    StopRes,
    StepReq,
    StepRes,
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
)


class Simulator:
    """Simulator client for the API."""
    http_client: HttpClient = None
    simulation_id: str = ""

    def __init__(self, http_client: HttpClient):
        """Initialize simulator client.
        
        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client.clone()

    @classmethod
    def from_config(cls, http_client: HttpClient, config: SimulatorConfig) -> 'Simulator':
        """Create simulator from configuration.
        
        Args:
            http_client: HTTP client instance
            config: Simulator configuration
            
        Returns:
            A new simulator instance
            
        Raises:
            APIError: If the request fails
        """
        simulator = cls(http_client)
        simulator.init_from_config(config)
        return simulator

    @classmethod
    def from_sim(cls, http_client: HttpClient, sim_id: str, sim_addr: str) -> 'Simulator':
        """Create simulator from existing simulation.
        
        Args:
            http_client: HTTP client instance
            sim_id: Simulation ID
            sim_addr: Simulation address
            
        Returns:
            A new simulator instance
            
        Raises:
            APIError: If the request fails
        """
        simulator = cls(http_client)
        simulator.init_from_sim(sim_id, sim_addr)
        return simulator

    def init_from_config(self, sim_config: SimulatorConfig):
        """Initialize simulator from configuration.
        
        Args:
            sim_config: Simulator configuration
            
        Raises:
            APIError: If the request fails
        """
        req = InitReq(
            scen_id=sim_config.scen_id,
            scen_ver=sim_config.scen_ver,
            sim_record_id=sim_config.sim_record_id
        )
        reply = InitRes()
        
        self.http_client.post(
            "/openapi/cosim/v2/simulation/init",
            {"scen_id": req.scen_id, "scen_ver": req.scen_ver, "sim_record_id": req.sim_record_id},
            reply
        )
        
        self.init_from_sim(reply.simulation_id, reply.simulation_addr)

    def init_from_sim(self, sim_id: str, sim_addr: str):
        """Initialize simulator from existing simulation.
        
        Args:
            sim_id: Simulation ID
            sim_addr: Simulation address
            
        Raises:
            APIError: If the request fails
        """
        self.http_client.headers["x-md-simulation_id"] = sim_id
        self.http_client.headers["x-md-rl-direct-addr"] = sim_addr
        self.simulation_id = sim_id

    def step(self) -> StepRes:
        """Step the simulation forward.
        
        Returns:
            Step response
            
        Raises:
            APIError: If the request fails
        """
        req = StepReq(simulation_id=self.simulation_id)
        reply = StepRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/step",
            {"simulation_id": req.simulation_id},
            reply
        )

    def stop(self) -> StopRes:
        """Stop the simulation.
        
        Returns:
            Stop response
            
        Raises:
            APIError: If the request fails
        """
        req = StopReq(simulation_id=self.simulation_id)
        reply = StopRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/stop",
            {"simulation_id": req.simulation_id},
            reply
        )

    # --------- 地图部分 ---------
    def get_current_stage(self, junction_id: str) -> GetCurrentStageRes:
        """Get current stage.
        
        Args:
            junction_id: Junction ID
            
        Returns:
            Current stage response
            
        Raises:
            APIError: If the request fails
        """
        req = GetCurrentStageReq(simulation_id=self.simulation_id, junction_id=junction_id)
        reply = GetCurrentStageRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/stage/get",
            {"simulation_id": req.simulation_id, "junction_id": req.junction_id},
            reply
        )

    def get_movement_signal(self, movement_id: str) -> GetMovementSignalRes:
        """Get movement signal.
        
        Args:
            movement_id: Movement ID
            
        Returns:
            Movement signal response
            
        Raises:
            APIError: If the request fails
        """
        req = GetMovementSignalReq(simulation_id=self.simulation_id, movement_id=movement_id)
        reply = GetMovementSignalRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/movement/signal/get",
            {"simulation_id": req.simulation_id, "movement_id": req.movement_id},
            reply
        )

    def get_signal_plan(self, junction_id: str) -> GetSignalPlanRes:
        """Get signal plan.
        
        Args:
            junction_id: Junction ID
            
        Returns:
            Signal plan response
            
        Raises:
            APIError: If the request fails
        """
        req = GetSignalPlanReq(simulation_id=self.simulation_id, junction_id=junction_id)
        reply = GetSignalPlanRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/signal_plan/get",
            {"simulation_id": req.simulation_id, "junction_id": req.junction_id},
            reply
        )

    def get_movement_list(self, junction_id: str) -> GetMovementListRes:
        """Get movement list.
        
        Args:
            junction_id: Junction ID
            
        Returns:
            Movement list response
            
        Raises:
            APIError: If the request fails
        """
        req = GetMovementListReq(simulation_id=self.simulation_id, junction_id=junction_id)
        reply = GetMovementListRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/movement/list/get",
            {"simulation_id": req.simulation_id, "junction_id": req.junction_id},
            reply
        )

    # --------- 车辆部分 ---------
    def get_vehicle_id_list(self) -> GetVehicleIdListRes:
        """Get vehicle ID list.
        
        Returns:
            Vehicle ID list response
            
        Raises:
            APIError: If the request fails
        """
        req = GetVehicleIdListReq(simulation_id=self.simulation_id)
        reply = GetVehicleIdListRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/id_list/get",
            {"simulation_id": req.simulation_id},
            reply
        )

    def get_test_vehicle_id_list(self) -> GetTestVehicleIdListRes:
        """Get test vehicle ID list.
        
        Returns:
            Test vehicle ID list response
            
        Raises:
            APIError: If the request fails
        """
        req = GetTestVehicleIdListReq(simulation_id=self.simulation_id)
        reply = GetTestVehicleIdListRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/test_id_list/get",
            {"simulation_id": req.simulation_id},
            reply
        )

    def get_vehicle_base_info(self, vehicle_id_list: List[str]) -> GetVehicleBaseInfoRes:
        """Get vehicle base information.
        
        Args:
            vehicle_id_list: List of vehicle IDs
            
        Returns:
            Vehicle base information response
            
        Raises:
            APIError: If the request fails
        """
        req = GetVehicleBaseInfoReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
        reply = GetVehicleBaseInfoRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/base_info/get",
            {"simulation_id": req.simulation_id, "id_list": req.id_list},
            reply
        )

    def get_vehicle_position(self, vehicle_id_list: List[str]) -> GetVehiclePositionRes:
        """Get vehicle position.
        
        Args:
            vehicle_id_list: List of vehicle IDs
            
        Returns:
            Vehicle position response
            
        Raises:
            APIError: If the request fails
        """
        req = GetVehiclePositionReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
        reply = GetVehiclePositionRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/position/get",
            {"simulation_id": req.simulation_id, "id_list": req.id_list},
            reply
        )

    def get_vehicle_moving_info(self, vehicle_id_list: List[str]) -> GetVehicleMovingInfoRes:
        """Get vehicle moving information.
        
        Args:
            vehicle_id_list: List of vehicle IDs
            
        Returns:
            Vehicle moving information response
            
        Raises:
            APIError: If the request fails
        """
        req = GetVehicleMovingInfoReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
        reply = GetVehicleMovingInfoRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/moving_info/get",
            {"simulation_id": req.simulation_id, "id_list": req.id_list},
            reply
        )

    def get_vehicle_control_info(self, vehicle_id_list: List[str]) -> GetVehicleControlInfoRes:
        """Get vehicle control information.
        
        Args:
            vehicle_id_list: List of vehicle IDs
            
        Returns:
            Vehicle control information response
            
        Raises:
            APIError: If the request fails
        """
        req = GetVehicleControlInfoReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
        reply = GetVehicleControlInfoRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/control_info/get",
            {"simulation_id": req.simulation_id, "id_list": req.id_list},
            reply
        )

    def get_vehicle_perception_info(self, vehicle_id_list: List[str]) -> GetVehiclePerceptionInfoRes:
        """Get vehicle perception information.
        
        Args:
            vehicle_id_list: List of vehicle IDs
            
        Returns:
            Vehicle perception information response
            
        Raises:
            APIError: If the request fails
        """
        req = GetVehiclePerceptionInfoReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
        reply = GetVehiclePerceptionInfoRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/perception_info/get",
            {"simulation_id": req.simulation_id, "id_list": req.id_list},
            reply
        )

    def get_vehicle_reference_lines(self, vehicle_id_list: List[str]) -> GetVehicleReferenceLinesRes:
        """Get vehicle reference lines.
        
        Args:
            vehicle_id_list: List of vehicle IDs
            
        Returns:
            Vehicle reference lines response
            
        Raises:
            APIError: If the request fails
        """
        req = GetVehicleReferenceLinesReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
        reply = GetVehicleReferenceLinesRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/reference_lines/get",
            {"simulation_id": req.simulation_id, "id_list": req.id_list},
            reply
        )

    def get_vehicle_planning_info(self, vehicle_id_list: List[str]) -> GetVehiclePlanningInfoRes:
        """Get vehicle planning information.
        
        Args:
            vehicle_id_list: List of vehicle IDs
            
        Returns:
            Vehicle planning information response
            
        Raises:
            APIError: If the request fails
        """
        req = GetVehiclePlanningInfoReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
        reply = GetVehiclePlanningInfoRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/planning_info/get",
            {"simulation_id": req.simulation_id, "id_list": req.id_list},
            reply
        )

    def get_vehicle_navigation_info(self, vehicle_id_list: List[str]) -> GetVehicleNavigationInfoRes:
        """Get vehicle navigation information.
        
        Args:
            vehicle_id_list: List of vehicle IDs
            
        Returns:
            Vehicle navigation information response
            
        Raises:
            APIError: If the request fails
        """
        req = GetVehicleNavigationInfoReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
        reply = GetVehicleNavigationInfoRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/navigation_info/get",
            {"simulation_id": req.simulation_id, "id_list": req.id_list},
            reply
        )

    def get_vehicle_collision_status(self, vehicle_id_list: List[str]) -> GetVehicleCollisionStatusRes:
        """Get vehicle collision status.
        
        Args:
            vehicle_id_list: List of vehicle IDs
            
        Returns:
            Vehicle collision status response
            
        Raises:
            APIError: If the request fails
        """
        req = GetVehicleCollisionStatusReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
        reply = GetVehicleCollisionStatusRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/collision_status/get",
            {"simulation_id": req.simulation_id, "id_list": req.id_list},
            reply
        )

    def get_vehicle_target_speed(self, vehicle_id_list: List[str]) -> GetVehicleTargetSpeedRes:
        """Get vehicle target speed.
        
        Args:
            vehicle_id_list: List of vehicle IDs
            
        Returns:
            Vehicle target speed response
            
        Raises:
            APIError: If the request fails
        """
        req = GetVehicleTargetSpeedReq(simulation_id=self.simulation_id, id_list=vehicle_id_list)
        reply = GetVehicleTargetSpeedRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/target_speed/get",
            {"simulation_id": req.simulation_id, "id_list": req.id_list},
            reply
        )

    def set_vehicle_planning_info(self, vehicle_id: str, info: Dict) -> SetVehiclePlanningInfoRes:
        """Set vehicle planning information.
        
        Args:
            vehicle_id: Vehicle ID
            info: Planning information dictionary
            
        Returns:
            Set vehicle planning information response
            
        Raises:
            APIError: If the request fails
        """
        req = SetVehiclePlanningInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, info=info)
        reply = SetVehiclePlanningInfoRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/planning_info/set",
            {"simulation_id": req.simulation_id, "vehicle_id": req.vehicle_id, "info": req.info},
            reply
        )

    def set_vehicle_control_info(self, vehicle_id: str, info: Dict) -> SetVehicleControlInfoRes:
        """Set vehicle control information.
        
        Args:
            vehicle_id: Vehicle ID
            info: Control information dictionary
            
        Returns:
            Set vehicle control information response
            
        Raises:
            APIError: If the request fails
        """
        req = SetVehicleControlInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, info=info)
        reply = SetVehicleControlInfoRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/control_info/set",
            {"simulation_id": req.simulation_id, "vehicle_id": req.vehicle_id, "info": req.info},
            reply
        )

    def set_vehicle_position(self, vehicle_id: str, position: Point) -> SetVehiclePositionRes:
        """Set vehicle position.
        
        Args:
            vehicle_id: Vehicle ID
            position: Position point
            
        Returns:
            Set vehicle position response
            
        Raises:
            APIError: If the request fails
        """
        req = SetVehiclePositionReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, position=position)
        reply = SetVehiclePositionRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/position/set",
            {"simulation_id": req.simulation_id, "vehicle_id": req.vehicle_id, "position": req.position},
            reply
        )

    def set_vehicle_moving_info(self, vehicle_id: str, info: DynamicInfo) -> SetVehicleMovingInfoRes:
        """Set vehicle moving information.
        
        Args:
            vehicle_id: Vehicle ID
            info: Dynamic information
            
        Returns:
            Set vehicle moving information response
            
        Raises:
            APIError: If the request fails
        """
        req = SetVehicleMovingInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, info=info)
        reply = SetVehicleMovingInfoRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/moving_info/set",
            {"simulation_id": req.simulation_id, "vehicle_id": req.vehicle_id, "info": req.info},
            reply
        )

    def set_vehicle_base_info(self, vehicle_id: str, info: ObjBaseInfo) -> SetVehicleBaseInfoRes:
        """Set vehicle base information.
        
        Args:
            vehicle_id: Vehicle ID
            info: Base information
            
        Returns:
            Set vehicle base information response
            
        Raises:
            APIError: If the request fails
        """
        req = SetVehicleBaseInfoReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, info=info)
        reply = SetVehicleBaseInfoRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/base_info/set",
            {"simulation_id": req.simulation_id, "vehicle_id": req.vehicle_id, "info": req.info},
            reply
        )

    def set_vehicle_link_nav(self, vehicle_id: str, link_id_list: List[str]) -> SetVehicleLinkNavRes:
        """Set vehicle link navigation.
        
        Args:
            vehicle_id: Vehicle ID
            link_id_list: List of link IDs
            
        Returns:
            Set vehicle link navigation response
            
        Raises:
            APIError: If the request fails
        """
        req = SetVehicleLinkNavReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, link_id_list=link_id_list)
        reply = SetVehicleLinkNavRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/link_nav/set",
            {"simulation_id": req.simulation_id, "vehicle_id": req.vehicle_id, "link_id_list": req.link_id_list},
            reply
        )

    def set_vehicle_destination(self, vehicle_id: str, destination: Point) -> SetVehicleDestinationRes:
        """Set vehicle destination.
        
        Args:
            vehicle_id: Vehicle ID
            destination: Destination point
            
        Returns:
            Set vehicle destination response
            
        Raises:
            APIError: If the request fails
        """
        req = SetVehicleDestinationReq(simulation_id=self.simulation_id, vehicle_id=vehicle_id, destination=destination)
        reply = SetVehicleDestinationRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/destination/set",
            {"simulation_id": req.simulation_id, "vehicle_id": req.vehicle_id, "destination": req.destination},
            reply
        )

    # --------- 行人部分 ---------
    def get_ped_id_list(self) -> GetPedIdListRes:
        """Get pedestrian ID list.
        
        Returns:
            Pedestrian ID list response
            
        Raises:
            APIError: If the request fails
        """
        req = GetPedIdListReq(simulation_id=self.simulation_id)
        reply = GetPedIdListRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/pedestrian/id_list/get",
            {"simulation_id": req.simulation_id},
            reply
        )

    def get_ped_base_info(self, ped_id_list: List[str]) -> GetPedBaseInfoRes:
        """Get pedestrian base information.
        
        Args:
            ped_id_list: List of pedestrian IDs
            
        Returns:
            Pedestrian base information response
            
        Raises:
            APIError: If the request fails
        """
        req = GetPedBaseInfoReq(simulation_id=self.simulation_id, id_list=ped_id_list)
        reply = GetPedBaseInfoRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/pedestrian/base_info/get",
            {"simulation_id": req.simulation_id, "id_list": req.id_list},
            reply
        )

    def set_ped_position(self, ped_id: str, position: Point) -> SetPedPositionRes:
        """Set pedestrian position.
        
        Args:
            ped_id: Pedestrian ID
            position: Position point
            
        Returns:
            Set pedestrian position response
            
        Raises:
            APIError: If the request fails
        """
        req = SetPedPositionReq(simulation_id=self.simulation_id, ped_id=ped_id, position=position)
        reply = SetPedPositionRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/pedestrian/position/set",
            {"simulation_id": req.simulation_id, "ped_id": req.ped_id, "position": req.position},
            reply
        )

    # --------- 非机动车部分 ---------
    def get_nmv_id_list(self) -> GetNMVIdListRes:
        """Get non-motor vehicle ID list.
        
        Returns:
            Non-motor vehicle ID list response
            
        Raises:
            APIError: If the request fails
        """
        req = GetNMVIdListReq(simulation_id=self.simulation_id)
        reply = GetNMVIdListRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/non_motor_vehicle/id_list/get",
            {"simulation_id": req.simulation_id},
            reply
        )

    def get_nmv_base_info(self, nmv_id_list: List[str]) -> GetNMVBaseInfoRes:
        """Get non-motor vehicle base information.
        
        Args:
            nmv_id_list: List of non-motor vehicle IDs
            
        Returns:
            Non-motor vehicle base information response
            
        Raises:
            APIError: If the request fails
        """
        req = GetNMVBaseInfoReq(simulation_id=self.simulation_id, id_list=nmv_id_list)
        reply = GetNMVBaseInfoRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/non_motor_vehicle/base_info/get",
            {"simulation_id": req.simulation_id, "id_list": req.id_list},
            reply
        )

    def set_nmv_position(self, nmv_id: str, position: Point) -> SetNMVPositionRes:
        """Set non-motor vehicle position.
        
        Args:
            nmv_id: Non-motor vehicle ID
            position: Position point
            
        Returns:
            Set non-motor vehicle position response
            
        Raises:
            APIError: If the request fails
        """
        req = SetNMVPositionReq(simulation_id=self.simulation_id, nmv_id=nmv_id, position=position)
        reply = SetNMVPositionRes()
        
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/non_motor_vehicle/position/set",
            {"simulation_id": req.simulation_id, "nmv_id": req.nmv_id, "position": req.position},
            reply
        )
