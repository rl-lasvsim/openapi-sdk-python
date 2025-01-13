"""Tests for the SimRecord API."""
from typing import Tuple

import os
import pytest

from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator import Simulator


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
def scenario_info(client: Client, task_record_ids: Tuple[int, int]) -> Tuple[str, str]:
    """Get scenario ID and version for testing."""
    task_id, record_id = task_record_ids
    res = client.process_task.get_record_scenario(task_id, record_id)
    return res.scen_id, res.scen_ver


@pytest.fixture
def sim_record_test_data(client: Client, scenario_info: Tuple[str, str]) -> Tuple[str, str, str]:
    """Set up test data for sim record tests."""
    # Get record IDs
    scen_id, scen_ver = scenario_info
    record_res = client.sim_record.get_record_ids(scen_id, scen_ver)
    assert len(record_res.ids) > 0, "record list should not be empty"

    # Get record info
    record_id = record_res.ids[0]

    return scen_id, scen_ver, record_id,


def test_get_record_ids(client: Client, scenario_info: Tuple[str, str]):
    """Test getting record IDs."""
    scen_id, scen_ver = scenario_info

    # Test getting record IDs
    res = client.sim_record.get_record_ids(scen_id, scen_ver)
    assert res.ids is not None, "record list should not be None"
    assert len(res.ids) > 0, "record list should not be empty"

    # Test with invalid inputs
    with pytest.raises(Exception):
        client.sim_record.get_record_ids("", "")

    # with pytest.raises(Exception):
    res = client.sim_record.get_record_ids("invalid_id", "invalid_ver")
    assert len(res.ids) == 0, "record list should be empty"


def test_get_track_results(client: Client, sim_record_test_data: Tuple[str, str, str, str]):
    """Test getting track results."""
    _, _, record_id = sim_record_test_data
    assert record_id is not None, "record ID should not be None"
    assert record_id != "", "record ID should not be empty"

    # Test getting track results
    res = client.sim_record.get_track_results(record_id, "")
    assert res is not None, "track results should not be None"

    # Test with invalid inputs
    with pytest.raises(Exception):
        client.sim_record.get_track_results("", "")


def test_get_sensor_results(client: Client, sim_record_test_data: Tuple[str, str, str, str]):
    """Test getting sensor results."""
    _, _, record_id = sim_record_test_data

    # Test getting sensor results
    res = client.sim_record.get_sensor_results(record_id, "")
    assert res is not None, "sensor results should not be None"

    # Test with invalid inputs
    with pytest.raises(Exception):
        client.sim_record.get_sensor_results("", "")


def test_get_step_results(client: Client, sim_record_test_data: Tuple[str, str, str, str]):
    """Test getting step results."""
    _, _, record_id = sim_record_test_data

    # Test getting step results
    res = client.sim_record.get_step_results(record_id, "")
    assert res is not None, "step results should not be None"


def test_get_path_results(client: Client, sim_record_test_data: Tuple[str, str, str, str]):
    """Test getting path results."""
    _, _, record_id = sim_record_test_data

    # Test getting path results
    res = client.sim_record.get_path_results(record_id, "")
    assert res is not None, "path results should not be None"


def test_get_reference_line_results(client: Client, sim_record_test_data: Tuple[str, str, str, str]):
    """Test getting reference line results."""
    _, _, record_id = sim_record_test_data

    # Test getting reference line results
    res = client.sim_record.get_reference_line_results(record_id, "")
    assert res is not None, "reference line results should not be None"


def test_sim_record_results_data_validation(client: Client, sim_record_test_data: Tuple[str, str, str, str]):
    """Test sim record results data validation."""
    _, _, record_id = sim_record_test_data

    # Test track results validation
    track_res = client.sim_record.get_track_results(record_id, "")
    assert track_res is not None

    # Test sensor results validation
    sensor_res = client.sim_record.get_sensor_results(record_id, "")
    assert sensor_res is not None

    # Test step results validation
    step_res = client.sim_record.get_step_results(record_id, "")
    assert step_res is not None

    # Test path results validation
    path_res = client.sim_record.get_path_results(record_id, "")
    assert path_res is not None
