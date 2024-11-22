# Qianxing OpenAPI SDK for Python

A Python SDK for interacting with Qianxing's simulation platform. This package provides a simple and intuitive way to control and monitor simulations for autonomous driving scenarios.

## Installation

You can install the package directly from PyPI:

```bash
pip install qianxing-openapi
```

## Quick Start

Here's a simple example of how to use the SDK:

```python
from qianxing_openapi.client import Client
from qianxing_openapi.http_client import HttpConfig
from qianxing_openapi.simulator import SimulatorConfig
from qianxing_openapi.request_model import Point

# Initialize the client
client = Client(
    HttpConfig(
        token="your_token_here",
        endpoint="your_endpoint_here"
    )
)

# Get available scenes from training task
res = client.train_task.get_scene_id_list(task_id)
print(f"Available scenes: {res}")

# Create a simulator instance
simulator = client.init_simulator_from_config(
    SimulatorConfig(
        scenario_id=res.scene_id_list[0],
        scenario_version=res.scene_version_list[0]
    )
)

# Run simulation steps
for i in range(10):
    step_res = simulator.step()
    print(f"Step {i} result: {step_res}")

# Get vehicle information
vehicle_ids = simulator.get_vehicle_id_list()
print(f"Vehicle IDs: {vehicle_ids}")

# Control vehicle movement
simulator.set_vehicle_control_info(
    vehicle_id="test_vehicle_1", 
    ste_wheel=1.2,
    lon_acc=1.1
)

# Set vehicle position
simulator.set_vehicle_position(
    vehicle_id="test_vehicle_1",
    point=Point(x=-8.75, y=-537.0316, z=0)
)

# Stop the simulation
simulator.stop()
```

## Available APIs

### Simulator APIs

#### Simulation Control
- `init_from_config(sim_config)`: Initialize simulator from configuration
- `init_from_sim(simulation_id, addr)`: Initialize simulator from existing simulation
- `step()`: Advance simulation by one step
- `stop()`: Stop the simulation
- `reset(reset_traffic_flow)`: Reset the simulation to initial state, optionally reset traffic flow

#### Vehicle APIs
- `get_vehicle_id_list()`: Get all vehicle IDs
- `get_test_vehicle_id_list()`: Get test vehicle IDs
- `get_vehicle_base_info(id_list)`: Get vehicle basic information
- `get_vehicle_position(id_list)`: Get vehicle positions
- `get_vehicle_moving_info(id_list)`: Get vehicle movement information
- `get_vehicle_control_info(id_list)`: Get vehicle control parameters
- `get_vehicle_perception_info(vehicle_id)`: Get vehicle perception information
- `get_vehicle_reference_lines(vehicle_id)`: Get available reference lines
- `get_vehicle_planning_info(vehicle_id)`: Get vehicle planning information
- `get_vehicle_navigation_info(vehicle_id)`: Get vehicle navigation information
- `get_vehicle_collision_status(vehicle_id)`: Check vehicle collision status
- `get_vehicle_target_speed(vehicle_id)`: Get vehicle target speed
- `set_vehicle_position(vehicle_id, point, phi)`: Set vehicle position and heading angle
- `set_vehicle_control_info(vehicle_id, ste_wheel, lon_acc)`: Set vehicle control parameters
- `set_vehicle_planning_info(vehicle_id, planning_path)`: Set vehicle planning path
- `set_vehicle_moving_info(vehicle_id, u, v, w, u_acc, v_acc, w_acc)`: Set vehicle movement parameters
- `set_vehicle_base_info(vehicle_id, base_info)`: Set vehicle basic information
- `set_vehicle_link_nav(vehicle_id, link_nav)`: Set vehicle link navigation information
- `set_vehicle_destination(vehicle_id, destination)`: Set vehicle destination point

#### Traffic Light APIs
- `get_current_stage(junction_id)`: Get current traffic light stage
- `get_movement_signal(movement_id)`: Get movement signal light color
- `get_signal_plan(junction_id)`: Get traffic light timing plan
- `get_movement_list(junction_id)`: Get movement list for junction

#### Pedestrian APIs
- `get_ped_id_list()`: Get all pedestrian IDs
- `get_ped_base_info(ped_id_list)`: Get pedestrian basic information
- `set_ped_position(ped_id, point, phi)`: Set pedestrian position and heading angle

#### Non-motorized Vehicle APIs
- `get_nmv_id_list()`: Get all non-motorized vehicle IDs
- `get_nmv_base_info(nmv_id_list)`: Get non-motorized vehicle basic information
- `set_nmv_position(nmv_id, point, phi)`: Set non-motorized vehicle position and heading angle

### Training Task APIs
- `get_scene_id_list(task_id)`: Get list of available scenes for a training task

### Resource APIs
- `get_map(asset_id, asset_version)`: Get map data for a specific asset

## Requirements

- Python >= 3.0
- requests >= 2.25.0

## License

This project is licensed under the terms of the MIT license.

## Support

For bug reports and feature requests, please use the [GitHub Issues](https://github.com/risenlighten-qianxing/openapi-sdk-python/issues) page.