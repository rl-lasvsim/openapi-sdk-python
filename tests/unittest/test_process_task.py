"""Tests for the ProcessTask API."""
from typing import Tuple

import pytest

from lasvsim_openapi.client import Client


def test_process_task_get_record_scenario(client: Client, task_record_ids: Tuple[int, int]):
    """Test getting record scenario."""
    task_id, record_id = task_record_ids

    # Test getting record scenario
    res = client.process_task.get_record_scenario(task_id, record_id)
    assert res.scen_id, "scenario ID should not be empty"
    assert res.scen_ver, "scenario version should not be empty"


def test_process_task_get_task_record_ids(client: Client, task_record_ids: Tuple[int, int]):
    """Test getting task record IDs."""
    task_id, _ = task_record_ids

    # Test getting task record IDs
    res = client.process_task.get_task_record_ids(task_id)
    assert res.record_ids is not None, "record ID list should not be None"


def test_process_task_copy_record(client: Client, task_record_ids: Tuple[int, int]):
    """Test copying record."""
    task_id, record_id = task_record_ids

    # Test copying record
    res = client.process_task.copy_record(task_id, record_id)
    assert res.new_record_id != 0, "copied record ID should not be zero"

    # Verify the copied record exists
    records = client.process_task.get_task_record_ids(task_id)
    found = False
    for rid in records.record_ids:
        if rid == res.new_record_id:
            found = True
            break
    assert found, "copied record should exist in task records"

    # Test copying with invalid task ID
    with pytest.raises(Exception):
        client.process_task.copy_record(0, record_id)


def test_process_task_invalid_inputs(client: Client):
    """Test process task with invalid inputs."""
    # Test invalid task ID
    with pytest.raises(Exception):
        client.process_task.get_task_record_ids(0)

    # Test invalid record ID
    with pytest.raises(Exception):
        client.process_task.get_record_scenario(0, 0)
