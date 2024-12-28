from dataclasses import dataclass
from typing import Optional
from .qxmap_model import Qxmap

@dataclass
class GetHdMapReq:
    scen_id: str = ""
    scen_ver: str = ""

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data

@dataclass
class GetHdMapRes:
    data: Optional[Qxmap] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return

        self.__dict__ = data
