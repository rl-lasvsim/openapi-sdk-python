from dataclasses import dataclass
from typing import List, Optional

@dataclass
class GetSceneIdListReq:
    task_id: int

@dataclass
class GetSceneIdListRes:
    scene_id_list: List[str]
    scene_version_list: List[str]
