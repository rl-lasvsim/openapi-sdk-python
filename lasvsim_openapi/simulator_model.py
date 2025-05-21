"""
Simulator model module for the lasvsim API.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import IntEnum


@dataclass
class Point:
    """Point information."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None

        instance = cls()
        instance.__dict__ = data
        return instance


@dataclass
class ObjBaseInfo:
    """Object base information."""

    width: float = 0.0
    height: float = 0.0
    length: float = 0.0
    weight: float = 0.0
    max_dec: float = 0.0
    max_acc: float = 0.0
    max_speed: float = 0.0

    def __init__(
        self,
        width: float = 0.0,
        height: float = 0.0,
        length: float = 0.0,
        weight: float = 0.0,
        max_dec: float = 0.0,
        max_acc: float = 0.0,
        max_speed: float = 0.0,
    ):
        self.width = width
        self.height = height
        self.length = length
        self.weight = weight
        self.max_dec = max_dec
        self.max_acc = max_acc
        self.max_speed = max_speed

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            width=data.get("width", 0.0),
            height=data.get("height", 0.0),
            length=data.get("length", 0.0),
            weight=data.get("weight", 0.0),
            max_dec=data.get("max_dec", 0.0),
            max_acc=data.get("max_acc", 0.0),
            max_speed=data.get("max_speed", 0.0),
        )


@dataclass
class DynamicInfo:
    """Dynamic information."""

    front_wheel_stiffness: float = 0.0
    rear_wheel_stiffness: float = 0.0
    front_axle_to_center: float = 0.0
    rear_axle_to_center: float = 0.0
    yaw_moment_of_inertia: float = 0.0

    def __init__(
        self,
        front_wheel_stiffness: float = 0.0,
        rear_wheel_stiffness: float = 0.0,
        front_axle_to_center: float = 0.0,
        rear_axle_to_center: float = 0.0,
        yaw_moment_of_inertia: float = 0.0,
    ):
        self.front_wheel_stiffness = front_wheel_stiffness
        self.rear_wheel_stiffness = rear_wheel_stiffness
        self.front_axle_to_center = front_axle_to_center
        self.rear_axle_to_center = rear_axle_to_center
        self.yaw_moment_of_inertia = yaw_moment_of_inertia

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            front_wheel_stiffness=data.get("front_wheel_stiffness", 0.0),
            rear_wheel_stiffness=data.get("rear_wheel_stiffness", 0.0),
            front_axle_to_center=data.get("front_axle_to_center", 0.0),
            rear_axle_to_center=data.get("rear_axle_to_center", 0.0),
            yaw_moment_of_inertia=data.get("yaw_moment_of_inertia", 0.0),
        )


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

    type: int = 0
    heading: Optional[float] = None
    roll: Optional[float] = None
    patch: Optional[float] = None
    lane_index: Optional[int] = None
    lane_offset: Optional[float] = None
    s: Optional[float] = None
    t: Optional[float] = None

    def __init__(
        self,
        point: Optional[Point] = None,
        phi: float = 0.0,
        lane_id: str = "",
        link_id: str = "",
        junction_id: str = "",
        segment_id: str = "",
        dis_to_lane_end: Optional[float] = None,
        position_type: int = 0,
        type: int = 0,
        heading: Optional[float] = None,
        roll: Optional[float] = None,
        patch: Optional[float] = None,
        lane_index: Optional[int] = None,
        lane_offset: Optional[float] = None,
        s: Optional[float] = None,
        t: Optional[float] = None,
    ):
        self.point = point
        self.phi = phi
        self.lane_id = lane_id
        self.link_id = link_id
        self.junction_id = junction_id
        self.segment_id = segment_id
        self.dis_to_lane_end = dis_to_lane_end
        self.position_type = position_type
        self.type = type
        self.heading = heading
        self.roll = roll
        self.patch = patch
        self.lane_index = lane_index
        self.lane_offset = lane_offset
        self.s = s
        self.t = t

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            point=Point.from_dict(data.get("point")),
            phi=data.get("phi", 0.0),
            lane_id=data.get("lane_id", ""),
            link_id=data.get("link_id", ""),
            junction_id=data.get("junction_id", ""),
            segment_id=data.get("segment_id", ""),
            dis_to_lane_end=data.get("dis_to_lane_end"),
            position_type=data.get("position_type", 0),
            type=data.get("type", 0),
            heading=data.get("heading"),
            roll=data.get("roll"),
            patch=data.get("patch"),
            lane_index=data.get("lane_index"),
            lane_offset=data.get("lane_offset"),
            s=data.get("s"),
            t=data.get("t"),
        )


@dataclass
class ObjMovingInfo:
    """Object moving information."""

    u: float = 0.0
    u_acc: float = 0.0
    v: float = 0.0
    v_acc: float = 0.0
    w: float = 0.0
    w_acc: float = 0.0

    heading: float = 0.0

    def __init__(
        self,
        u: float = 0.0,
        u_acc: float = 0.0,
        v: float = 0.0,
        v_acc: float = 0.0,
        w: float = 0.0,
        w_acc: float = 0.0,
        heading: float = 0.0,
    ):
        self.u = u
        self.u_acc = u_acc
        self.v = v
        self.v_acc = v_acc
        self.w = w
        self.w_acc = w_acc
        self.heading = heading

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            u=data.get("u", 0.0),
            u_acc=data.get("u_acc", 0.0),
            v=data.get("v", 0.0),
            v_acc=data.get("v_acc", 0.0),
            w=data.get("w", 0.0),
            w_acc=data.get("w_acc", 0.0),
            heading=data.get("heading", 0.0),
        )


@dataclass
class ControlInfo:
    """Control information."""

    ste_wheel: float = 0.0
    lon_acc: float = 0.0
    fl_torque: float = 0.0
    fr_torque: float = 0.0
    rl_torque: float = 0.0
    rr_torque: float = 0.0

    def __init__(
        self,
        ste_wheel: float = 0.0,
        lon_acc: float = 0.0,
        fl_torque: float = 0.0,
        fr_torque: float = 0.0,
        rl_torque: float = 0.0,
        rr_torque: float = 0.0,
    ):
        self.ste_wheel = ste_wheel
        self.lon_acc = lon_acc
        self.fl_torque = fl_torque
        self.fr_torque = fr_torque
        self.rl_torque = rl_torque
        self.rr_torque = rr_torque

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            ste_wheel=data.get("ste_wheel", 0.0),
            lon_acc=data.get("lon_acc", 0.0),
            fl_torque=data.get("fl_torque", 0.0),
            fr_torque=data.get("fr_torque", 0.0),
            rl_torque=data.get("rl_torque", 0.0),
            rr_torque=data.get("rr_torque", 0.0),
        )


@dataclass
class ReferenceLine:
    """Reference line information."""

    lane_ids: List[str] = field(default_factory=list)
    lane_types: List[str] = field(default_factory=list)
    points: List[Point] = field(default_factory=list)
    lane_idxes: List[int] = field(default_factory=list)
    opposite: bool = False

    def __init__(
        self,
        lane_ids: List[str] = None,
        lane_types: List[str] = None,
        points: List[Point] = None,
        lane_idxes: List[int] = None,
        opposite: bool = False,
    ):
        self.lane_ids = lane_ids if lane_ids is not None else []
        self.lane_types = lane_types if lane_types is not None else []
        self.points = points if points is not None else []
        self.lane_idxes = lane_idxes if lane_idxes is not None else []
        self.opposite = opposite

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None

        point = data.pop("points", [])

        instance = cls()
        instance.__dict__ = data
        instance.points = [Point.from_dict(p) for p in point]

        return instance


@dataclass
class NavigationInfo:
    """Navigation information."""

    link_nav: List[str] = field(default_factory=list)
    destination: Optional[Position] = None

    def __init__(
        self, link_nav: List[str] = None, destination: Optional[Position] = None
    ):
        self.link_nav = link_nav if link_nav is not None else []
        self.destination = destination

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            link_nav=data.get("link_nav", []),
            destination=Position.from_dict(data.get("destination")),
        )


@dataclass
class Movement:
    """Movement information."""

    map_id: int = 0
    movement_id: str = ""
    upstream_link_id: str = ""
    downstream_link_id: str = ""
    junction_id: str = ""
    flow_direction: str = ""

    def __init__(
        self,
        map_id: int = 0,
        movement_id: str = "",
        upstream_link_id: str = "",
        downstream_link_id: str = "",
        junction_id: str = "",
        flow_direction: str = "",
    ):
        self.map_id = map_id
        self.movement_id = movement_id
        self.upstream_link_id = upstream_link_id
        self.downstream_link_id = downstream_link_id
        self.junction_id = junction_id
        self.flow_direction = flow_direction

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            map_id=data.get("map_id", 0),
            movement_id=data.get("movement_id", ""),
            upstream_link_id=data.get("upstream_link_id", ""),
            downstream_link_id=data.get("downstream_link_id", ""),
            junction_id=data.get("junction_id", ""),
            flow_direction=data.get("flow_direction", ""),
        )


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

    def __init__(self, scen_id: str = "", scen_ver: str = "", sim_record_id: str = ""):
        self.scen_id = scen_id
        self.scen_ver = scen_ver
        self.sim_record_id = sim_record_id


@dataclass
class InitReq:
    """Request for initializing simulator."""

    scen_id: str = ""
    scen_ver: str = ""
    sim_record_id: str = ""

    def __init__(self, scen_id: str = "", scen_ver: str = "", sim_record_id: str = ""):
        self.scen_id = scen_id
        self.scen_ver = scen_ver
        self.sim_record_id = sim_record_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            scen_id=data.get("scen_id", ""),
            scen_ver=data.get("scen_ver", ""),
            sim_record_id=data.get("sim_record_id", ""),
        )


@dataclass
class InitRes:
    """Response for initializing simulator."""

    simulation_id: str = ""
    simulation_addr: str = ""

    def __init__(self, simulation_id: str = "", simulation_addr: str = ""):
        self.simulation_id = simulation_id
        self.simulation_addr = simulation_addr

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            simulation_addr=data.get("simulation_addr", ""),
        )


@dataclass
class StopReq:
    """Request for stopping simulator."""

    simulation_id: str = ""

    def __init__(self, simulation_id: str = ""):
        self.simulation_id = simulation_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class StopRes:
    """Response for stopping simulator."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class StepReq:
    """Request for stepping simulator."""

    simulation_id: str = ""

    def __init__(self, simulation_id: str = ""):
        self.simulation_id = simulation_id


class StepCode(IntEnum):
    """Step status code.
    0: running
    1001: finished normally
    1002: failed
    """

    RUNNING = 0
    FINISHED = 1001
    FAILED = 1002

    def is_running(self) -> bool:
        """Check if step is running."""
        return 0 <= self.value <= 100

    def is_stopped(self) -> bool:
        """Check if step is stopped."""
        return self.value == self.FINISHED

    def is_unpassed(self) -> bool:
        """Check if step is unpassed."""
        return self.value == self.FAILED


@dataclass
class StepRes:
    """Response for stepping simulator."""

    code: StepCode = StepCode.RUNNING
    message: str = ""

    def __init__(self, code: StepCode = StepCode.RUNNING, message: str = ""):
        self.code = code
        self.message = message

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(code=StepCode(data.get("code", 0)), message=data.get("message", ""))


@dataclass
class ResetVehicleConfig:
    vehicle_id: str = ""  # 测试车辆ID
    link_path: List[str] = field(default_factory=list)  # 设置指定导航信息
    s_range: List[float] = field(default_factory=list)  # 起始位置

    def __init__(
        self,
        vehicle_id: str = "",
        link_path: List[str] = None,
        s_range: List[float] = None,
    ):
        self.vehicle_id = vehicle_id
        self.link_path = link_path if link_path is not None else []
        self.s_range = s_range if s_range is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            vehicle_id=data.get("vehicle_id", ""),
            link_path=data.get("link_path", []),
            s_range=data.get("s_range", []),
        )


@dataclass
class VehicleDistribution:
    density: float = 0.0  # 密度
    min_target_speed: float = 0.0  # 最小目标速度
    max_target_speed: float = 0.0  # 最大目标速度
    size_ratio: List[float] = field(default_factory=list)
    style_ratio: List[float] = field(default_factory=list)
    skill_ratio: List[float] = field(default_factory=list)

    def __init__(
        self,
        density: float = 0.0,
        min_target_speed: float = 0.0,
        max_target_speed: float = 0.0,
        size_ratio: List[float] = None,
        style_ratio: List[float] = None,
        skill_ratio: List[float] = None,
    ):
        self.density = density
        self.min_target_speed = min_target_speed
        self.max_target_speed = max_target_speed
        self.size_ratio = size_ratio if size_ratio is not None else []
        self.style_ratio = style_ratio if style_ratio is not None else []
        self.skill_ratio = skill_ratio if skill_ratio is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            density=data.get("density", 0.0),
            min_target_speed=data.get("min_target_speed", 0.0),
            max_target_speed=data.get("max_target_speed", 0.0),
            size_ratio=data.get("size_ratio", []),
            style_ratio=data.get("style_ratio", []),
            skill_ratio=data.get("skill_ratio", []),
        )


@dataclass
class PedestrianDistribution:
    density: float = 0.0  # 密度
    ages_ratio: List[float] = field(default_factory=list)
    style_ratio: List[float] = field(default_factory=list)

    def __init__(
        self,
        density: float = 0.0,
        ages_ratio: List[float] = None,
        style_ratio: List[float] = None,
    ):
        self.density = density
        self.ages_ratio = ages_ratio if ages_ratio is not None else []
        self.style_ratio = style_ratio if style_ratio is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            density=data.get("density", 0.0),
            ages_ratio=data.get("ages_ratio", []),
            style_ratio=data.get("style_ratio", []),
        )


@dataclass
class NMVDistribution:
    density: float = 0.0  # 密度
    subtype_ratio: List[float] = field(default_factory=list)  # 车型比例
    style_ratio: List[float] = field(default_factory=list)  # 车型比例
    skill_ratio: List[float] = field(default_factory=list)  # 车型比例
    min_target_speed: float = 0.0  # 最小目标速度
    max_target_speed: float = 0.0  # 最大目标速度

    def __init__(
        self,
        density: float = 0.0,
        min_target_speed: float = 0.0,
        max_target_speed: float = 0.0,
        subtype_ratio: List[float] = None,
        skill_ratio: List[float] = None,
    ):
        self.density = density
        self.min_target_speed = min_target_speed
        self.max_target_speed = max_target_speed
        self.subtype_ratio = subtype_ratio if subtype_ratio is not None else []
        self.skill_ratio = skill_ratio if skill_ratio is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            density=data.get("density", 0.0),
            min_target_speed=data.get("min_target_speed", 0.0),
            max_target_speed=data.get("max_target_speed", 0.0),
            subtype_ratio=data.get("subtype_ratio", []),
            skill_ratio=data.get("skill_ratio", []),
        )


@dataclass
class ResetEnvPtcs:
    vehicle_distribution: VehicleDistribution = field(
        default_factory=VehicleDistribution
    )  # 车辆分布
    ped_conf: PedestrianDistribution = field(
        default_factory=PedestrianDistribution
    )  # 行人分布
    nmv_conf: NMVDistribution = field(default_factory=NMVDistribution)  # NMV分布

    def __init__(
        self,
        vehicle_distribution: VehicleDistribution = None,
        ped_conf: PedestrianDistribution = None,
        nmv_conf: NMVDistribution = None,
    ):
        self.vehicle_distribution = (
            vehicle_distribution
            if vehicle_distribution is not None
            else VehicleDistribution()
        )
        self.ped_conf = ped_conf if ped_conf is not None else PedestrianDistribution()
        self.nmv_conf = nmv_conf if nmv_conf is not None else NMVDistribution()

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            vehicle_distribution=VehicleDistribution.from_dict(
                data.get("vehicle_conf")
            ),
            ped_conf=PedestrianDistribution.from_dict(data.get("ped_conf")),
            nmv_conf=NMVDistribution.from_dict(data.get("nmv_conf")),
        )


@dataclass
class ResetReq:
    """Request for resetting simulator."""

    simulation_id: str = ""
    reset_traffic_flow: bool = False
    reset_vehicle: List[ResetVehicleConfig] = field(
        default_factory=list
    )  # 重置车辆配置
    reset_env_ptcs: Optional[ResetEnvPtcs] = None

    def __init__(
        self,
        simulation_id: str = "",
        reset_traffic_flow: bool = False,
        reset_vehicle: List[ResetVehicleConfig] = None,
        reset_env_ptcs: Optional[ResetEnvPtcs] = None,
    ):
        self.simulation_id = simulation_id
        self.reset_traffic_flow = reset_traffic_flow
        self.reset_vehicle = reset_vehicle if reset_vehicle is not None else []
        self.reset_env_ptcs = reset_env_ptcs if reset_env_ptcs is not None else None

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            reset_traffic_flow=data.get("reset_traffic_flow", False),
            reset_vehicle=[
                ResetVehicleConfig.from_dict(v) for v in data.get("reset_vehicle", [])
            ],
            reset_env_ptcs=ResetEnvPtcs.from_dict(data.get("reset_env_ptcs")),
        )


@dataclass
class ResetRes:
    """Response for resetting simulator."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class GetCurrentStageReq:
    """Request for getting current stage."""

    simulation_id: str = ""  # 仿真ID
    junction_id: str = ""  # movementId

    def __init__(self, simulation_id: str = "", junction_id: str = ""):
        self.simulation_id = simulation_id
        self.junction_id = junction_id


@dataclass
class GetCurrentStageRes:
    """Response for getting current stage."""

    movement_ids: List[str] = field(default_factory=list)  # 当前阶段包含的绿灯流向
    countdown: int = 0  # 倒计时(s)

    def __init__(self, movement_ids: List[str] = None, countdown: int = 0):
        self.movement_ids = movement_ids if movement_ids is not None else []
        self.countdown = countdown

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            movement_ids=data.get("movement_ids", []),
            countdown=data.get("countdown", 0),
        )


@dataclass
class GetMovementSignalReq:
    """Request for getting movement signal."""

    simulation_id: str = ""  # 仿真ID
    movement_id: str = ""  # movementId

    def __init__(self, simulation_id: str = "", movement_id: str = ""):
        self.simulation_id = simulation_id
        self.movement_id = movement_id


@dataclass
class GetMovementSignalRes:
    """Response for getting movement signal."""

    current_signal: int = 0  # 当前灯色
    countdown: int = 0  # 倒计时(s)

    def __init__(self, current_signal: int = 0, countdown: int = 0):
        self.current_signal = current_signal
        self.countdown = countdown

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            current_signal=data.get("current_signal", 0),
            countdown=data.get("countdown", 0),
        )


@dataclass
class GetSignalPlanRes_Stage:
    """Stage information in signal plan."""

    movement_ids: List[str] = field(default_factory=list)
    duration: int = 0  # 时长(s)

    def __init__(self, movement_ids: List[str] = None, duration: int = 0):
        self.movement_ids = movement_ids if movement_ids is not None else []
        self.duration = duration

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            movement_ids=data.get("movement_ids", []), duration=data.get("duration", 0)
        )


@dataclass
class GetSignalPlanReq:
    """Request for getting signal plan."""

    simulation_id: str = ""
    junction_id: str = ""

    def __init__(self, simulation_id: str = "", junction_id: str = ""):
        self.simulation_id = simulation_id
        self.junction_id = junction_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            junction_id=data.get("junction_id", ""),
        )


@dataclass
class GetSignalPlanRes:
    """Response for getting signal plan."""

    junction_id: str = ""
    cycle: int = 0
    offset: int = 0
    stages: List[GetSignalPlanRes_Stage] = field(default_factory=list)

    def __init__(
        self,
        junction_id: str = "",
        cycle: int = 0,
        offset: int = 0,
        stages: List[GetSignalPlanRes_Stage] = None,
    ):
        self.junction_id = junction_id
        self.cycle = cycle
        self.offset = offset
        self.stages = stages if stages is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            junction_id=data.get("junction_id", ""),
            cycle=data.get("cycle", 0),
            offset=data.get("offset", 0),
            stages=[
                GetSignalPlanRes_Stage.from_dict(item)
                for item in data.get("stages", [])
            ],
        )


@dataclass
class GetMovementListReq:
    """Request for getting movement list."""

    simulation_id: str = ""
    junction_id: str = ""

    def __init__(self, simulation_id: str = "", junction_id: str = ""):
        self.simulation_id = simulation_id
        self.junction_id = junction_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            junction_id=data.get("junction_id", ""),
        )


@dataclass
class GetMovementListRes:
    """Response for getting movement list."""

    list: List[Movement] = field(default_factory=list)  # movement 列表

    def __init__(self, list: List[Movement] = None):
        self.list = list if list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(list=[Movement.from_dict(item) for item in data.get("list", [])])


@dataclass
class GetVehicleIdListReq:
    """Request for getting vehicle ID list."""

    simulation_id: str = ""  # 仿真ID

    def __init__(self, simulation_id: str = ""):
        self.simulation_id = simulation_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(simulation_id=data.get("simulation_id", ""))


@dataclass
class GetVehicleIdListRes:
    """Response for getting vehicle ID list."""

    list: List[str] = field(default_factory=list)  # 车辆ID列表

    def __init__(self, list: List[str] = None):
        self.list = list if list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(list=data.get("list", []))


@dataclass
class GetTestVehicleIdListReq:
    """Request for getting test vehicle ID list."""

    simulation_id: str = ""  # 仿真ID

    def __init__(self, simulation_id: str = ""):
        self.simulation_id = simulation_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(simulation_id=data.get("simulation_id", ""))


@dataclass
class GetTestVehicleIdListRes:
    """Response for getting test vehicle ID list."""

    list: List[str] = field(default_factory=list)

    def __init__(self, list: List[str] = None):
        self.list = list if list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(list=data.get("list", []))


@dataclass
class GetVehicleBaseInfoReq:
    """Request for getting vehicle base information."""

    simulation_id: str = ""
    id_list: List[str] = field(default_factory=list)

    def __init__(self, simulation_id: str = "", id_list: List[str] = None):
        self.simulation_id = simulation_id
        self.id_list = id_list if id_list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""), id_list=data.get("id_list", [])
        )


@dataclass
class GetVehicleBaseInfoRes_VehicleBaseInfo:
    """Vehicle base information."""

    base_info: Optional[ObjBaseInfo] = None
    dynamic_info: Optional[DynamicInfo] = None

    def __init__(
        self,
        base_info: Optional[ObjBaseInfo] = None,
        dynamic_info: Optional[DynamicInfo] = None,
    ):
        self.base_info = base_info
        self.dynamic_info = dynamic_info

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            base_info=ObjBaseInfo.from_dict(data.get("base_info")),
            dynamic_info=DynamicInfo.from_dict(data.get("dynamic_info")),
        )


@dataclass
class GetVehicleBaseInfoRes:
    """Response for getting vehicle base information."""

    info_dict: Dict[str, GetVehicleBaseInfoRes_VehicleBaseInfo] = field(
        default_factory=dict
    )

    def __init__(
        self, info_dict: Dict[str, GetVehicleBaseInfoRes_VehicleBaseInfo] = None
    ):
        self.info_dict = info_dict if info_dict is not None else {}

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            info_dict={
                k: GetVehicleBaseInfoRes_VehicleBaseInfo.from_dict(v)
                for k, v in data.get("info_dict", {}).items()
            }
        )


@dataclass
class GetVehiclePositionReq:
    """Request for getting vehicle position."""

    simulation_id: str = ""
    id_list: List[str] = field(default_factory=list)

    def __init__(self, simulation_id: str = "", id_list: List[str] = None):
        self.simulation_id = simulation_id
        self.id_list = id_list if id_list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""), id_list=data.get("id_list", [])
        )


@dataclass
class GetVehiclePositionRes:
    """Response for getting vehicle position."""

    position_dict: Dict[str, Position] = field(default_factory=dict)

    def __init__(self, position_dict: Dict[str, Position] = None):
        self.position_dict = position_dict if position_dict is not None else {}

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            position_dict={
                k: Position.from_dict(v)
                for k, v in data.get("position_dict", {}).items()
            }
        )


@dataclass
class GetVehicleMovingInfoReq:
    """Request for getting vehicle moving information."""

    simulation_id: str = ""
    id_list: List[str] = field(default_factory=list)

    def __init__(self, simulation_id: str = "", id_list: List[str] = None):
        self.simulation_id = simulation_id
        self.id_list = id_list if id_list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""), id_list=data.get("id_list", [])
        )


@dataclass
class GetVehicleMovingInfoRes:
    """Response for getting vehicle moving information."""

    moving_info_dict: Dict[str, ObjMovingInfo] = field(default_factory=dict)

    def __init__(self, moving_info_dict: Dict[str, ObjMovingInfo] = None):
        self.moving_info_dict = moving_info_dict if moving_info_dict is not None else {}

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            moving_info_dict={
                k: ObjMovingInfo.from_dict(v)
                for k, v in data.get("moving_info_dict", {}).items()
            }
        )


@dataclass
class GetVehicleControlInfoReq:
    """Request for getting vehicle control information."""

    simulation_id: str = ""
    id_list: List[str] = field(default_factory=list)

    def __init__(self, simulation_id: str = "", id_list: List[str] = None):
        self.simulation_id = simulation_id
        self.id_list = id_list if id_list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""), id_list=data.get("id_list", [])
        )


@dataclass
class GetVehicleControlInfoRes:
    """Response for getting vehicle control information."""

    control_info_dict: Dict[str, ControlInfo] = field(default_factory=dict)

    def __init__(self, control_info_dict: Dict[str, ControlInfo] = None):
        self.control_info_dict = (
            control_info_dict if control_info_dict is not None else {}
        )

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            control_info_dict={
                k: ControlInfo.from_dict(v)
                for k, v in data.get("control_info_dict", {}).items()
            }
        )


@dataclass
class GetVehiclePerceptionInfoReq:
    """Request for getting vehicle perception information."""

    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, simulation_id: str = "", vehicle_id: str = ""):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
        )


@dataclass
class GetVehiclePerceptionInfoRes_PerceptionObj:
    """Perception object information."""

    obj_id: str = ""
    base_info: Optional[ObjBaseInfo] = None
    moving_info: Optional[ObjMovingInfo] = None
    position: Optional[Position] = None

    def __init__(
        self,
        obj_id: str = "",
        base_info: Optional[ObjBaseInfo] = None,
        moving_info: Optional[ObjMovingInfo] = None,
        position: Optional[Position] = None,
    ):
        self.obj_id = obj_id
        self.base_info = base_info
        self.moving_info = moving_info
        self.position = position

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            obj_id=data.get("obj_id", ""),
            base_info=ObjBaseInfo.from_dict(data.get("base_info")),
            moving_info=ObjMovingInfo.from_dict(data.get("moving_info")),
            position=Position.from_dict(data.get("position")),
        )


@dataclass
class GetVehiclePerceptionInfoRes:
    """Response for getting vehicle perception information."""

    list: List[GetVehiclePerceptionInfoRes_PerceptionObj] = field(default_factory=list)

    def __init__(self, list: List[GetVehiclePerceptionInfoRes_PerceptionObj] = None):
        self.list = list if list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            list=[
                GetVehiclePerceptionInfoRes_PerceptionObj.from_dict(item)
                for item in data.get("list", [])
            ]
        )


@dataclass
class GetVehicleReferenceLinesReq:
    """Request for getting vehicle reference lines."""

    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, simulation_id: str = "", vehicle_id: str = ""):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
        )


@dataclass
class GetVehicleReferenceLinesRes:
    """Response for getting vehicle reference lines."""

    reference_lines: List[ReferenceLine] = field(default_factory=list)

    def __init__(self, reference_lines: List[ReferenceLine] = None):
        self.reference_lines = reference_lines if reference_lines is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            reference_lines=[
                ReferenceLine.from_dict(item)
                for item in data.get("reference_lines", [])
            ]
        )


@dataclass
class GetVehiclePlanningInfoReq:
    """Request for getting vehicle planning information."""

    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, simulation_id: str = "", vehicle_id: str = ""):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
        )


@dataclass
class GetVehiclePlanningInfoRes:
    """Response for getting vehicle planning information."""

    planning_path: List[Point] = field(default_factory=list)

    def __init__(self, planning_path: List[Point] = None):
        self.planning_path = planning_path if planning_path is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            planning_path=[Point.from_dict(p) for p in data.get("planning_path", [])]
        )


@dataclass
class GetVehicleNavigationInfoReq:
    """Request for getting vehicle navigation information."""

    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, simulation_id: str = "", vehicle_id: str = ""):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
        )


@dataclass
class GetVehicleNavigationInfoRes:
    """Response for getting vehicle navigation information."""

    navigation_info: Optional[NavigationInfo] = None

    def __init__(self, navigation_info: Optional[NavigationInfo] = None):
        self.navigation_info = navigation_info

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            navigation_info=NavigationInfo.from_dict(data.get("navigation_info"))
        )


@dataclass
class GetVehicleCollisionStatusReq:
    """Request for getting vehicle collision status."""

    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, simulation_id: str = "", vehicle_id: str = ""):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
        )


@dataclass
class GetVehicleCollisionStatusRes:
    """Response for getting vehicle collision status."""

    collision_status: bool = False

    def __init__(self, collision_status: bool = False):
        self.collision_status = collision_status

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(collision_status=data.get("collision_status", False))


@dataclass
class GetVehicleTargetSpeedReq:
    """Request for getting vehicle target speed."""

    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, simulation_id: str = "", vehicle_id: str = ""):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
        )


@dataclass
class GetVehicleTargetSpeedRes:
    """Response for getting vehicle target speed."""

    target_speed: float = 0.0

    def __init__(self, target_speed: float = 0.0):
        self.target_speed = target_speed

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(target_speed=data.get("target_speed", 0.0))


@dataclass
class SetVehiclePlanningInfoReq:
    """Request for setting vehicle planning information."""

    simulation_id: str = ""
    vehicle_id: str = ""
    planning_path: List[Point] = field(default_factory=list)
    speed: List[float] = field(default_factory=list)  # Trajectory point speeds

    def __init__(
        self,
        simulation_id: str = "",
        vehicle_id: str = "",
        planning_path: List[Point] = None,
        speed: List[float] = None,
    ):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.planning_path = planning_path if planning_path is not None else []
        self.speed = speed if speed is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
            planning_path=[Point.from_dict(x) for x in data.get("planning_path", [])],
            speed=data.get("speed", []),
        )


@dataclass
class SetVehicleControlInfoReq:
    """Request for setting vehicle control information."""

    simulation_id: str = ""
    vehicle_id: str = ""
    ste_wheel: Optional[float] = None
    lon_acc: Optional[float] = None

    def __init__(
        self,
        simulation_id: str = "",
        vehicle_id: str = "",
        ste_wheel: Optional[float] = None,
        lon_acc: Optional[float] = None,
    ):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.ste_wheel = ste_wheel
        self.lon_acc = lon_acc

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
            ste_wheel=data.get("ste_wheel"),
            lon_acc=data.get("lon_acc"),
        )


@dataclass
class SetVehiclePositionReq:
    """Request for setting vehicle position."""

    simulation_id: str = ""
    vehicle_id: str = ""
    point: Optional[Point] = None
    phi: Optional[float] = None

    def __init__(
        self,
        simulation_id: str = "",
        vehicle_id: str = "",
        point: Optional[Point] = None,
        phi: Optional[float] = None,
    ):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.point = point
        self.phi = phi

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
            point=Point.from_dict(data.get("point")),
            phi=data.get("phi"),
        )


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

    def __init__(
        self,
        simulation_id: str = "",
        vehicle_id: str = "",
        u: Optional[float] = None,
        v: Optional[float] = None,
        w: Optional[float] = None,
        u_acc: Optional[float] = None,
        v_acc: Optional[float] = None,
        w_acc: Optional[float] = None,
    ):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.u = u
        self.v = v
        self.w = w
        self.u_acc = u_acc
        self.v_acc = v_acc
        self.w_acc = w_acc

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
            u=data.get("u"),
            v=data.get("v"),
            w=data.get("w"),
            u_acc=data.get("u_acc"),
            v_acc=data.get("v_acc"),
            w_acc=data.get("w_acc"),
        )


@dataclass
class SetVehicleBaseInfoReq:
    """Request for setting vehicle base information."""

    simulation_id: str = ""
    vehicle_id: str = ""
    base_info: Optional[ObjBaseInfo] = None
    dynamic_info: Optional[DynamicInfo] = None

    def __init__(
        self,
        simulation_id: str = "",
        vehicle_id: str = "",
        base_info: Optional[ObjBaseInfo] = None,
        dynamic_info: Optional[DynamicInfo] = None,
    ):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.base_info = base_info
        self.dynamic_info = dynamic_info

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
            base_info=ObjBaseInfo.from_dict(data.get("base_info")),
            dynamic_info=DynamicInfo.from_dict(data.get("dynamic_info")),
        )


@dataclass
class SetVehicleRouteNavReq:
    """Request for setting vehicle route navigation."""

    simulation_id: str = ""
    vehicle_id: str = ""
    route_nav: List[str] = field(default_factory=list)

    def __init__(
        self, simulation_id: str = "", vehicle_id: str = "", route_nav: List[str] = None
    ):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.route_nav = route_nav if route_nav is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
            route_nav=data.get("route_nav", []),
        )


@dataclass
class SetVehicleLinkNavReq:
    """Request for setting vehicle link navigation."""

    simulation_id: str = ""
    vehicle_id: str = ""
    link_nav: List[str] = field(default_factory=list)

    def __init__(
        self, simulation_id: str = "", vehicle_id: str = "", link_nav: List[str] = None
    ):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.link_nav = link_nav if link_nav is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
            link_nav=data.get("link_nav", []),
        )


@dataclass
class SetVehicleLaneNavReq:
    """Request for setting vehicle lane navigation."""

    simulation_id: str = ""
    vehicle_id: str = ""
    lane_nav: List[LaneNav] = field(default_factory=list)

    def __init__(
        self,
        simulation_id: str = "",
        vehicle_id: str = "",
        lane_nav: List[LaneNav] = None,
    ):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.lane_nav = lane_nav if lane_nav is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
            lane_nav=[LaneNav.from_dict(nav) for nav in data.get("lane_nav", [])],
        )


@dataclass
class SetVehicleDestinationReq:
    """Request for setting vehicle destination."""

    simulation_id: str = ""
    vehicle_id: str = ""
    destination: Optional[Point] = None

    def __init__(
        self,
        simulation_id: str = "",
        vehicle_id: str = "",
        destination: Optional[Point] = None,
    ):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id
        self.destination = destination

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
            destination=Point.from_dict(data.get("destination")),
        )


@dataclass
class SetPedPositionReq:
    """Request for setting pedestrian position."""

    simulation_id: str = ""
    ped_id: str = ""
    point: Optional[Point] = None
    phi: Optional[float] = None

    def __init__(
        self,
        simulation_id: str = "",
        ped_id: str = "",
        point: Optional[Point] = None,
        phi: Optional[float] = None,
    ):
        self.simulation_id = simulation_id
        self.ped_id = ped_id
        self.point = point
        self.phi = phi

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            ped_id=data.get("ped_id", ""),
            point=Point.from_dict(data.get("point")),
            phi=data.get("phi"),
        )


@dataclass
class SetNMVPositionReq:
    """Request for setting non-motor vehicle position."""

    simulation_id: str = ""
    nmv_id: str = ""
    point: Optional[Point] = None
    phi: Optional[float] = None

    def __init__(
        self,
        simulation_id: str = "",
        nmv_id: str = "",
        point: Optional[Point] = None,
        phi: Optional[float] = None,
    ):
        self.simulation_id = simulation_id
        self.nmv_id = nmv_id
        self.point = point
        self.phi = phi

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            nmv_id=data.get("nmv_id", ""),
            point=Point.from_dict(data.get("point")),
            phi=data.get("phi"),
        )


@dataclass
class GetPedIdListReq:
    """Request for getting pedestrian ID list."""

    simulation_id: str = ""  # 仿真ID

    def __init__(self, simulation_id: str = ""):
        self.simulation_id = simulation_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(simulation_id=data.get("simulation_id", ""))


@dataclass
class GetPedIdListRes:
    """Response for getting pedestrian ID list."""

    list: List[str] = field(default_factory=list)  # 行人ID列表

    def __init__(self, list: List[str] = None):
        self.list = list if list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(list=data.get("list", []))


@dataclass
class GetPedBaseInfoReq:
    """Request for getting pedestrian base information."""

    simulation_id: str = ""
    ped_id_list: List[str] = field(default_factory=list)

    def __init__(self, simulation_id: str = "", ped_id_list: List[str] = None):
        self.simulation_id = simulation_id
        self.ped_id_list = ped_id_list if ped_id_list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            ped_id_list=data.get("ped_id_list", []),
        )


@dataclass
class GetPedBaseInfoRes:
    """Response for getting pedestrian base information."""

    base_info_dict: Dict[str, ObjBaseInfo] = field(default_factory=dict)

    def __init__(self, base_info_dict: Dict[str, ObjBaseInfo] = None):
        self.base_info_dict = base_info_dict if base_info_dict is not None else {}

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            base_info_dict={
                k: ObjBaseInfo.from_dict(v)
                for k, v in data.get("base_info_dict", {}).items()
            }
        )


@dataclass
class GetNMVIdListReq:
    """Request for getting non-motor vehicle ID list."""

    simulation_id: str = ""  # 仿真ID

    def __init__(self, simulation_id: str = ""):
        self.simulation_id = simulation_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(simulation_id=data.get("simulation_id", ""))


@dataclass
class GetNMVIdListRes:
    """Response for getting non-motor vehicle ID list."""

    list: List[str] = field(default_factory=list)  # 非机动车ID列表

    def __init__(self, list: List[str] = None):
        self.list = list if list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(list=data.get("list", []))


@dataclass
class GetNMVBaseInfoReq:
    """Request for getting non-motor vehicle base information."""

    simulation_id: str = ""
    nmv_id_list: List[str] = field(default_factory=list)

    def __init__(self, simulation_id: str = "", nmv_id_list: List[str] = None):
        self.simulation_id = simulation_id
        self.nmv_id_list = nmv_id_list if nmv_id_list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            nmv_id_list=data.get("nmv_id_list", []),
        )


@dataclass
class GetNMVBaseInfoRes:
    """Response for getting non-motor vehicle base information."""

    base_info_dict: Dict[str, ObjBaseInfo] = field(default_factory=dict)

    def __init__(self, base_info_dict: Dict[str, ObjBaseInfo] = None):
        self.base_info_dict = base_info_dict if base_info_dict is not None else {}

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            base_info_dict={
                k: ObjBaseInfo.from_dict(v)
                for k, v in data.get("base_info_dict", {}).items()
            }
        )


@dataclass
class SetVehiclePlanningInfoRes:
    """Response for setting vehicle planning information."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class SetVehicleControlInfoRes:
    """Response for setting vehicle control information."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class SetVehiclePositionRes:
    """Response for setting vehicle position."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class SetVehicleMovingInfoRes:
    """Response for setting vehicle moving information."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class SetVehicleBaseInfoRes:
    """Response for setting vehicle base information."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class SetVehicleRouteNavRes:
    """Response for setting vehicle route navigation."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class SetVehicleLinkNavRes:
    """Response for setting vehicle link navigation."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class SetVehicleLaneNavRes:
    """Response for setting vehicle lane navigation."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class SetVehicleDestinationRes:
    """Response for setting vehicle destination."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class SetPedPositionRes:
    """Response for setting pedestrian position."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class SetNMVPositionRes:
    """Response for setting non-motor vehicle position."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class GetStepSpawnIdListReq:
    """Request for getting step spawn ID list."""

    simulation_id: str = ""

    def __init__(self, simulation_id: str = ""):
        self.simulation_id = simulation_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(simulation_id=data.get("simulation_id", ""))


@dataclass
class GetStepSpawnIdListRes:
    """Response for getting step spawn ID list."""

    id_list: List[str] = field(default_factory=list)

    def __init__(self, id_list: List[str] = None):
        self.id_list = id_list if id_list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(id_list=data.get("id_list", []))


@dataclass
class GetParticipantBaseInfoReq:
    """Request for getting participant base information."""

    simulation_id: str = ""
    participant_id_list: List[str] = field(default_factory=list)

    def __init__(self, simulation_id: str = "", participant_id_list: List[str] = None):
        self.simulation_id = simulation_id
        self.participant_id_list = (
            participant_id_list if participant_id_list is not None else []
        )

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            participant_id_list=data.get("participant_id_list", []),
        )


@dataclass
class GetParticipantBaseInfoRes:
    """Response for getting participant base information."""

    base_info_dict: Dict[str, ObjBaseInfo] = field(default_factory=dict)

    def __init__(self, base_info_dict: Dict[str, ObjBaseInfo] = None):
        self.base_info_dict = base_info_dict if base_info_dict is not None else {}

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        base_info_dict = {}
        for k, v in data.get("base_info_dict", {}).items():
            base_info_dict[k] = ObjBaseInfo.from_dict(v)
        return cls(base_info_dict=base_info_dict)


@dataclass
class GetParticipantMovingInfoReq:
    """Request for getting participant moving information."""

    simulation_id: str = ""
    participant_id_list: List[str] = field(default_factory=list)

    def __init__(self, simulation_id: str = "", participant_id_list: List[str] = None):
        self.simulation_id = simulation_id
        self.participant_id_list = (
            participant_id_list if participant_id_list is not None else []
        )

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            participant_id_list=data.get("participant_id_list", []),
        )


@dataclass
class GetParticipantMovingInfoRes:
    """Response for getting participant moving information."""

    moving_info_dict: Dict[str, ObjMovingInfo] = field(default_factory=dict)

    def __init__(self, moving_info_dict: Dict[str, ObjMovingInfo] = None):
        self.moving_info_dict = moving_info_dict if moving_info_dict is not None else {}

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        moving_info_dict = {}
        for k, v in data.get("moving_info_dict", {}).items():
            moving_info_dict[k] = ObjMovingInfo.from_dict(v)
        return cls(moving_info_dict=moving_info_dict)


@dataclass
class GetSignalPlanReq:
    """Request for getting signal plan."""

    simulation_id: str = ""
    junction_id: str = ""

    def __init__(self, simulation_id: str = "", junction_id: str = ""):
        self.simulation_id = simulation_id
        self.junction_id = junction_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            junction_id=data.get("junction_id", ""),
        )


@dataclass
class GetSignalPlanRes_Stage:
    """Stage information for signal plan."""

    movement_ids: List[str] = field(default_factory=list)
    duration: int = 0

    def __init__(self, movement_ids: List[str] = None, duration: int = 0):
        self.movement_ids = movement_ids if movement_ids is not None else []
        self.duration = duration

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            movement_ids=data.get("movement_ids", []), duration=data.get("duration", 0)
        )


@dataclass
class GetSignalPlanRes:
    """Response for getting signal plan."""

    junction_id: str = ""
    cycle: int = 0
    offset: int = 0
    stages: List[GetSignalPlanRes_Stage] = field(default_factory=list)

    def __init__(
        self,
        junction_id: str = "",
        cycle: int = 0,
        offset: int = 0,
        stages: List[GetSignalPlanRes_Stage] = None,
    ):
        self.junction_id = junction_id
        self.cycle = cycle
        self.offset = offset
        self.stages = stages if stages is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            junction_id=data.get("junction_id", ""),
            cycle=data.get("cycle", 0),
            offset=data.get("offset", 0),
            stages=[
                GetSignalPlanRes_Stage.from_dict(stage)
                for stage in data.get("stages", [])
            ],
        )


@dataclass
class GetMovementListReq:
    """Request for getting movement list."""

    simulation_id: str = ""
    junction_id: str = ""

    def __init__(self, simulation_id: str = "", junction_id: str = ""):
        self.simulation_id = simulation_id
        self.junction_id = junction_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            junction_id=data.get("junction_id", ""),
        )


@dataclass
class GetMovementListRes:
    """Response for getting movement list."""

    list: List[Movement] = field(default_factory=list)

    def __init__(self, list: List[Movement] = None):
        self.list = list if list is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(list=[Movement.from_dict(item) for item in data.get("list", [])])


@dataclass
class NextStageReq:
    """Request for moving to next stage."""

    simulation_id: str = ""
    junction_id: str = ""

    def __init__(self, simulation_id: str = "", junction_id: str = ""):
        self.simulation_id = simulation_id
        self.junction_id = junction_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            junction_id=data.get("junction_id", ""),
        )


@dataclass
class NextStageRes:
    """Response for moving to next stage."""

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class GetParticipantPositionReq:
    """Request for getting participant position information."""

    simulation_id: str = ""
    participant_id_list: List[str] = field(default_factory=list)  # Maximum 1000 IDs

    def __init__(self, simulation_id: str = "", participant_id_list: List[str] = None):
        self.simulation_id = simulation_id
        self.participant_id_list = (
            participant_id_list if participant_id_list is not None else []
        )

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            participant_id_list=data.get("participant_id_list", []),
        )


@dataclass
class GetParticipantPositionRes:
    """Response for getting participant position information."""

    position_dict: Dict[str, Position] = field(default_factory=dict)

    def __init__(self, position_dict: Dict[str, Position] = None):
        self.position_dict = position_dict if position_dict is not None else {}

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        position_dict = {}
        for k, v in data.get("position_dict", {}).items():
            position_dict[k] = Position.from_dict(v)
        return cls(position_dict=position_dict)


class SensorType(IntEnum):
    """Sensor type enum."""

    UNKNOWN = 0
    CAMERA = 1
    LIDAR = 2
    RADAR = 3


@dataclass
class SensorErrorConfig:
    """Sensor error configuration."""

    location_sigma: float = 0.0  # Position variance
    phi_sigma: float = 0.0  # Heading angle variance
    size_sigma: float = 0.0  # Size variance
    velocity_sigma: float = 0.0  # Velocity variance

    def __init__(
        self,
        location_sigma: float = 0.0,
        phi_sigma: float = 0.0,
        size_sigma: float = 0.0,
        velocity_sigma: float = 0.0,
    ):
        self.location_sigma = location_sigma
        self.phi_sigma = phi_sigma
        self.size_sigma = size_sigma
        self.velocity_sigma = velocity_sigma

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            location_sigma=data.get("location_sigma", 0.0),
            phi_sigma=data.get("phi_sigma", 0.0),
            size_sigma=data.get("size_sigma", 0.0),
            velocity_sigma=data.get("velocity_sigma", 0.0),
        )


@dataclass
class SensorConfig:
    """Sensor configuration."""

    sensor_id: str = ""
    sensor_type: SensorType = SensorType.UNKNOWN
    detect_angle: float = 0.0  # Detection angle (sector central angle)
    detect_range: float = 0.0  # Detection range (sector radius)
    install_x: float = 0.0  # Longitudinal offset relative to vehicle center of mass
    install_y: float = 0.0  # Lateral offset relative to vehicle center of mass
    install_phi: float = 0.0  # Installation angle relative to vehicle heading
    sensor_error: Optional[SensorErrorConfig] = None  # Sensor perception error accuracy
    install_lon: float = 0.0  # Longitudinal offset relative to vehicle center of mass
    install_lat: float = 0.0  # Lateral offset relative to vehicle center of mass

    def __init__(
        self,
        sensor_id: str = "",
        sensor_type: SensorType = SensorType.UNKNOWN,
        detect_angle: float = 0.0,
        detect_range: float = 0.0,
        install_x: float = 0.0,
        install_y: float = 0.0,
        install_phi: float = 0.0,
        sensor_error: Optional[SensorErrorConfig] = None,
        install_lon: float = 0.0,
        install_lat: float = 0.0,
    ):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.detect_angle = detect_angle
        self.detect_range = detect_range
        self.install_x = install_x
        self.install_y = install_y
        self.install_phi = install_phi
        self.sensor_error = sensor_error
        self.install_lon = install_lon
        self.install_lat = install_lat

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            sensor_id=data.get("sensor_id", ""),
            sensor_type=SensorType(data.get("sensor_type", 0)),
            detect_angle=data.get("detect_angle", 0.0),
            detect_range=data.get("detect_range", 0.0),
            install_x=data.get("install_x", 0.0),
            install_y=data.get("install_y", 0.0),
            install_phi=data.get("install_phi", 0.0),
            sensor_error=SensorErrorConfig.from_dict(data.get("sensor_error")),
            install_lon=data.get("install_lon", 0.0),
            install_lat=data.get("install_lat", 0.0),
        )


@dataclass
class GetVehicleSensorConfigReq:
    """Request for getting vehicle sensor configuration."""

    simulation_id: str = ""
    vehicle_id: str = ""

    def __init__(self, simulation_id: str = "", vehicle_id: str = ""):
        self.simulation_id = simulation_id
        self.vehicle_id = vehicle_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            simulation_id=data.get("simulation_id", ""),
            vehicle_id=data.get("vehicle_id", ""),
        )


@dataclass
class GetVehicleSensorConfigRes:
    """Response for getting vehicle sensor configuration."""

    sensors_config: List[SensorConfig] = field(default_factory=list)

    def __init__(self, sensors_config: List[SensorConfig] = None):
        self.sensors_config = sensors_config if sensors_config is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            sensors_config=[
                SensorConfig.from_dict(x) for x in data.get("sensors_config", [])
            ]
        )


@dataclass
class LineString:
    points: List[Point] = field(default_factory=list)

    def __init__(self, points: List[Point] = None):
        self.points = points if points is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(points=[Point.from_dict(x) for x in data.get("points", [])])


@dataclass
class Polygon:
    points: List[Point] = field(default_factory=list)
    style: str = ""
    color: str = ""

    def __init__(self, points: List[Point] = None, style: str = "", color: str = ""):
        self.points = points if points is not None else []
        self.style = style
        self.color = color

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            points=[Point.from_dict(x) for x in data.get("points", [])],
            style=data.get("style", ""),
            color=data.get("color", ""),
        )


# 停车线
@dataclass
class StopLines:
    line: Optional[LineString] = None
    style: str = ""
    color: str = ""

    def __init__(
        self, line: Optional[LineString] = None, style: str = "", color: str = ""
    ):
        self.line = line
        self.style = style
        self.color = color

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            line=LineString.from_dict(data.get("line")),
            style=data.get("style", ""),
            color=data.get("color", ""),
        )


# 停车线
@dataclass
class LaneCenterLines:
    line: Optional[LineString] = None
    style: str = ""
    color: str = ""

    def __init__(
        self, line: Optional[LineString] = None, style: str = "", color: str = ""
    ):
        self.line = line
        self.style = style
        self.color = color

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            line=LineString.from_dict(data.get("line")),
            style=data.get("style", ""),
            color=data.get("color", ""),
        )


@dataclass
class LaneBoundary:
    line: Optional[LineString] = None
    style: str = ""
    color: str = ""

    def __init__(
        self, line: Optional[LineString] = None, style: str = "", color: str = ""
    ):
        self.line = line
        self.style = style
        self.color = color

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            line=LineString.from_dict(data.get("line")),
            style=data.get("style", ""),
            color=data.get("color", ""),
        )


@dataclass
class ReferenceLines:
    line: Optional[LineString] = None
    style: str = ""
    color: str = ""

    def __init__(
        self, line: Optional[LineString] = None, style: str = "", color: str = ""
    ):
        self.line = line
        self.style = style
        self.color = color

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            line=LineString.from_dict(data.get("line")),
            style=data.get("style", ""),
            color=data.get("color", ""),
        )


@dataclass
class LocalMap:
    lane_boundaries: List[LaneBoundary] = field(default_factory=list)
    junctions: List[Polygon] = field(default_factory=list)
    crosswalks: List[Polygon] = field(default_factory=list)
    traffic_light_colors: Dict[str, int] = field(default_factory=dict)
    stop_lines: List[StopLines] = field(default_factory=list)
    lane_center_lines: List[LaneCenterLines] = field(default_factory=list)
    virtual_polygons: List[Polygon] = field(default_factory=list)
    reference_lines: List[ReferenceLines] = field(default_factory=list)

    def __init__(
        self,
        lane_boundaries: List[LaneBoundary] = None,
        junctions: List[Polygon] = None,
        crosswalks: List[Polygon] = None,
        traffic_light_colors: Dict[str, int] = None,
        stop_lines: List[StopLines] = None,
        lane_center_lines: List[LaneCenterLines] = None,
        virtual_polygons: List[Polygon] = None,
        reference_lines: List[ReferenceLines] = None,
    ):
        self.lane_boundaries = lane_boundaries if lane_boundaries is not None else []
        self.junctions = junctions if junctions is not None else []
        self.crosswalks = crosswalks if crosswalks is not None else []
        self.traffic_light_colors = (
            traffic_light_colors if traffic_light_colors is not None else {}
        )
        self.stop_lines = stop_lines if stop_lines is not None else []
        self.lane_center_lines = (
            lane_center_lines if lane_center_lines is not None else []
        )
        self.virtual_polygons = virtual_polygons if virtual_polygons is not None else []
        self.reference_lines = reference_lines if reference_lines is not None else []

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            lane_boundaries=[
                LaneBoundary.from_dict(x) for x in data.get("lane_boundaries", [])
            ],
            junctions=[Polygon.from_dict(x) for x in data.get("junctions", [])],
            crosswalks=[Polygon.from_dict(x) for x in data.get("crosswalks", [])],
            traffic_light_colors=data.get("traffic_light_colors", {}),
            stop_lines=[StopLines.from_dict(x) for x in data.get("stop_lines", [])],
            lane_center_lines=[
                LaneCenterLines.from_dict(x) for x in data.get("lane_center_lines", [])
            ],
            virtual_polygons=[
                Polygon.from_dict(x) for x in data.get("virtual_polygons", [])
            ],
            reference_lines=[
                ReferenceLines.from_dict(x) for x in data.get("reference_lines", [])
            ],
        )


@dataclass
class SetVehicleRoadPerceptionInfoRes:

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class Obstacle:
    id: str = ""
    type: int = 0
    base_info: Optional[ObjBaseInfo] = None
    moving_info: Optional[ObjMovingInfo] = None
    position: Optional[Position] = None

    def __init__(
        self,
        id: str = "",
        type: int = 0,
        base_info: Optional[ObjBaseInfo] = None,
        moving_info: Optional[ObjMovingInfo] = None,
        position: Optional[Position] = None,
    ):
        self.id = id
        self.type = type
        self.base_info = base_info
        self.moving_info = moving_info
        self.position = position

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            id=data.get("id", ""),
            type=data.get("type", 0),
            base_info=ObjBaseInfo.from_dict(data.get("base_info")),
            moving_info=ObjMovingInfo.from_dict(data.get("moving_info")),
            position=Position.from_dict(data.get("position")),
        )


@dataclass
class SetVehicleObstaclePerceptionInfoRes:

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class SetVehicleExtraMetricsRes:

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class LocalPath:
    points: List[Point] = field(default_factory=list)
    prob: float = 0.0

    def __init__(self, points: List[Point] = None, prob: float = 0.0):
        self.points = points if points is not None else []
        self.prob = prob

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            points=[Point.from_dict(x) for x in data.get("points", [])],
            prob=data.get("prob", 0.0),
        )


@dataclass
class SetVehicleLocalPathsRes:

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls()


@dataclass
class GetIdcVehicleNavRes:

    link_path_nav: List[str] = field(default_factory=list)
    link_junction_nav: List[str] = field(default_factory=list)
    next_junction_id: str = ""
    dis_to_next_junction: float = 0.0
    next_movement_id: str = ""

    def __init__(
        self,
        link_path_nav: List[str] = None,
        link_junction_nav: List[str] = None,
        next_junction_id="",
        dis_to_next_junction=0.0,
        next_movement_id="",
    ):
        self.link_path_nav = link_path_nav if link_path_nav is not None else []
        self.link_junction_nav = (
            link_junction_nav if link_junction_nav is not None else []
        )
        self.next_junction_id = next_junction_id
        self.dis_to_next_junction = dis_to_next_junction
        self.next_movement_id = next_movement_id

    @classmethod
    def from_dict(cls, data: dict = None):
        if data is None:
            return None
        return cls(
            link_path_nav=data.get("link_path_nav", []),
            link_junction_nav=data.get("link_junction_nav", []),
            next_junction_id=data.get("next_junction_id", ""),
            dis_to_next_junction=data.get("dis_to_next_junction", 0.0),
            next_movement_id=data.get("next_movement_id", ""),
        )


@dataclass
class IdcStepRes:
    position: Position
    moving_info: ObjMovingInfo
    perception_infos: List[GetVehiclePerceptionInfoRes_PerceptionObj] = field(
        default_factory=list
    )
    reference_lines: List[ReferenceLine] = field(default_factory=list)
    navigation_info: Optional[NavigationInfo] = None
    step_res: StepRes = None

    @classmethod
    def from_dict(cls, data: dict = None):
        return cls(
            position=Position.from_dict(data.get("position", {})),
            moving_info=ObjMovingInfo.from_dict(data.get("moving_info", {})),
            perception_infos=[
                GetVehiclePerceptionInfoRes_PerceptionObj.from_dict(obj)
                for obj in data.get("perception_infos", [])
            ],
            reference_lines=[
                ReferenceLine.from_dict(obj) for obj in data.get("reference_lines", [])
            ],
            navigation_info=NavigationInfo.from_dict(data.get("navigation_info", {})),
            step_res=StepRes.from_dict(data.get("step_res", {})),
        )
