"""Tests for the Resources API."""
from typing import Tuple

import pytest

from lasvsim_openapi.client import Client


def test_get_hd_map(client: Client, scenario_info: Tuple[str, str]):
    """Test getting HD map."""
    scen_id, scen_ver = scenario_info

    # Test getting HD map
    map_res = client.resources.get_hd_map(scen_id, scen_ver)
    assert map_res is not None, "HD map response should not be None"
    assert map_res.data is not None, "HD map data should not be None"
    assert map_res.data.junctions is not None, "junctions should not be None"


def test_get_hd_map_with_invalid_inputs(client: Client):
    """Test getting HD map with invalid inputs."""
    # Test with empty scenario ID
    with pytest.raises(Exception):
        client.resources.get_hd_map("", "version")

    # Test with empty version
    with pytest.raises(Exception):
        client.resources.get_hd_map("scen_id", "")

    # Test with invalid scenario ID
    with pytest.raises(Exception):
        client.resources.get_hd_map("invalid_scen_id", "version")


def test_get_hd_map_data_validation(client: Client, scenario_info: Tuple[str, str]):
    """Test HD map data validation."""
    scen_id, scen_ver = scenario_info

    # Get HD map
    map_res = client.resources.get_hd_map(scen_id, scen_ver)
    assert map_res is not None

    # Validate basic fields
    assert map_res.data.header is not None, "map header should not be None"
    if map_res.data.header is not None:
        assert map_res.data.header.center_point is not None, "map center point should not be None"

    # Validate junction data
    if len(map_res.data.junctions) > 0:
        junction = map_res.data.junctions[0]
        assert junction.id, "junction ID should not be empty"

        # Validate junction shape
        if junction.shape is not None and len(junction.shape.points) > 0:
            point = junction.shape.points[0]
            assert point.x is not None, "junction shape point X should not be None"
            assert point.y is not None, "junction shape point Y should not be None"

        # Validate junction internal roads
        if len(junction.links) > 0:
            link = junction.links[0]
            assert link.id, "junction link ID should not be empty"
