from lasvsim_openapi.http_client import HttpClient
from lasvsim_openapi.qxmap_model import Qxmap


class Resources:
    client: HttpClient

    def __init__(self, client: HttpClient):
        self.client = client

    def get_map(
        self,
        scen_id: str = None,
        scen_ver: str = None,
    ) -> Qxmap:
        req_data = {"scen_id": scen_id, "scen_ver": scen_ver}
        resp = self.client.post(
            "/openapi/resource/v2/scenario/map/get", req_data)

        return Qxmap(resp["data"])
