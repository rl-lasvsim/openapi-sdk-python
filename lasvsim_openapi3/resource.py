from typing import Optional
from .resource_model import (
    Qxmap,
    GetHdMapReq,
    GetHdMapRes,
    Header,
    Junction,
    Polygon,
    Point,
    Movement,
    Direction,
    Connection,
    LineString,
    Crosswalk,
    Link,
    LinkType,
    Width,
    Lane,
    LaneType,
    LaneTurn,
    DirectedPoint,
    SpeedLimit,
    SpeedLimitType,
    Stopline,
    LaneMark,
    LaneMarkStyle,
    LaneMarkColor,
    CenterPoint,
    SignalPlan,
    SignalPlan_MovementSignal,
    SignalPlan_MovementSignal_SignalOfGreen,
    Segment,
    TrafficSign,
    TrafficSignType,
    Road,
    RoadType,
    RoadPosition,
    ControlPoint,
    ReferencePoint,
    Section,
    JunctionPosition,
    Mapper,
    Building,
    Tree,
    Lamp
)
from .httpclient import HttpClient

class Resource:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client.clone()

    def get_hd_map(self, scen_id: str, scen_ver: str) -> Optional[Qxmap]:
        req = GetHdMapReq(scen_id=scen_id, scen_ver=scen_ver)
        res = GetHdMapRes()
        self.http_client.post(
            "/openapi/resource/v2/scenario/map/get",
            req,
            res
        )
        return res.data
