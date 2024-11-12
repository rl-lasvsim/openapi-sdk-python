from http_client import HttpConfig, HttpClient
from request_struct import Point
from request_struct import ObjBaseInfo
import response_struct


class SimulatorConfig(object):
    def __init__(
        self,
        scenario_id: str = None,
        scenario_version: str = None,
        record_id: int = None,
    ):
        self.scen_id = scenario_id
        self.scen_ver = scenario_version
        self.record_id = record_id


class Simulator(object):
    def __init__(self, http_config: HttpConfig):
        client = HttpClient(http_config, {})
        self.client = client
        # self.simulation_id = res.get("simulation_id")

    def init_from_config(self, sim_config: SimulatorConfig):
        res = self.client.post(
            "/cosim/v2/simulation/init", sim_config.__dict__)
        self.client.headers["simulation_id"] = res.get("simulation_id")
        self.client.headers["rl-direct-addr"] = res.get("simulation_addr")
        self.simulation_id = res.get("simulation_id")

    def init_from_sim(self, simulation_id: str, addr: str):
        self.simulation_id = simulation_id
        self.client.headers["simulation_id"] = simulation_id
        self.client.headers["rl-direct-addr"] = addr

    def step(self) -> response_struct.StepRes:
        resp = self.client.post(
            "/cosim/v2/simulation/step", {"simulation_id": self.simulation_id}
        )
        return response_struct.StepRes(resp)

    # 停止仿真器
    def stop(self) -> response_struct.StopRes:
        resp = self.client.post(
            "/cosim/v2/simulation/stop", {"simulation_id": self.simulation_id}
        )
        return response_struct.StopRes(resp)

    # 重置仿真器
    def reset(self) -> response_struct.ResetRes:
        resp = self.client.post(
            "/cosim/v2/simulation/reset", {"simulation_id": self.simulation_id}
        )
        return response_struct.ResetRes(resp)

    # 根据junction_id获取交通信号灯当前阶段信息
    def get_current_stage(self, junction_id: str) -> response_struct.GetCurrentStageRes:
        resp = self.client.post(
            "/cosim/v2/simulation/map/traffic_light/current_stage/get",
            {"simulation_id": self.simulation_id, "junction_id": junction_id},
        )
        return response_struct.GetCurrentStageRes(resp)

    # 根据movement_id获取流向对应信号灯灯色信息
    def get_movement_signal(
        self, movement_id: str
    ) -> response_struct.GetMovementSignalRes:
        resp = self.client.post(
            "/cosim/v2/simulation/map/traffic_light/phase_info/get",
            {"simulation_id": self.simulation_id, "movement_id": movement_id},
        )
        return response_struct.GetMovementSignalRes(resp)

    # 根据junction_id获取交通信号灯配时方案
    def get_signal_plan(self, junction_id: str) -> response_struct.GetSignalPlanRes:
        resp = self.client.post(
            "/cosim/v2/simulation/map/traffic_light/signal_plan/get",
            {"simulation_id": self.simulation_id, "junction_id": junction_id},
        )
        return response_struct.GetSignalPlanRes(resp)

    # 根据junctionId获取对应movement列表
    def get_movement_list(self, junction_id: str) -> response_struct.GetMovementListRes:
        resp = self.client.post(
            "/cosim/v2/simulation/map/movement/list/get",
            {"simulation_id": self.simulation_id, "junction_id": junction_id},
        )
        return response_struct.GetMovementListRes(resp)

    # junction对应信号灯灯色切换到下个阶段(暂不支持)
    # def next_stage(self, junction_id: str):
    #     return self.client.post(
    #         "/cosim/v2/simulation/map/traffic_light/next_stage",
    #         {"simulation_id": self.simulation_id, "junction_id": junction_id},
    #     )

    # 根据仿真ID获取所有车辆ID列表
    def get_vehicle_id_list(self) -> response_struct.GetVehicleIdListRes:
        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/id_list/get",
            {"simulation_id": self.simulation_id},
        )
        return response_struct.GetVehicleIdListRes(resp)

    # 根据仿真ID获取测试车辆ID列表
    def get_test_vehicle_id_list(self) -> response_struct.GetTestVehicleIdListRes:
        resp = self.client.post(
            "/cosim/v2/simulation/test_vehicle/id_list/get",
            {"simulation_id": self.simulation_id},
        )
        return response_struct.GetTestVehicleIdListRes(resp)

    # 根据车辆ID列表获取车辆基本信息
    def get_vehicle_base_info(
        self, id_list: list[str]
    ) -> response_struct.GetVehicleBaseInfoRes:
        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/base_info/get",
            {"simulation_id": self.simulation_id, "id_list": id_list},
        )
        return response_struct.GetVehicleBaseInfoRes(resp)

    # 根据车辆ID列表获取车辆位置信息
    def get_vehicle_position(
        self, id_list: list[str]
    ) -> response_struct.GetVehiclePositionRes:
        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/position/get",
            {"simulation_id": self.simulation_id, "id_list": id_list},
        )
        return response_struct.GetVehiclePositionRes(resp)

    # 根据车辆ID列表获取车辆运动信息
    def get_vehicle_moving_info(
        self, id_list: list[str]
    ) -> response_struct.GetVehicleMovingInfoRes:
        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/moving_info/get",
            {"simulation_id": self.simulation_id, "id_list": id_list},
        )
        return response_struct.GetVehicleMovingInfoRes(resp)

    # 根据车辆ID列表获取车辆控制参数信息
    def get_vehicle_control_info(
        self, id_list: list[str]
    ) -> response_struct.GetVehicleControlInfoRes:
        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/control/get",
            {"simulation_id": self.simulation_id, "id_list": id_list},
        )
        return response_struct.GetVehicleControlInfoRes(resp)

    # 根据车辆ID获取车辆感知信息
    def get_vehicle_perception_info(
        self, vehicle_id: str
    ) -> response_struct.GetVehiclePerceptionInfoRes:
        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/perception/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )
        return response_struct.GetVehiclePerceptionInfoRes(resp)

    # 根据车辆ID获取车辆可选参考线
    def get_vehicle_reference_lines(
        self, vehicle_id: str
    ) -> response_struct.GetVehicleReferenceLinesRes:
        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/reference_line/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )

        return response_struct.GetVehicleReferenceLinesRes(resp)

    # 根据车辆ID获取车辆规划路径
    def get_vehicle_planning_info(
        self, vehicle_id: str
    ) -> response_struct.GetVehiclePlanningInfoRes:
        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/planning/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )
        return response_struct.GetVehiclePlanningInfoRes(resp)

    # 获取车辆导航信息,暂不支持route_nav以及lane_nav
    def get_vehicle_navigation_info(
        self, vehicle_id: str
    ) -> response_struct.GetVehicleNavigationInfoRes:
        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/navigation/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )
        return response_struct.GetVehicleNavigationInfoRes(resp)

    # 根据车辆ID检测车辆是否发生碰撞
    def get_vehicle_collision_status(
        self, vehicle_id: str
    ) -> response_struct.GetVehicleCollisionStatusRes:
        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/collision/get",
            {"simulation_id": self.simulation_id, "vehicle_id": vehicle_id},
        )

        return response_struct.GetVehicleCollisionStatusRes(resp)

    # 修改车辆规划路径
    def set_vehicle_planning_info(
        self, vehicle_id: str, planning_path: list[Point]
    ) -> response_struct.SetVehiclePlanningInfoRes:
        # FIXME: ？
        points_json = [point.to_dict() for point in planning_path]
        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/planning/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "planning_path": points_json,
            },
        )
        return response_struct.SetVehiclePlanningInfoRes(resp)

    # 修改车辆控制参数(方向盘转角、纵向加速度)
    # FIXME: ?
    def set_vehicle_control_info(
        self,
        vehicle_id: str,
        ste_wheel: float = None,
        lon_acc: float = None,
    ) -> response_struct.SetVehicleControlInfoRes:
        req_data = {"simulation_id": self.simulation_id,
                    "vehicle_id": vehicle_id}

        if ste_wheel is not None:
            req_data["ste_wheel"] = ste_wheel
        if lon_acc is not None:
            req_data["lon_acc"] = lon_acc

        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/control/set", req_data)
        return response_struct.SetVehicleControlInfoRes(resp)

    # 修改车辆点位信息{x,y,z}, phi
    def set_vehicle_position(
        self, vehicle_id: str, point: Point = None, phi: float = None
    ) -> response_struct.SetVehiclePositionRes:
        req_data = {"simulation_id": self.simulation_id,
                    "vehicle_id": vehicle_id}

        if point is not None:
            req_data["point"] = point.to_dict()
        if phi is not None:
            req_data["phi"] = phi

        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/position/set", req_data)
        return response_struct.SetVehiclePositionRes(resp)

    # 修改车辆运动信息
    def set_vehicle_moving_info(
        self,
        vehicle_id: str,
        u: float = None,
        v: float = None,
        w: float = None,
        u_acc: float = None,
        v_acc: float = None,
        w_acc: float = None,
    ) -> response_struct.SetVehicleMovingInfoRes:
        req_data = {"simulation_id": self.simulation_id,
                    "vehicle_id": vehicle_id}

        if u is not None:
            req_data["u"] = u
        if v is not None:
            req_data["v"] = v
        if w is not None:
            req_data["w"] = w
        if u_acc is not None:
            req_data["u_acc"] = u_acc
        if v_acc is not None:
            req_data["v_acc"] = v_acc
        if w_acc is not None:
            req_data["w_acc"] = w_acc

        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/moving_info/set", req_data
        )
        return response_struct.SetVehicleMovingInfoRes(resp)

    # 修改车辆基础信息, 暂不支持动力学相关参数
    def set_vehicle_base_info(
        self, vehicle_id: str, base_info: ObjBaseInfo = None
    ) -> response_struct.SetVehicleBaseInfoRes:
        req_data = {"simulation_id": self.simulation_id,
                    "vehicle_id": vehicle_id}

        if base_info is not None:
            req_data["base_info"] = base_info.to_dict()

        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/base_info/set", req_data)
        return response_struct.SetVehicleBaseInfoRes(resp)

    # # 修改车辆路段导航信息(暂不支持)
    # def set_vehicle_router_nav(self, vehicle_id: str, route_nav: list[str]):
    #     return self.client.post(
    #         "/cosim/v2/simulation/vehicle/route_nav/set",
    #         {
    #             "simulation_id": self.simulation_id,
    #             "vehicle_id": vehicle_id,
    #             "route_nav": route_nav,
    #         },
    #     )

    # 修改车辆子路段导航信息
    def set_vehicle_link_nav(
        self, vehicle_id: str, link_nav: list[str]
    ) -> response_struct.SetVehicleLinkNavRes:
        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/link_nav/set",
            {
                "simulation_id": self.simulation_id,
                "vehicle_id": vehicle_id,
                "link_nav": link_nav,
            },
        )

        return response_struct.SetVehicleLinkNavRes(resp)

    #  修改车辆终点
    def set_vehicle_destination(
        self, vehicle_id: str, destination: Point = None
    ) -> response_struct.SetVehicleDestinationRes:
        req_data = {"simulation_id": self.simulation_id,
                    "vehicle_id": vehicle_id}

        if destination is not None:
            req_data["destination"] = destination.to_dict()

        resp = self.client.post(
            "/cosim/v2/simulation/vehicle/destination/set", req_data
        )
        return response_struct.SetVehicleDestinationRes(resp)

    # 获取行人ID列表
    def get_ped_id_list(self) -> response_struct.GetPedIdListRes:
        resp = self.client.post(
            "/cosim/v2/simulation/ped/id_list/get",
            {"simulation_id": self.simulation_id},
        )
        return response_struct.GetPedIdListRes(resp)

    # 获取行人基础信息
    def get_ped_base_info(
        self, ped_id_list: list[str]
    ) -> response_struct.GetPedBaseInfoRes:
        resp = self.client.post(
            "/cosim/v2/simulation/ped/base_info/get",
            {"simulation_id": self.simulation_id, "ped_id_list": ped_id_list},
        )
        return response_struct.GetPedBaseInfoRes(resp)

    # 修改行人点位信息{x,y,z}, 航向角Phi
    def set_ped_position(
        self, ped_id: str, point: Point = None, phi: float = None
    ) -> response_struct.SetPedPositionRes:
        req_data = {"simulation_id": self.simulation_id, "ped_id": ped_id}

        if point is not None:
            req_data["point"] = point.to_dict()
        if phi is not None:
            req_data["phi"] = phi

        resp = self.client.post(
            "/cosim/v2/simulation/ped/position/set", req_data)
        return response_struct.SetPedPositionRes(resp)

    # 获取非机动车ID列表
    def get_nmv_id_list(self) -> response_struct.GetNMVIdListRes:
        resp = self.client.post(
            "/cosim/v2/simulation/nmv/id_list/get",
            {"simulation_id": self.simulation_id},
        )
        return response_struct.GetNMVIdListRes(resp)

    # 获取非机动车基础信息
    def get_nmv_base_info(
        self, nmv_id_list: list[str]
    ) -> response_struct.GetNMVBaseInfoRes:
        resp = self.client.post(
            "/cosim/v2/simulation/nmv/base_info/get",
            {"simulation_id": self.simulation_id, "nmv_id_list": nmv_id_list},
        )
        return response_struct.GetNMVBaseInfoRes(resp)

    # 修改非机动车点位信息{x,y,z}, 航向角Phi
    def set_nmv_position(
        self, nmv_id: str, point: Point = None, phi: float = None
    ) -> response_struct.SetNMVPositionRes:
        req_data = {"simulation_id": self.simulation_id, "nmv_id": nmv_id}

        if point is not None:
            req_data["point"] = point
        if phi is not None:
            req_data["phi"] = phi

        resp = self.client.post(
            "/cosim/v2/simulation/nmv/position/set", req_data)
        return response_struct.SetNMVPositionRes(resp)

    # 直接给仿真器发post请求
    def do_post(self, path: str, data: dict):
        return self.client.post(path, data)

    # 直接给仿真器发get请求
    def do_get(self, path: str, params: dict):
        return self.client.get(path, params)
