from typing import Optional
from lasvsim_openapi2.http_client import HttpClient
from lasvsim_openapi2.resource_model import GetHdMapRes, GetHdMapReq

class Resource:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def get_hd_map(self, scen_id: str, scen_ver: str) -> Optional[GetHdMapRes]:
        """Get HD map for a scenario"""
        try:
            response = self.http_client.post(
                "/openapi/resource/v2/scenario/map/get",
                GetHdMapReq(scen_id=scen_id, scen_ver=scen_ver)
            )
            return GetHdMapRes(**response)
        except Exception as e:
            print(f"Error getting HD map: {e}")
            return None
