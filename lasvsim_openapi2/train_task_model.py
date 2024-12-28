from dataclasses import dataclass
from typing import List

@dataclass
class GetSceneIdListReq:
    task_id: int = 0

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data

@dataclass
class GetSceneIdListRes:
    scene_id_list: List[str] = None
    scene_version_list: List[str] = None

    def __init__(self, data: dict) -> None:
        if data == None:
            return
        self.__dict__ = data
