"""Test configuration and fixtures."""
import os
from typing import Tuple

import pytest

from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator import Simulator
from lasvsim_openapi.simulator_model import SimulatorConfig


@pytest.fixture
def client() -> Client:
    """Create a client instance for testing."""
    return Client(HttpConfig(
        token=os.getenv("QX_TOKEN"),
        endpoint=os.getenv("QX_ENDPOINT")
    ))


@pytest.fixture
def task_record_ids() -> Tuple[int, int]:
    """Get task and record IDs from environment variables."""
    task_id = int(os.getenv("QX_TASK_ID"))
    record_id = int(os.getenv("QX_RECORD_ID"))
    return task_id, record_id


@pytest.fixture
def simulator(client: Client, task_record_ids: Tuple[int, int]) -> Simulator:
    """Create a simulator instance for testing."""
    task_id, record_id = task_record_ids
    res = client.process_task.get_record_scenario(task_id, record_id)
    simulator = client.init_simulator_from_config(SimulatorConfig(
        scen_id=res.scen_id,
        scen_ver=res.scen_ver
    ))
    yield simulator
    try:
        simulator.stop()
    except Exception:
        pass

@pytest.fixture
def scenario_info(client: Client, task_record_ids: Tuple[int, int]) -> Tuple[str, str]:
    """Get scenario ID and version for testing."""
    task_id, record_id = task_record_ids
    res = client.process_task.get_record_scenario(task_id, record_id)
    return res.scen_id, res.scen_ver
