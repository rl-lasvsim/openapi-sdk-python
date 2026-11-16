"""Offline tests for the seed get/set APIs.

These use a local mock HTTP server so they run without a live backend.
"""
import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import List, Tuple

import pytest

from lasvsim_openapi.http_client import HttpClient, HttpConfig
from lasvsim_openapi.simulator import Simulator
from lasvsim_openapi.simulator_fast import SimulatorFast
from lasvsim_openapi.simulator_model import (
    GetSeedReq,
    GetSeedRes,
    SetSeedReq,
    SetSeedRes,
    SimulatorConfig,
)


class _MockHandler(BaseHTTPRequestHandler):
    """Records requests and replies with canned responses."""

    received: List[Tuple[str, dict, dict]] = []

    def log_message(self, *args):
        pass

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length) or b"{}")
        _MockHandler.received.append((self.path, body, dict(self.headers)))

        if self.path.endswith("/init"):
            resp = {"simulation_id": "sim-abc", "simulation_addr": "127.0.0.1:9999"}
        elif self.path.endswith("/seed/get"):
            resp = {"seed": 20261116}
        else:
            resp = {}

        out = json.dumps(resp).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)


@pytest.fixture
def mock_server():
    """Start a mock backend and yield its endpoint."""
    _MockHandler.received = []
    server = HTTPServer(("127.0.0.1", 0), _MockHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_address[1]}"
    server.shutdown()


@pytest.fixture
def simulator(mock_server: str) -> Simulator:
    """Create a Simulator backed by the mock backend."""
    client = HttpClient(HttpConfig(token="test-token", endpoint=mock_server))
    fast = SimulatorFast(
        http_client=client,
        sim_config=SimulatorConfig(scen_id="scen", scen_ver="1.0.0"),
    )
    return Simulator(fast)


def test_get_seed(simulator: Simulator):
    """Test getting the currently effective random seed."""
    res = simulator.get_seed()
    assert res is not None, "seed response should not be None"
    assert isinstance(res, GetSeedRes)
    assert res.seed == 20261116, "unexpected seed value"


def test_set_seed(simulator: Simulator):
    """Test setting the random seed."""
    res = simulator.set_seed(42)
    assert res is not None, "set seed response should not be None"
    assert isinstance(res, SetSeedRes)


def test_seed_request_paths_and_payloads(simulator: Simulator):
    """Test that seed calls hit the expected paths with the expected payload."""
    simulator.get_seed()
    simulator.set_seed(42)

    paths = [p for p, _, _ in _MockHandler.received]
    assert paths[1].endswith("/openapi/cosim/v2/simulation/seed/get")
    assert paths[2].endswith("/openapi/cosim/v2/simulation/seed/set")

    assert _MockHandler.received[1][1] == {"simulation_id": "sim-abc"}
    assert _MockHandler.received[2][1] == {"simulation_id": "sim-abc", "seed": 42}

    # The BFF routes the request to the simulator via these headers
    for _, _, headers in _MockHandler.received[1:]:
        assert headers.get("x-md-simulation_id") == "sim-abc"
        assert headers.get("x-md-rl-direct-addr") == "127.0.0.1:9999"


def test_seed_models():
    """Test the seed request/response models."""
    get_req = GetSeedReq.from_dict({"simulation_id": "sim-1"})
    assert get_req.simulation_id == "sim-1"

    get_res = GetSeedRes.from_dict({"seed": 12345})
    assert get_res.seed == 12345

    set_req = SetSeedReq.from_dict({"simulation_id": "sim-1", "seed": 42})
    assert set_req.simulation_id == "sim-1"
    assert set_req.seed == 42

    assert SetSeedRes.from_dict({}) is not None
    assert GetSeedRes.from_dict(None) is None
