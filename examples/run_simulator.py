#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator import SimulatorConfig
from lasvsim_openapi.request_model import Point, ObjBaseInfo
from lasvsim_openapi.qxmap_model import Qxmap
import os


def main():
    print("Running simulator example...\n")
    print(Qxmap({}))
    # Initialize the client
    api_client = Client(
        HttpConfig(
            token=os.getenv("QX_TOKEN"),
            endpoint=os.getenv("QX_ENDPOINT"),
        )
    )

    # Get scene list from training task
    res = api_client.train_task.get_scene_id_list(168)
    print(f"Training task scene list: {res}\n")

    # Initialize simulator with first scene
    simulator_instance = api_client.init_simulator_from_config(
        SimulatorConfig(
            scen_id=res.scene_id_list[0],
            scen_ver=res.scene_version_list[0]
        )
    )

    print(
        f"Initialized simulator with ID: {simulator_instance.simulation_id}\n")

    # Run simulation steps
    for i in range(10):
        step_res = simulator_instance.step()
        print(f"Step {i} result: {step_res}")

    # Get vehicle information
    vehicle_ids = simulator_instance.get_vehicle_id_list()
    print(f"Vehicle IDs: {vehicle_ids}\n")

    # Stop simulation
    res = simulator_instance.stop()
    print(f"Stopped simulator: {res}\n")


if __name__ == "__main__":
    main()
