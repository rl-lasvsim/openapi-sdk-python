pytest tests/unittest/test_simulator.py::test_get_vehicle_planning_info

pytest tests/unittest/test_sim_record.py::test_get_sensor_results
pytest tests/unittest/test_simulator.py::test_set_vehicle_obstacle_perception_info

tests/unittest/test_simulator.py::test_set_vehicle_destination
tests/unittest/test_simulator.py::test_set_vehicle_road_perception_info

def test_set_vehicle_obstacle_perception_info(simulator: Simulator):
    """Test setting vehicle obstacle perception info."""
    # First get vehicle ID list
    res = simulator.get_vehicle_id_list()
    assert len(res.list) > 0, "not found vehicle id list"

    # Create test obstacles
    obstacles = [
        Obstacle(
            id="test_obstacle",
            type=1,
            position=Position(
                point = Point(
                    x = 0,
                    y = 0,
                    z = 0
                ),
                heading=0,
                dis_to_lane_end=1,
                s=0,
                t=0,
            ),
            base_info= ObjBaseInfo(
                
            ),
            moving_info= ObjMovingInfo(
                u=10.0,
            )
        )
    ]

    # Test setting vehicle obstacle perception info
    obstacle_perception_res = simulator.set_vehicle_obstacle_perception_info(res.list[0], obstacles)
    assert obstacle_perception_res is not None, "obstacle perception response should not be None"
