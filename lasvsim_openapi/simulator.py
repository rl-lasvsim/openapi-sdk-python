"""
Simulator module for the lasvsim API.
"""

from typing import Dict, List, Optional
from dataclasses import asdict

from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.simulator_fast import SimulatorFast
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
    ResetReq,
    ResetRes,
    GetVehicleSensorConfigReq,
    GetVehicleSensorConfigRes,
    LocalMap,
    SetVehicleRoadPerceptionInfoRes,
    Obstacle,
    SetVehicleObstaclePerceptionInfoRes,
    SetVehicleExtraMetricsRes,
    LocalPath,
    SetVehicleLocalPathsRes,
    GetIdcVehicleNavRes,
    ResetVehicleConfig,
    ResetEnvPtcs,
    IdcStepRes,
)


class Simulator:
    """Simulator client for the API."""

    simulator_fast: SimulatorFast = None

    def __init__(self, simulator_v2: SimulatorFast):
        """Initialize simulator client.

        Args:
            http_client: HTTP client instance
        """
        self.simulator_fast = simulator_v2

    def step(self) -> StepRes:
        """Step the simulation forward.

        Returns:
            Step response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.step()
        return StepRes.from_dict(reply)

    def stop(self) -> StopRes:
        """Stop the simulation.

        Returns:
            Stop response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.stop()
        return StopRes.from_dict(reply)

    def reset(
        self,
        reset_traffic_flow: bool = False,
        reset_vehicle: List = None,
        reset_env_ptcs=None,
    ) -> ResetRes:
        """Reset simulator.

        Args:
            reset_traffic_flow: Whether to reset traffic flow

        Returns:
            Reset response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.reset(
            reset_traffic_flow, reset_vehicle, reset_env_ptcs=reset_env_ptcs
        )
        return ResetRes.from_dict(reply)

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
        reply = self.simulator_fast.get_current_stage(junction_id)
        return GetCurrentStageRes.from_dict(reply)

    def get_movement_signal(self, movement_id: str) -> GetMovementSignalRes:
        """Get movement signal.

        Args:
            movement_id: Movement ID

        Returns:
            Movement signal response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_movement_signal(movement_id)
        return GetMovementSignalRes.from_dict(reply)

    def get_signal_plan(self, junction_id: str) -> GetSignalPlanRes:
        """Get signal plan.

        Args:
            junction_id: Junction ID

        Returns:
            Signal plan response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_signal_plan(junction_id)
        return GetSignalPlanRes.from_dict(reply)

    def get_movement_list(self, junction_id: str) -> GetMovementListRes:
        """Get movement list.

        Args:
            junction_id: Junction ID

        Returns:
            Movement list response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_movement_list(junction_id)
        return GetMovementListRes.from_dict(reply)

    # --------- 车辆部分 ---------
    def get_vehicle_id_list(self) -> GetVehicleIdListRes:
        """Get vehicle ID list.

        Returns:
            Vehicle ID list response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_vehicle_id_list()
        return GetVehicleIdListRes.from_dict(reply)

    def get_test_vehicle_id_list(self) -> GetTestVehicleIdListRes:
        """Get test vehicle ID list.

        Returns:
            Test vehicle ID list response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_test_vehicle_id_list()
        return GetTestVehicleIdListRes.from_dict(reply)

    def get_vehicle_base_info(
        self, vehicle_id_list: List[str]
    ) -> GetVehicleBaseInfoRes:
        """Get vehicle base information.

        Args:
            vehicle_id_list: List of vehicle IDs

        Returns:
            Vehicle base information response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_vehicle_base_info(vehicle_id_list)
        return GetVehicleBaseInfoRes.from_dict(reply)

    def get_vehicle_position(self, vehicle_id_list: List[str]) -> GetVehiclePositionRes:
        """Get vehicle position.

        Args:
            vehicle_id_list: List of vehicle IDs

        Returns:
            Vehicle position response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_vehicle_position(vehicle_id_list)
        return GetVehiclePositionRes.from_dict(reply)

    def get_vehicle_moving_info(
        self, vehicle_id_list: List[str]
    ) -> GetVehicleMovingInfoRes:
        """Get vehicle moving information.

        Args:
            vehicle_id_list: List of vehicle IDs

        Returns:
            Vehicle moving information response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_vehicle_moving_info(vehicle_id_list)
        return GetVehicleMovingInfoRes.from_dict(reply)

    def get_vehicle_control_info(
        self, vehicle_id_list: List[str]
    ) -> GetVehicleControlInfoRes:
        """Get vehicle control information.

        Args:
            vehicle_id_list: List of vehicle IDs

        Returns:
            Vehicle control information response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_vehicle_control_info(vehicle_id_list)
        return GetVehicleControlInfoRes.from_dict(reply)

    def get_vehicle_perception_info(
        self, vehicle_id: str
    ) -> GetVehiclePerceptionInfoRes:
        """Get vehicle perception information.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            GetVehiclePerceptionInfoRes: Vehicle perception information

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_vehicle_perception_info(vehicle_id)
        return GetVehiclePerceptionInfoRes.from_dict(reply)

    def get_vehicle_reference_lines(
        self, vehicle_id: str
    ) -> GetVehicleReferenceLinesRes:
        """Get vehicle reference lines.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            GetVehicleReferenceLinesRes: Vehicle reference lines

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_vehicle_reference_lines(vehicle_id)
        return GetVehicleReferenceLinesRes.from_dict(reply)

    def get_vehicle_dis_to_link_boundary(self, vehicle_id: str):
        return self.simulator_fast.get_vehicle_dis_to_link_boundary(vehicle_id)

    def get_vehicle_planning_info(self, vehicle_id: str) -> GetVehiclePlanningInfoRes:
        """Get vehicle planning information.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            GetVehiclePlanningInfoRes: Vehicle planning information

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_vehicle_planning_info(vehicle_id)
        return GetVehiclePlanningInfoRes.from_dict(reply)

    def get_vehicle_navigation_info(
        self, vehicle_id: str
    ) -> GetVehicleNavigationInfoRes:
        """Get vehicle navigation information.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            GetVehicleNavigationInfoRes: Vehicle navigation information

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_vehicle_navigation_info(vehicle_id)
        return GetVehicleNavigationInfoRes.from_dict(reply)

    def get_vehicle_collision_status(
        self, vehicle_id: str
    ) -> GetVehicleCollisionStatusRes:
        """Get vehicle collision status.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            GetVehicleCollisionStatusRes: Vehicle collision status

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_vehicle_collision_status(vehicle_id)
        return GetVehicleCollisionStatusRes.from_dict(reply)

    def get_vehicle_target_speed(self, vehicle_id: str) -> GetVehicleTargetSpeedRes:
        """Get vehicle target speed.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            GetVehicleTargetSpeedRes: Vehicle target speed

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_vehicle_target_speed(vehicle_id)
        return GetVehicleTargetSpeedRes.from_dict(reply)

    def get_vehicle_sensor_config(self, vehicle_id: str) -> GetVehicleSensorConfigRes:
        """Get vehicle sensor configuration.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            Vehicle sensor configuration response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_vehicle_sensor_config(vehicle_id=vehicle_id)
        return GetVehicleSensorConfigRes.from_dict(reply)

    def set_vehicle_control_info(
        self,
        vehicle_id: str,
        ste_wheel: Optional[float] = None,
        lon_acc: Optional[float] = None,
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
        reply = self.simulator_fast.set_vehicle_control_info(
            vehicle_id=vehicle_id, ste_wheel=ste_wheel, lon_acc=lon_acc
        )
        return SetVehicleControlInfoRes.from_dict(reply)

    def set_vehicle_moving_info(
        self,
        vehicle_id: str,
        u: Optional[float] = None,
        v: Optional[float] = None,
        w: Optional[float] = None,
        u_acc: Optional[float] = None,
        v_acc: Optional[float] = None,
        w_acc: Optional[float] = None,
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
        reply = self.simulator_fast.set_vehicle_moving_info(
            vehicle_id=vehicle_id,
            u=u,
            v=v,
            w=w,
            u_acc=u_acc,
            v_acc=v_acc,
            w_acc=w_acc,
        )
        return SetVehicleMovingInfoRes.from_dict(reply)

    def set_vehicle_base_info(
        self,
        vehicle_id: str,
        base_info: Optional[ObjBaseInfo] = None,
        dynamic_info: Optional[DynamicInfo] = None,
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
        reply = self.simulator_fast.set_vehicle_base_info(
            vehicle_id=vehicle_id, base_info=base_info, dynamic_info=dynamic_info
        )
        return SetVehicleBaseInfoRes.from_dict(reply)

    def set_vehicle_planning_info(
        self, vehicle_id: str, planning_path: List[Point], speed: List[float]
    ) -> SetVehiclePlanningInfoRes:
        """Set vehicle planning information.

        Args:
            vehicle_id: Vehicle ID
            planning_path: List of planning path points
            speed: List of speeds for each trajectory point

        Returns:
            Vehicle planning info response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.set_vehicle_planning_info(
            vehicle_id=vehicle_id, planning_path=planning_path, speed=speed
        )
        return SetVehiclePlanningInfoRes.from_dict(reply)

    def set_vehicle_position(
        self, vehicle_id: str, point: Point, phi: Optional[float] = None
    ) -> SetVehiclePositionRes:
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
        reply = self.simulator_fast.set_vehicle_position(
            vehicle_id=vehicle_id, point=point, phi=phi
        )
        return SetVehiclePositionRes.from_dict(reply)

    def set_vehicle_link_nav(
        self, vehicle_id: str, link_id_list: List[str]
    ) -> SetVehicleLinkNavRes:
        """Set vehicle link navigation.

        Args:
            vehicle_id: Vehicle ID
            link_id_list: List of link IDs

        Returns:
            Set vehicle link navigation response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.set_vehicle_link_nav(
            vehicle_id=vehicle_id, link_id_list=link_id_list
        )
        return SetVehicleLinkNavRes.from_dict(reply)

    def set_vehicle_destination(
        self, vehicle_id: str, destination: Point
    ) -> SetVehicleDestinationRes:
        """Set vehicle destination.

        Args:
            vehicle_id: Vehicle ID
            destination: Destination point

        Returns:
            Set vehicle destination response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.set_vehicle_destination(
            vehicle_id=vehicle_id, destination=destination
        )
        return SetVehicleDestinationRes.from_dict(reply)

    # --------- 行人部分 ---------
    def get_ped_id_list(self) -> GetPedIdListRes:
        """Get pedestrian ID list.

        Returns:
            Pedestrian ID list response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_ped_id_list()
        return GetPedIdListRes.from_dict(reply)

    def get_ped_base_info(self, ped_id_list: List[str]) -> GetPedBaseInfoRes:
        """Get pedestrian base information.

        Args:
            ped_id_list: List of pedestrian IDs

        Returns:
            Pedestrian base information response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_ped_base_info(ped_id_list)
        return GetPedBaseInfoRes.from_dict(reply)

    def set_ped_position(
        self, ped_id: str, point: Point, phi: Optional[float] = None
    ) -> SetPedPositionRes:
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
        reply = self.simulator_fast.set_ped_position(
            ped_id=ped_id, point=point, phi=phi
        )
        return SetPedPositionRes.from_dict(reply)

    # --------- 非机动车部分 ---------
    def get_nmv_id_list(self) -> GetNMVIdListRes:
        """Get non-motor vehicle ID list.

        Returns:
            Non-motor vehicle ID list response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_nmv_id_list()
        return GetNMVIdListRes.from_dict(reply)

    def get_nmv_base_info(self, nmv_id_list: List[str]) -> GetNMVBaseInfoRes:
        """Get non-motor vehicle base information.

        Args:
            nmv_id_list: List of non-motor vehicle IDs

        Returns:
            Non-motor vehicle base information response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_nmv_base_info(nmv_id_list)
        return GetNMVBaseInfoRes.from_dict(reply)

    def set_nmv_position(
        self, nmv_id: str, point: Point, phi: Optional[float] = None
    ) -> SetNMVPositionRes:
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
        reply = self.simulator_fast.set_nmv_position(
            nmv_id=nmv_id, point=point, phi=phi
        )
        return SetNMVPositionRes.from_dict(reply)

    def get_step_spawn_id_list(self) -> GetStepSpawnIdListRes:
        """Get step spawn ID list.

        Returns:
            Step spawn ID list response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_step_spawn_id_list()
        return GetStepSpawnIdListRes.from_dict(reply)

    def get_participant_base_info(
        self, participant_id_list: List[str]
    ) -> GetParticipantBaseInfoRes:
        """Get participant base information.

        Args:
            participant_id_list: List of participant IDs

        Returns:
            Participant base information response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_participant_base_info(participant_id_list)
        return GetParticipantBaseInfoRes.from_dict(reply)

    def get_participant_moving_info(
        self, participant_id_list: List[str]
    ) -> GetParticipantMovingInfoRes:
        """Get participant moving information.

        Args:
            participant_id_list: List of participant IDs

        Returns:
            Participant moving information response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_participant_moving_info(participant_id_list)
        return GetParticipantMovingInfoRes.from_dict(reply)

    def get_participant_position(
        self, participant_id_list: List[str]
    ) -> GetParticipantPositionRes:
        """Get participant position information.

        Args:
            participant_id_list: List of participant IDs (maximum 1000 IDs)

        Returns:
            Participant position response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.get_participant_position(
            participant_id_list=participant_id_list
        )
        return GetParticipantPositionRes.from_dict(reply)

    def next_stage(self, junction_id: str) -> NextStageRes:
        """Move to next stage.

        Args:
            junction_id: Junction ID

        Returns:
            Next stage response

        Raises:
            APIError: If the request fails
        """
        reply = self.simulator_fast.next_stage(junction_id)
        return NextStageRes.from_dict(reply)

    def set_vehicle_road_perception_info(
        self,
        vehicle_id: str,
        noa: Optional[LocalMap] = None,
    ) -> SetVehicleRoadPerceptionInfoRes:

        reply = self.simulator_fast.set_vehicle_road_perception_info(
            vehicle_id,
            asdict(noa),
        )
        return SetVehicleRoadPerceptionInfoRes.from_dict(reply)

    def set_vehicle_obstacle_perception_info(
        self,
        vehicle_id: str,
        obstacles: List[Obstacle] = None,
    ) -> SetVehicleObstaclePerceptionInfoRes:

        reply = self.simulator_fast.set_vehicle_obstacle_perception_info(
            vehicle_id,
            [asdict(obstacle) for obstacle in obstacles],
        )
        return SetVehicleObstaclePerceptionInfoRes.from_dict(reply)

    def set_vehicle_extra_metrics(
        self,
        vehicle_id: str,
        metrics: Dict[str, str] = None,
    ) -> SetVehicleExtraMetricsRes:

        reply = self.simulator_fast.set_vehicle_extra_metrics(
            vehicle_id,
            metrics,
        )
        return SetVehicleExtraMetricsRes.from_dict(reply)

    def set_vehicle_local_paths(
        self,
        vehicle_id: str,
        local_paths: List[LocalPath] = None,
        choose_idx: Optional[int] = None,
    ) -> SetVehicleLocalPathsRes:

        reply = self.simulator_fast.set_vehicle_local_paths(
            vehicle_id,
            [asdict(local_path) for local_path in local_paths],
            choose_idx,
        )
        return SetVehicleLocalPathsRes.from_dict(reply)

    def get_idc_vehicle_nav(
        self,
        vehicle_id: str,
    ) -> GetIdcVehicleNavRes:

        reply = self.simulator_fast.get_idc_vehicle_nav(
            vehicle_id,
        )
        return GetIdcVehicleNavRes.from_dict(reply)

    def idc_step(
        self,
        vehicle_id: str,
        ste_wheel: Optional[float] = None,
        lon_acc: Optional[float] = None,
        ref_limit: Optional[float] = None,
    ):

        reply = self.simulator_fast.idc_step(
            vehicle_id,
            ste_wheel,
            lon_acc,
            ref_limit,
        )
        return IdcStepRes.from_dict(reply)
