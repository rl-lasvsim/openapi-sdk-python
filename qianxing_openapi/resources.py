from qianxing_openapi.http_client import HttpClient
from qianxing_openapi.qxmap_model import Qxmap


class Resources:
    client: HttpClient

    def __init__(self, client: HttpClient):
        self.client = client

    def get_map(
        self,
        asset_id: str = None,
        asset_version: str = None,
    ) -> Qxmap:
        req_data = {"asset_id": asset_id, "asset_version": asset_version}
        resp = self.client.post("/openapi/resource/v2/scenario/map/get", req_data)

        return Qxmap(resp["data"])
