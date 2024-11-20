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

## Features

- Easy-to-use client interface
- Comprehensive simulation control
- Vehicle state monitoring and control
- Support for pedestrians and non-motorized vehicles
- Training task management
- Map resource handling

## Main Components

- `Client`: Main entry point for the SDK
- `HttpConfig`: Configuration for API endpoints and authentication
- `SimulatorConfig`: Configuration for simulation scenarios
- `Simulator`: Core simulation control interface
- `TrainTask`: Training task management
- `Resources`: Map and resource handling

## Available Methods

### Simulation Control
- `step()`: Advance simulation by one step
- `stop()`: Stop the simulation

### Vehicle Control
- `get_vehicle_id_list()`: Get all vehicle IDs
- `get_vehicle_position()`: Get vehicle positions
- `set_vehicle_position()`: Set vehicle position
- `set_vehicle_control_info()`: Set vehicle control parameters
- `set_vehicle_moving_info()`: Set vehicle movement parameters
- `get_vehicle_base_info()`: Get vehicle basic information

### Pedestrian Control
- `get_ped_id_list()`: Get all pedestrian IDs
- `get_ped_base_info()`: Get pedestrian information
- `set_ped_position()`: Set pedestrian position

### Non-motorized Vehicle Control
- `get_nmv_id_list()`: Get all non-motorized vehicle IDs
- `get_nmv_base_info()`: Get non-motorized vehicle information
- `set_nmv_position()`: Set non-motorized vehicle position

## Requirements

- Python >= 3.0
- requests >= 2.25.0

## License

This project is licensed under the terms of the MIT license.

## Support

For bug reports and feature requests, please use the [GitHub Issues](https://github.com/risenlighten-qianxing/openapi-sdk-python/issues) page.