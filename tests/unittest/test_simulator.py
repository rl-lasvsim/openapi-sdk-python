"""Tests for the Simulator API."""
from typing import Tuple

import pytest

from lasvsim_openapi.client import Client
from lasvsim_openapi.simulator import Simulator
from lasvsim_openapi.simulator_model import Point, ObjBaseInfo, DynamicInfo


def test_simulator_initialization(simulator: Simulator):
    """Test simulator initialization."""
    assert simulator is not None, "simulator should be initialized"


def test_get_vehicle_id_list(simulator: Simulator):
    """Test getting vehicle ID list."""
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0, "not found vehicle id list"


def test_get_vehicle_moving_info(simulator: Simulator):
    """Test getting vehicle moving info."""
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0, "not found vehicle id list"

    veh_moving_infos = simulator.get_vehicle_moving_info([res.list[0]])
    veh_moving_info = veh_moving_infos.moving_info_dict[res.list[0]]
    assert veh_moving_info is not None, "not found vehicle moving info"


def test_set_vehicle_moving_info(simulator: Simulator):
    """Test setting vehicle moving info."""
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0, "not found vehicle id list"

    veh_moving_infos = simulator.get_vehicle_moving_info([res.list[0]])
    veh_moving_info = veh_moving_infos.moving_info_dict[res.list[0]]
    assert veh_moving_info is not None, "not found vehicle moving info"

    # Set vehicle moving info with current values
    simulator.set_vehicle_moving_info(
        res.list[0],
        u=veh_moving_info.u,
        v=veh_moving_info.v,
        w=veh_moving_info.w,
        u_acc=veh_moving_info.u_acc,
        v_acc=veh_moving_info.v_acc,
        w_acc=veh_moving_info.w_acc
    )


def test_simulator_step(simulator: Simulator):
    """Test simulator step."""
    res = simulator.step()
    assert res is not None, "step response should not be None"


def test_simulator_stop(simulator: Simulator):
    """Test simulator stop."""
    res = simulator.stop()
    assert res is not None, "stop response should not be None"


def test_simulator_reset(simulator: Simulator):
    """Test simulator reset."""
    res = simulator.reset(False)
    assert res is not None, "reset response should not be None"


def test_get_current_stage(simulator: Simulator, client: Client, scenario_info: Tuple[str, str]):
    """Test getting current stage."""
    # Get HD map to find junction ID
    scen_id, scen_ver = scenario_info
    hd_map = client.resources.get_hd_map(scen_id, scen_ver)
    assert hd_map is not None, "hd map should not be nil"
    assert len(hd_map.data.junctions) > 0, "not found junction"

    # Test getting current stage
    with pytest.raises(Exception):
        stage_res = simulator.get_current_stage(hd_map.data.junctions[0].id)
        assert stage_res is not None


def test_get_movement_signal(simulator: Simulator, client: Client, scenario_info: Tuple[str, str]):
    """Test getting movement signal."""
    # Get HD map to find junction ID
    scen_id, scen_ver = scenario_info
    hd_map = client.resources.get_hd_map(scen_id, scen_ver)
    assert hd_map is not None, "hd map should not be nil"
    assert len(hd_map.data.junctions) > 0, "not found junction"

    # Get movement list for the junction
    movement_list_res = simulator.get_movement_list(hd_map.data.junctions[0].id)
    assert movement_list_res is not None
    if len(movement_list_res.list) == 0:
        return
    
    # Then test getting movement signal
    signal_res = simulator.get_movement_signal(movement_list_res.list[0].id)
    assert signal_res is not None


def test_get_signal_plan(simulator: Simulator, client: Client, scenario_info: Tuple[str, str]):
    """Test getting signal plan."""
    # Get HD map to find junction ID
    scen_id, scen_ver = scenario_info
    hd_map = client.resources.get_hd_map(scen_id, scen_ver)
    assert hd_map is not None, "hd map should not be nil"
    assert len(hd_map.data.junctions) > 0, "not found junction"

    # Test getting signal plan
    with pytest.raises(Exception):
        plan_res = simulator.get_signal_plan(hd_map.data.junctions[0].id)
        assert plan_res is not None


def test_get_movement_list(simulator: Simulator, client: Client, scenario_info: Tuple[str, str]):
    """Test getting movement list."""
    # Get HD map to find junction ID
    scen_id, scen_ver = scenario_info
    hd_map = client.resources.get_hd_map(scen_id, scen_ver)
    assert hd_map is not None, "hd map should not be nil"
    assert len(hd_map.data.junctions) > 0, "not found junction"

    # Test getting movement list
    movement_list_res = simulator.get_movement_list(hd_map.data.junctions[0].id)
    assert movement_list_res is not None


def test_get_vehicle_base_info(simulator: Simulator):
    """Test getting vehicle base info."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Then test getting vehicle base info
    base_info_res = simulator.get_vehicle_base_info([res.list[0]])
    assert base_info_res is not None


def test_get_vehicle_position(simulator: Simulator):
    """Test getting vehicle position."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Then test getting vehicle position
    pos_res = simulator.get_vehicle_position([res.list[0]])
    assert pos_res is not None


def test_get_vehicle_control_info(simulator: Simulator):
    """Test getting vehicle control info."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Then test getting vehicle control info
    control_res = simulator.get_vehicle_control_info([res.list[0]])
    assert control_res is not None


def test_get_vehicle_perception_info(simulator: Simulator):
    """Test getting vehicle perception info."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Then test getting vehicle perception info
    perception_res = simulator.get_vehicle_perception_info(res.list[0])
    assert perception_res is not None


def test_get_vehicle_reference_lines(simulator: Simulator):
    """Test getting vehicle reference lines."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Then test getting vehicle reference lines
    ref_lines_res = simulator.get_vehicle_reference_lines(res.list[0])
    assert ref_lines_res is not None


def test_get_vehicle_planning_info(simulator: Simulator):
    """Test getting vehicle planning info."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Then test getting vehicle planning info
    planning_res = simulator.get_vehicle_planning_info(res.list[0])
    assert planning_res is not None


def test_get_vehicle_navigation_info(simulator: Simulator):
    """Test getting vehicle navigation info."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Then test getting vehicle navigation info
    nav_res = simulator.get_vehicle_navigation_info(res.list[0])
    assert nav_res is not None


def test_get_vehicle_collision_status(simulator: Simulator):
    """Test getting vehicle collision status."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Then test getting vehicle collision status
    collision_res = simulator.get_vehicle_collision_status(res.list[0])
    assert collision_res is not None


def test_get_vehicle_target_speed(simulator: Simulator):
    """Test getting vehicle target speed."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Then test getting vehicle target speed
    speed_res = simulator.get_vehicle_target_speed(res.list[0])
    assert speed_res is not None


def test_set_vehicle_planning_info(simulator: Simulator):
    """Test setting vehicle planning info."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Create test planning path
    planning_path = [Point(x=0.0, y=0.0, z=0.0)]

    # Test setting vehicle planning info
    planning_res = simulator.set_vehicle_planning_info(res.list[0], planning_path)
    assert planning_res is not None


def test_set_vehicle_control_info(simulator: Simulator):
    """Test setting vehicle control info."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Test setting vehicle control info
    control_res = simulator.set_vehicle_control_info(res.list[0], ste_wheel=0.0, lon_acc=0.0)
    assert control_res is not None


def test_set_vehicle_position(simulator: Simulator):
    """Test setting vehicle position."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Test setting vehicle position
    pos_res = simulator.set_vehicle_position(res.list[0], Point(x=0.0, y=0.0, z=0.0), phi=0.0)
    assert pos_res is not None


def test_set_vehicle_base_info(simulator: Simulator):
    """Test setting vehicle base info."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Create test base info
    base_info = ObjBaseInfo(
        length=4.5,
        width=1.8,
        height=1.5,
        weight=2.7
    )

    # Create test dynamic info
    dynamic_info = DynamicInfo(
        front_wheel_stiffness=0.0,
        rear_wheel_stiffness=0.0,
        front_axle_to_center=0.0,
        rear_axle_to_center=0.0,
        yaw_moment_of_inertia=0.0
    )

    # Test setting vehicle base info
    base_info_res = simulator.set_vehicle_base_info(res.list[0], base_info, dynamic_info)
    assert base_info_res is not None


def test_set_vehicle_destination(simulator: Simulator):
    """Test setting vehicle destination."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Get vehicle position
    pos_res = simulator.get_vehicle_position([res.list[0]])
    assert pos_res is not None

    # Create destination point slightly offset from current position
    current_pos = pos_res.position_dict[res.list[0]]
    destination = Point(
        x=current_pos.point.x + 10.0,
        y=current_pos.point.y + 10.0,
        z=current_pos.point.z
    )

    # Test setting vehicle destination
    dest_res = simulator.set_vehicle_destination(res.list[0], destination)
    assert dest_res is not None


def test_get_ped_id_list(simulator: Simulator):
    """Test getting pedestrian ID list."""
    res = simulator.get_ped_id_list()
    assert res is not None


def test_get_ped_base_info(simulator: Simulator):
    """Test getting pedestrian base info."""
    res = simulator.get_ped_id_list()
    if len(res.list) > 0:
        base_info_res = simulator.get_ped_base_info([res.list[0]])
        assert base_info_res is not None


def test_set_ped_position(simulator: Simulator):
    """Test setting pedestrian position."""
    res = simulator.get_ped_id_list()
    if len(res.list) > 0:
        pos_res = simulator.set_ped_position(res.list[0], Point(x=0.0, y=0.0, z=0.0), phi=0.0)
        assert pos_res is not None


def test_get_nmv_id_list(simulator: Simulator):
    """Test getting non-motor vehicle ID list."""
    res = simulator.get_nmv_id_list()
    assert res is not None


def test_get_nmv_base_info(simulator: Simulator):
    """Test getting non-motor vehicle base info."""
    res = simulator.get_nmv_id_list()
    if len(res.list) > 0:
        base_info_res = simulator.get_nmv_base_info([res.list[0]])
        assert base_info_res is not None


def test_set_nmv_position(simulator: Simulator):
    """Test setting non-motor vehicle position."""
    res = simulator.get_nmv_id_list()
    if len(res.list) > 0:
        pos_res = simulator.set_nmv_position(res.list[0], Point(x=0.0, y=0.0, z=0.0), phi=0.0)
        assert pos_res is not None


def test_get_step_spawn_id_list(simulator: Simulator):
    """Test getting step spawn ID list."""
    res = simulator.get_step_spawn_id_list()
    assert res is not None


def test_get_participant_base_info(simulator: Simulator):
    """Test getting participant base info."""
    # First get vehicle ID list as participants
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Then test getting participant base info
    base_info_res = simulator.get_participant_base_info([res.list[0]])
    assert base_info_res is not None


def test_get_participant_moving_info(simulator: Simulator):
    """Test getting participant moving info."""
    # First get vehicle ID list as participants
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Then test getting participant moving info
    moving_info_res = simulator.get_participant_moving_info([res.list[0]])
    assert moving_info_res is not None


def test_get_participant_position(simulator: Simulator):
    """Test getting participant position."""
    # First get vehicle ID list as participants
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Then test getting participant position
    pos_res = simulator.get_participant_position([res.list[0]])
    assert pos_res is not None


def test_get_vehicle_moving_info_with_invalid_id(simulator: Simulator):
    """Test getting vehicle moving info with invalid ID."""
    res = simulator.get_vehicle_moving_info(["invalid_id"])
    assert len(res.moving_info_dict) == 0


def test_get_vehicle_moving_info_with_empty_list(simulator: Simulator):
    """Test getting vehicle moving info with empty list."""
    res = simulator.get_vehicle_moving_info([])
    assert len(res.moving_info_dict) == 0


def test_set_vehicle_moving_info_with_boundary_values(simulator: Simulator):
    """Test setting vehicle moving info with boundary values."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Test with zero values
    simulator.set_vehicle_moving_info(res.list[0], u=0.0, v=0.0, w=0.0, u_acc=0.0, v_acc=0.0, w_acc=0.0)

    # Test with large values
    simulator.set_vehicle_moving_info(res.list[0], u=1000.0, v=1000.0, w=1000.0, u_acc=1000.0, v_acc=1000.0, w_acc=1000.0)

    # Test with negative values
    simulator.set_vehicle_moving_info(res.list[0], u=-1.0, v=-1.0, w=-1.0, u_acc=-1.0, v_acc=-1.0, w_acc=-1.0)


def test_set_vehicle_position_with_boundary_values(simulator: Simulator):
    """Test setting vehicle position with boundary values."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Test with zero values
    simulator.set_vehicle_position(res.list[0], Point(x=0.0, y=0.0, z=0.0), phi=0.0)

    # Test with large values
    simulator.set_vehicle_position(res.list[0], Point(x=1000.0, y=1000.0, z=1000.0), phi=3.14)

    # Test with negative values
    simulator.set_vehicle_position(res.list[0], Point(x=-1000.0, y=-1000.0, z=-1000.0), phi=-3.14)


def test_set_vehicle_control_info_with_boundary_values(simulator: Simulator):
    """Test setting vehicle control info with boundary values."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0

    # Test with zero values
    simulator.set_vehicle_control_info(res.list[0], ste_wheel=0.0, lon_acc=0.0)

    # Test with large values
    simulator.set_vehicle_control_info(res.list[0], ste_wheel=1.0, lon_acc=10.0)

    # Test with negative values
    simulator.set_vehicle_control_info(res.list[0], ste_wheel=-1.0, lon_acc=-10.0)


def test_simulator_step_sequence(simulator: Simulator):
    """Test simulator step sequence."""
    # Step multiple times
    for _ in range(5):
        res = simulator.step()
        assert res is not None


def test_reset_after_multiple_steps(simulator: Simulator):
    """Test resetting simulator after multiple steps."""
    # Get initial vehicle positions
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0
    initial_pos = simulator.get_vehicle_position([res.list[0]])

    # Step multiple times
    for _ in range(5):
        simulator.step()

    # Get positions after steps
    after_steps_pos = simulator.get_vehicle_position([res.list[0]])

    # Reset simulator
    simulator.reset(True)

    # Get positions after reset
    after_reset_pos = simulator.get_vehicle_position([res.list[0]])

    # Verify positions are different after steps but same after reset
    assert initial_pos != after_steps_pos


def test_ped_position_with_boundary_values(simulator: Simulator):
    """Test setting pedestrian position with boundary values."""
    res = simulator.get_ped_id_list()
    if len(res.list) > 0:
        # Test with zero values
        simulator.set_ped_position(res.list[0], Point(x=0.0, y=0.0, z=0.0), phi=0.0)

        # Test with large values
        simulator.set_ped_position(res.list[0], Point(x=1000.0, y=1000.0, z=1000.0), phi=3.14)

        # Test with negative values
        simulator.set_ped_position(res.list[0], Point(x=-1000.0, y=-1000.0, z=-1000.0), phi=-3.14)


def test_nmv_position_with_boundary_values(simulator: Simulator):
    """Test setting non-motor vehicle position with boundary values."""
    res = simulator.get_nmv_id_list()
    if len(res.list) > 0:
        # Test with zero values
        simulator.set_nmv_position(res.list[0], Point(x=0.0, y=0.0, z=0.0), phi=0.0)

        # Test with large values
        simulator.set_nmv_position(res.list[0], Point(x=1000.0, y=1000.0, z=1000.0), phi=3.14)

        # Test with negative values
        simulator.set_nmv_position(res.list[0], Point(x=-1000.0, y=-1000.0, z=-1000.0), phi=-3.14)


def test_participant_info_with_empty_lists(simulator: Simulator):
    """Test getting participant info with empty lists."""
    # Test base info
    res = simulator.get_participant_base_info([])
    assert len(res.base_info_dict) == 0

    # Test moving info
    res = simulator.get_participant_moving_info([])
    assert len(res.moving_info_dict) == 0

    # Test position
    res = simulator.get_participant_position([])
    assert len(res.position_dict) == 0
