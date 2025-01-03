"""
Simulator module for the lasvsim API.
"""
from typing import Dict, List, Optional
from dataclasses import asdict

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
    GetStepSpawnIdListReq,
    GetStepSpawnIdListRes,
    GetParticipantBaseInfoReq,
    GetParticipantBaseInfoRes,
    GetParticipantMovingInfoReq,
    GetParticipantMovingInfoRes,
    GetParticipantPositionReq,
    GetParticipantPositionRes,
    NextStageReq,
    NextStageRes,
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
        reply = self.http_client.post(
            "/openapi/cosim/v2/simulation/init",
            {"scen_id": sim_config.scen_id, "scen_ver": sim_config.scen_ver, "sim_record_id": sim_config.sim_record_id},
            InitRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/step",
            {"simulation_id": self.simulation_id},
            StepRes
        )

    def stop(self) -> StopRes:
        """Stop the simulation.
        
        Returns:
            Stop response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/stop",
            {"simulation_id": self.simulation_id},
            StopRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/stage/get",
            {"simulation_id": self.simulation_id, "junction_id": junction_id},
            GetCurrentStageRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/movement/signal/get",
            {"simulation_id": self.simulation_id, "movement_id": movement_id},
            GetMovementSignalRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/signal_plan/get",
            {"simulation_id": self.simulation_id, "junction_id": junction_id},
            GetSignalPlanRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/movement/list/get",
            {"simulation_id": self.simulation_id, "junction_id": junction_id},
            GetMovementListRes
        )

    # --------- 车辆部分 ---------
    def get_vehicle_id_list(self) -> GetVehicleIdListRes:
        """Get vehicle ID list.
        
        Returns:
            Vehicle ID list response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/id_list/get",
            {"simulation_id": self.simulation_id},
            GetVehicleIdListRes
        )

    def get_test_vehicle_id_list(self) -> GetTestVehicleIdListRes:
        """Get test vehicle ID list.
        
        Returns:
            Test vehicle ID list response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/test_vehicle/id_list/get",
            {"simulation_id": self.simulation_id},
            GetTestVehicleIdListRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/base_info/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
            GetVehicleBaseInfoRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/position/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
            GetVehiclePositionRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/moving_info/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
            GetVehicleMovingInfoRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/control/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
            GetVehicleControlInfoRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/perception/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
            GetVehiclePerceptionInfoRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/reference_line/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
            GetVehicleReferenceLinesRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/planning/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
            GetVehiclePlanningInfoRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/navigation/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
            GetVehicleNavigationInfoRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/collision/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
            GetVehicleCollisionStatusRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/target_speed/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
            GetVehicleTargetSpeedRes
        )

    def set_vehicle_control_info(
        self,
        vehicle_id: str,
        ste_wheel: Optional[float] = None,
        lon_acc: Optional[float] = None
    ) -> SetVehicleControlInfoRes:
        """Set vehicle control information.
        
        Args:
            vehicle_id: Vehicle ID
            ste_wheel: Optional steering wheel angle
            lon_acc: Optional longitudinal acceleration
            
        Returns:
            Set vehicle control information response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/control/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "ste_wheel": ste_wheel,
                "lon_acc": lon_acc
            },
            SetVehicleControlInfoRes
        )

    def set_vehicle_moving_info(
        self,
        vehicle_id: str,
        u: Optional[float] = None,
        v: Optional[float] = None,
        w: Optional[float] = None,
        u_acc: Optional[float] = None,
        v_acc: Optional[float] = None,
        w_acc: Optional[float] = None
    ) -> SetVehicleMovingInfoRes:
        """Set vehicle moving information.
        
        Args:
            vehicle_id: Vehicle ID
            u: Optional longitudinal velocity
            v: Optional lateral velocity
            w: Optional yaw rate
            u_acc: Optional longitudinal acceleration
            v_acc: Optional lateral acceleration
            w_acc: Optional yaw acceleration
            
        Returns:
            Set vehicle moving information response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/moving_info/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "u": u,
                "v": v,
                "w": w,
                "u_acc": u_acc,
                "v_acc": v_acc,
                "w_acc": w_acc
            },
            SetVehicleMovingInfoRes
        )

    def set_vehicle_base_info(
        self,
        vehicle_id: str,
        base_info: Optional[ObjBaseInfo] = None,
        dynamic_info: Optional[DynamicInfo] = None
    ) -> SetVehicleBaseInfoRes:
        """Set vehicle base information.
        
        Args:
            vehicle_id: Vehicle ID
            base_info: Optional base information
            dynamic_info: Optional dynamic information
            
        Returns:
            Set vehicle base information response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/base_info/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "base_info": base_info,
                "dynamic_info": dynamic_info
            },
            SetVehicleBaseInfoRes
        )

    def set_vehicle_planning_info(
        self,
        vehicle_id: str,
        planning_path: List[Point]
    ) -> SetVehiclePlanningInfoRes:
        """Set vehicle planning information.
        
        Args:
            vehicle_id: Vehicle ID
            planning_path: List of planning path points
            
        Returns:
            Set vehicle planning information response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/planning/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "planning_path": [asdict(p) for p in planning_path]
            },
            SetVehiclePlanningInfoRes
        )

    def set_vehicle_position(self, vehicle_id: str, point: Point, phi: Optional[float] = None) -> SetVehiclePositionRes:
        """Set vehicle position.
        
        Args:
            vehicle_id: Vehicle ID
            point: Position point with x, y, z coordinates
            phi: Optional heading angle in radians
            
        Returns:
            Set vehicle position response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/position/set",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id, "point": asdict(point), "phi": phi},
            SetVehiclePositionRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/link_nav/set",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id, "link_id_list": link_id_list},
            SetVehicleLinkNavRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/destination/set",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id, "destination": asdict(destination)},
            SetVehicleDestinationRes
        )

    # --------- 行人部分 ---------
    def get_ped_id_list(self) -> GetPedIdListRes:
        """Get pedestrian ID list.
        
        Returns:
            Pedestrian ID list response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/pedestrian/id_list/get",
            {"simulation_id": self.simulation_id},
            GetPedIdListRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/pedestrian/base_info/get",
            {"simulation_id": self.simulation_id, "id_list": ped_id_list},
            GetPedBaseInfoRes
        )

    def set_ped_position(self, ped_id: str, point: Point, phi: Optional[float] = None) -> SetPedPositionRes:
        """Set pedestrian position.
        
        Args:
            ped_id: Pedestrian ID
            point: Position point with x, y, z coordinates
            phi: Optional heading angle in radians
            
        Returns:
            Set pedestrian position response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/pedestrian/position/set",
            {"simulation_id": self.simulation_id, "ped_id": ped_id, "point": asdict(point), "phi": phi},
            SetPedPositionRes
        )

    # --------- 非机动车部分 ---------
    def get_nmv_id_list(self) -> GetNMVIdListRes:
        """Get non-motor vehicle ID list.
        
        Returns:
            Non-motor vehicle ID list response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/non_motor_vehicle/id_list/get",
            {"simulation_id": self.simulation_id},
            GetNMVIdListRes
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
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/non_motor_vehicle/base_info/get",
            {"simulation_id": self.simulation_id, "id_list": nmv_id_list},
            GetNMVBaseInfoRes
        )

    def set_nmv_position(self, nmv_id: str, point: Point, phi: Optional[float] = None) -> SetNMVPositionRes:
        """Set non-motor vehicle position.
        
        Args:
            nmv_id: Non-motor vehicle ID
            point: Position point with x, y, z coordinates
            phi: Optional heading angle in radians
            
        Returns:
            Set non-motor vehicle position response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/non_motor_vehicle/position/set",
            {"simulation_id": self.simulation_id, "nmv_id": nmv_id, "point": asdict(point), "phi": phi},
            SetNMVPositionRes
        )

    def get_step_spawn_id_list(self) -> GetStepSpawnIdListRes:
        """Get step spawn ID list.
        
        Returns:
            Step spawn ID list response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/participant/step_spawn_ids/get",
            {"simulation_id": self.simulation_id},
            GetStepSpawnIdListRes
        )

    def get_participant_base_info(self, participant_id_list: List[str]) -> GetParticipantBaseInfoRes:
        """Get participant base information.
        
        Args:
            participant_id_list: List of participant IDs
            
        Returns:
            Participant base information response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/participant/base_info/get",
            {
                "simulation_id": self.simulation_id,
                "participant_id_list": participant_id_list
            },
            GetParticipantBaseInfoRes
        )

    def get_participant_moving_info(self, participant_id_list: List[str]) -> GetParticipantMovingInfoRes:
        """Get participant moving information.
        
        Args:
            participant_id_list: List of participant IDs
            
        Returns:
            Participant moving information response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/participant/moving_info/get",
            {
                "simulation_id": self.simulation_id,
                "participant_id_list": participant_id_list
            },
            GetParticipantMovingInfoRes
        )

    def get_participant_position(self, participant_id_list: List[str]) -> GetParticipantPositionRes:
        """Get participant position information.
        
        Args:
            participant_id_list: List of participant IDs (maximum 1000 IDs)
            
        Returns:
            Participant position response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/participant/position/get",
            {
                "simulation_id": self.simulation_id,
                "participant_id_list": participant_id_list
            },
            GetParticipantPositionRes
        )

    def next_stage(self, junction_id: str) -> NextStageRes:
        """Move to next stage.
        
        Args:
            junction_id: Junction ID
            
        Returns:
            Next stage response
            
        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/stage/next",
            {
                "simulation_id": self.simulation_id,
                "junction_id": junction_id
            },
            NextStageRes
        )
