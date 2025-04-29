from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.simulator_model import SimulatorConfig
from typing import Dict, List, Optional
from dataclasses import asdict

from lasvsim_openapi.simulator_model import ObjBaseInfo, DynamicInfo, Point


class SimulatorFast:
    """Simulator client for the API."""

    http_client: HttpClient = None
    simulation_id: str = ""

    def __init__(self, http_client: HttpClient, sim_config: SimulatorConfig):
        """Initialize simulator client.

        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client.clone()

        reply = self.http_client.post(
            "/openapi/cosim/v2/simulation/init",
            {
                "scen_id": sim_config.scen_id,
                "scen_ver": sim_config.scen_ver,
                "sim_record_id": sim_config.sim_record_id,
            },
        )

        self.http_client.headers["x-md-simulation_id"] = reply["simulation_id"]
        self.http_client.headers["x-md-rl-direct-addr"] = reply["simulation_addr"]
        self.simulation_id = reply["simulation_id"]

    def step(self):
        """Step the simulation forward.

        Returns:
            dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/step",
            {"simulation_id": self.simulation_id},
        )

    def stop(self) -> dict:
        """Stop the simulation.

        Returns:
            dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/stop",
            {"simulation_id": self.simulation_id},
        )

    def reset(
        self,
        reset_traffic_flow: bool = False,
        reset_vehicle: List = None,
        reset_env_ptcs=None,
    ) -> dict:
        """Reset simulator.

        Args:
            reset_traffic_flow: Whether to reset traffic flow
            reset_vehicle: List of vehicles to reset

        Returns:
            dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/reset",
            {
                "simulation_id": self.simulation_id,
                "reset_traffic_flow": reset_traffic_flow,
                "reset_vehicle": reset_vehicle,
                "reset_env_ptcs": reset_env_ptcs,
            },
        )

    def get_current_stage(self, junction_id: str) -> dict:
        """Get current stage.

        Args:
            junction_id: Junction ID

        Returns:
            Current stage response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/map/traffic_light/current_stage/get",
            {"simulation_id": self.simulation_id, "junction_id": junction_id},
        )

    def get_movement_signal(self, movement_id: str) -> dict:
        """Get movement signal.

        Args:
            movement_id: Movement ID

        Returns:
            Movement signal response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/map/traffic_light/phase_info/get",
            {"simulation_id": self.simulation_id, "movement_id": movement_id},
        )

    def get_signal_plan(self, junction_id: str) -> dict:
        """Get signal plan.

        Args:
            junction_id: Junction ID

        Returns:
            Signal plan response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/map/traffic_light/signal_plan/get",
            {"simulation_id": self.simulation_id, "junction_id": junction_id},
        )

    def get_movement_list(self, junction_id: str) -> dict:
        """Get movement list.

        Args:
            junction_id: Junction ID

        Returns:
            Movement list response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/map/movement/list/get",
            {"simulation_id": self.simulation_id, "junction_id": junction_id},
        )

    def get_vehicle_id_list(self) -> dict:
        """Get vehicle ID list.

        Returns:
            Vehicle ID list response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/id_list/get",
            {"simulation_id": self.simulation_id},
        )

    def get_test_vehicle_id_list(self) -> dict:
        """Get test vehicle ID list.

        Returns:
            Test vehicle ID list response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/test_vehicle/id_list/get",
            {"simulation_id": self.simulation_id},
        )

    def get_vehicle_base_info(self, vehicle_id_list: List[str]) -> dict:
        """Get vehicle base information.

        Args:
            vehicle_id_list: List of vehicle IDs

        Returns:
            Vehicle base information response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/base_info/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
        )

    def get_vehicle_position(self, vehicle_id_list: List[str]) -> dict:
        """Get vehicle position.

        Args:
            vehicle_id_list: List of vehicle IDs

        Returns:
            Vehicle position response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/position/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
        )

    def get_vehicle_moving_info(self, vehicle_id_list: List[str]) -> dict:
        """Get vehicle moving information.

        Args:
            vehicle_id_list: List of vehicle IDs

        Returns:
            Vehicle moving information response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/moving_info/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
        )

    def get_vehicle_control_info(self, vehicle_id_list: List[str]) -> dict:
        """Get vehicle control information.

        Args:
            vehicle_id_list: List of vehicle IDs

        Returns:
            Vehicle control information response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/control/get",
            {"simulation_id": self.simulation_id, "id_list": vehicle_id_list},
        )

    def get_vehicle_perception_info(self, vehicle_id: str) -> dict:
        """Get vehicle perception information.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            Vehicle perception information response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/perception/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )

    def get_vehicle_reference_lines(self, vehicle_id: str) -> dict:
        """Get vehicle reference lines.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            Vehicle reference lines response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/reference_line/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )

    def get_vehicle_dis_to_link_boundary(self, vehicle_id: str) -> dict:
        """获取车辆到车道边界的距离。

        Args:
            vehicle_id: 车辆ID

        Returns:
            包含距离信息的字典

        Raises:
            APIError: 如果请求失败
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/dis_to_link_boundary/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )

    def get_vehicle_planning_info(self, vehicle_id: str) -> dict:
        """Get vehicle planning information.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            Vehicle planning information response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/planning/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )

    def get_vehicle_navigation_info(self, vehicle_id: str) -> dict:
        """Get vehicle navigation information.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            Vehicle navigation information response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/navigation/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )

    def get_vehicle_collision_status(self, vehicle_id: str) -> dict:
        """Get vehicle collision status.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            Vehicle collision status response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/collision/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )

    def get_vehicle_target_speed(self, vehicle_id: str) -> dict:
        """Get vehicle target speed.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            Vehicle target speed response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/target_speed/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )

    def get_vehicle_sensor_config(self, vehicle_id: str) -> dict:
        """Get vehicle sensor configuration.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            Vehicle sensor configuration response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/sensor_config/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )

    def set_vehicle_control_info(
        self,
        vehicle_id: str,
        ste_wheel: Optional[float] = None,
        lon_acc: Optional[float] = None,
    ) -> dict:
        """Set vehicle control information.

        Args:
            vehicle_id: Vehicle ID
            ste_wheel: Optional steering wheel angle
            lon_acc: Optional longitudinal acceleration

        Returns:
            Set vehicle control information response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/control/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "ste_wheel": ste_wheel,
                "lon_acc": lon_acc,
            },
        )

    def set_vehicle_moving_info(
        self,
        vehicle_id: str,
        u: Optional[float] = None,
        v: Optional[float] = None,
        w: Optional[float] = None,
        u_acc: Optional[float] = None,
        v_acc: Optional[float] = None,
        w_acc: Optional[float] = None,
    ) -> dict:
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
            Set vehicle moving information response as dict

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
                "w_acc": w_acc,
            },
        )

    def set_vehicle_base_info(
        self,
        vehicle_id: str,
        base_info: Optional[ObjBaseInfo] = None,
        dynamic_info: Optional[DynamicInfo] = None,
    ) -> dict:
        """Set vehicle base information.

        Args:
            vehicle_id: Vehicle ID
            base_info: Optional base information
            dynamic_info: Optional dynamic information

        Returns:
            Set vehicle base information response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/base_info/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "base_info": asdict(base_info),
                "dynamic_info": asdict(dynamic_info),
            },
        )

    def set_vehicle_planning_info(
        self, vehicle_id: str, planning_path: List[Point], speed: List[float]
    ) -> dict:
        """Set vehicle planning information.

        Args:
            vehicle_id: Vehicle ID
            planning_path: List of planning path points
            speed: List of speeds for each trajectory point

        Returns:
            Vehicle planning info response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/planning/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "planning_path": [asdict(p) for p in planning_path],
                "speed": speed,
            },
        )

    def set_vehicle_position(
        self, vehicle_id: str, point: Point, phi: Optional[float] = None
    ) -> dict:
        """Set vehicle position.

        Args:
            vehicle_id: Vehicle ID
            point: Position point with x, y, z coordinates
            phi: Optional heading angle in radians

        Returns:
            Set vehicle position response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/position/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "point": asdict(point),
                "phi": phi,
            },
        )

    def set_vehicle_link_nav(self, vehicle_id: str, link_id_list: List[str]) -> dict:
        """Set vehicle link navigation.

        Args:
            vehicle_id: Vehicle ID
            link_id_list: List of link IDs

        Returns:
            Set vehicle link navigation response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/link_nav/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "link_id_list": link_id_list,
            },
        )

    def set_vehicle_destination(self, vehicle_id: str, destination: Point) -> dict:
        """Set vehicle destination.

        Args:
            vehicle_id: Vehicle ID
            destination: Destination point

        Returns:
            Set vehicle destination response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/destination/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "destination": asdict(destination),
            },
        )

    def get_ped_id_list(self) -> dict:
        """Get pedestrian ID list.

        Returns:
            Pedestrian ID list response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/ped/id_list/get",
            {"simulation_id": self.simulation_id},
        )

    def get_ped_base_info(self, ped_id_list: List[str]) -> dict:
        """Get pedestrian base information.

        Args:
            ped_id_list: List of pedestrian IDs

        Returns:
            Pedestrian base information response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/ped/base_info/get",
            {"simulation_id": self.simulation_id, "id_list": ped_id_list},
        )

    def set_ped_position(
        self, ped_id: str, point: Point, phi: Optional[float] = None
    ) -> dict:
        """Set pedestrian position.

        Args:
            ped_id: Pedestrian ID
            point: Position point with x, y, z coordinates
            phi: Optional heading angle in radians

        Returns:
            Set pedestrian position response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/ped/position/set",
            {
                "simulation_id": self.simulation_id,
                "ped_id": ped_id,
                "point": asdict(point),
                "phi": phi,
            },
        )

    # --------- 非机动车部分 ---------
    def get_nmv_id_list(self) -> dict:
        """Get non-motor vehicle ID list.

        Returns:
            Non-motor vehicle ID list response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/nmv/id_list/get",
            {"simulation_id": self.simulation_id},
        )

    def get_nmv_base_info(self, nmv_id_list: List[str]) -> dict:
        """Get non-motor vehicle base information.

        Args:
            nmv_id_list: List of non-motor vehicle IDs

        Returns:
            Non-motor vehicle base information response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/nmv/base_info/get",
            {"simulation_id": self.simulation_id, "id_list": nmv_id_list},
        )

    def set_nmv_position(
        self, nmv_id: str, point: Point, phi: Optional[float] = None
    ) -> dict:
        """Set non-motor vehicle position.

        Args:
            nmv_id: Non-motor vehicle ID
            point: Position point with x, y, z coordinates
            phi: Optional heading angle in radians

        Returns:
            Set non-motor vehicle position response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/nmv/position/set",
            {
                "simulation_id": self.simulation_id,
                "nmv_id": nmv_id,
                "point": asdict(point),
                "phi": phi,
            },
        )

    def get_step_spawn_id_list(self) -> dict:
        """Get step spawn ID list.

        Returns:
            Step spawn ID list response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/participant/step_spawn_ids/get",
            {"simulation_id": self.simulation_id},
        )

    def get_participant_base_info(self, participant_id_list: List[str]) -> dict:
        """Get participant base information.

        Args:
            participant_id_list: List of participant IDs

        Returns:
            Participant base information response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/participant/base_info/get",
            {
                "simulation_id": self.simulation_id,
                "participant_id_list": participant_id_list,
            },
        )

    def get_participant_moving_info(self, participant_id_list: List[str]) -> dict:
        """Get participant moving information.

        Args:
            participant_id_list: List of participant IDs

        Returns:
            Participant moving information response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/participant/moving_info/get",
            {
                "simulation_id": self.simulation_id,
                "participant_id_list": participant_id_list,
            },
        )

    def get_participant_position(self, participant_id_list: List[str]) -> dict:
        """Get participant position information.

        Args:
            participant_id_list: List of participant IDs (maximum 1000 IDs)

        Returns:
            Participant position response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/participant/position/get",
            {
                "simulation_id": self.simulation_id,
                "participant_id_list": participant_id_list,
            },
        )

    def next_stage(self, junction_id: str) -> dict:
        """Move to next stage.

        Args:
            junction_id: Junction ID

        Returns:
            dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/stage/next",
            {"simulation_id": self.simulation_id, "junction_id": junction_id},
        )

    def set_vehicle_road_perception_info(
        self,
        vehicle_id: str,
        noa: Optional[Dict] = None,
    ) -> dict:
        """Set vehicle road perception information.

        Args:
            vehicle_id: Vehicle ID
            noa: Navigation oriented annotation data

        Returns:
            Response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/road_perception/set",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id, "noa": noa},
        )

    def set_vehicle_obstacle_perception_info(
        self,
        vehicle_id: str,
        obstacles: Optional[List[Dict]] = None,
    ) -> dict:
        """Set vehicle obstacle perception information.

        Args:
            vehicle_id: Vehicle ID
            obstacles: List of obstacle data

        Returns:
            Response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/obstacle_perception/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "obstacles": obstacles,
            },
        )

    def set_vehicle_extra_metrics(
        self,
        vehicle_id: str,
        metrics: Optional[Dict[str, float]] = None,
    ) -> dict:
        """Set vehicle extra metrics.

        Args:
            vehicle_id: Vehicle ID
            metrics: Dictionary of metric names and values

        Returns:
            Response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/extra_metrics/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "metrics": metrics,
            },
        )

    def set_vehicle_local_paths(
        self,
        vehicle_id: str,
        local_paths: Optional[List[Dict]] = None,
        choose_idx: Optional[int] = None,
    ) -> dict:
        """Set vehicle local paths.

        Args:
            vehicle_id: Vehicle ID
            local_paths: List of local path data
            choose_idx: Index of selected path

        Returns:
            Response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/local_paths/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "local_paths": local_paths,
                "choose_idx": choose_idx,
            },
        )

    def get_idc_vehicle_nav(
        self,
        vehicle_id: str,
    ) -> dict:
        """Get IDC vehicle navigation information.

        Args:
            vehicle_id: Vehicle ID

        Returns:
            Response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/vehicle/idc_vehicle_nav/get",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
            },
        )

    def idc_step(
        self,
        vehicle_id: str,
        ste_wheel: Optional[float] = None,
        lon_acc: Optional[float] = None,
        ref_limit: Optional[float] = None,
    ) -> dict:
        """Perform IDC step.

        Args:
            vehicle_id: Vehicle ID
            ste_wheel: Steering wheel angle
            lon_acc: Longitudinal acceleration
            ref_limit: Reference limit

        Returns:
            Response as dict

        Raises:
            APIError: If the request fails
        """
        return self.http_client.post(
            "/openapi/cosim/v2/simulation/idc_step",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "ste_wheel": ste_wheel,
                "lon_acc": lon_acc,
                "ref_limit": ref_limit,
            },
        )
