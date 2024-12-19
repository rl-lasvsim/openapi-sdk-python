#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig, HttpClient
from lasvsim_openapi.simulator import SimulatorConfig
from dataclasses import dataclass
from lasvsim_openapi.request_model import Point, ObjBaseInfo
from typing import List
from lasvsim_openapi.train_task import TrainTask
from lasvsim_openapi.qxmap_model import Qxmap

# data = {
#     'id': 23,
#     'config': {
#         'scenario_id': 'gfdsfsf',
#         'scenario_version': 'hhhhh',
#         'record_id': 1
#     },
#     'reason': 'my reason',
# }


# class ErrorModel:
#     code: int = 0
#     message: str = ""
#     reason: str = ""


# class MyConfig:
#     scenario_id: str
#     scenario_version: str
#     record_id: int
#     # 如果不是必需的字段，需要设置默认值，保证from_dict成功执行。
#     not_in_dict: str = None

#     def __init__(self, data: dict):
#         self.__dict__ = data

#     def to_dict(self):
#         return self.__dict__


# # @dataclass
# class MyTabl(ErrorModel):
#     id: int
#     config: MyConfig

#     def __init__(self, data: dict):
#         if (data == None):
#             return
#         config = data.pop('config', None)

#         self.__dict__ = data
#         self.config = MyConfig(config)


# mt = MyTabl(data)


# def myfunc() -> MyTabl:
#     return mt


# def cc():
#     return mt


# haha = myfunc()
# print(mt.id, mt.reason)
# print(mt.config.scenario_id)
# print(haha.config)
# print(haha.config.to_dict())
# hclient = HttpClient(
#     config=HttpConfig(
#         "",
#         "",
#     ),
#     headers={},
# )
# resp = hclient.post(
#     "/dev/api/viewhelper/tableheader/get",
#     data={"table_code": "LISTCODE_TASK"},
#     object_hook=MyTabl,
# )
# print(resp)

api_client = Client(
    HttpConfig(
        token=os.getenv("QX_TOKEN"),
        endpoint=os.getenv("QX_ENDPOINT"),
    )
)

# simulator_instance = api_client.init_simulator_from_config(
#     SimulatorConfig(scenario_id="66e525cdb504ceb8d6cd4d9a", scenario_version="0")
# )

# print(f"初始化成功过后的仿真器id：{simulator_instance.simulation_id}\n")

# print("rrrrrrrrr", simulator_instance.client.headers)

# for i in range(10):
#     step_res = simulator_instance.step()
#     print(f"执行第{i}步的结果:{step_res}")  # FIXME: 第一步就执行结束了

# # stop_res = simulator_instance.stop()
# # print(f"停止仿真器的结果:{stop_res}\n")

# res = simulator_instance.get_vehicle_id_list()
# print(f"获取所有车辆ID列表的结果:{res}\n")

# res = simulator_instance.get_test_vehicle_id_list()  # FIXME: 401
# print(f"获取测试车辆ID列表的结果:{res}\n")

# res = simulator_instance.get_vehicle_base_info([])
# print(f"根据车辆ID列表获取车辆基本信息的结果:{res}\n")

# res = simulator_instance.get_vehicle_position(["测试车辆1", "环境车辆1", "环境车辆2"])
# print(f"根据车辆ID列表获取车辆位置信息的结果:{res}\n")

# res = simulator_instance.get_vehicle_moving_info(
#     ["测试车辆1", "环境车辆1", "环境车辆2"]
# )
# print(f"根据车辆ID列表获取车辆运动信息的结果:{res}\n")

# res = simulator_instance.get_vehicle_control_info(
#     ["测试车辆1", "环境车辆1", "环境车辆2"]
# )
# print(f"根据车辆ID列表获取车辆控制参数信息的结果:{res}\n")

# res = simulator_instance.get_vehicle_perception_info("测试车辆1")
# print(f"根据车辆ID获取车辆感知信息的结果:{res}\n")

# res = simulator_instance.get_vehicle_planning_info("测试车辆1")
# print(f"获取车辆规划路径的结果:{res}\n")

# res = simulator_instance.get_vehicle_navigation_info("测试车辆1")
# print(f"获取车辆导航信息的结果:{res}\n")

# res = simulator_instance.get_vehicle_collision_status("测试车辆1")
# print(f"根据车辆ID获取车辆碰撞状态的结果:{res}\n")

# res = simulator_instance.set_vehicle_planning_info(
#     vehicle_id="测试车辆1",
#     planning_path=[
#         Point(x=-8.75, y=-537.0316, z=0),
#         Point(x=-8.75, y=-537.5316, z=0),
#         Point(x=-8.75, y=-538.0316, z=0),
#         Point(x=-8.75, y=-538.5316, z=0),
#     ],
# )
# print(f"修改车辆规划路径的结果:{res}\n")

# res = simulator_instance.get_vehicle_planning_info("测试车辆1")
# print(f"获取车辆规划路径的结果:{res}\n")

# res = simulator_instance.set_vehicle_control_info(
#     vehicle_id="测试车辆1", ste_wheel=1.2, lon_acc=1.1
# )
# print(f"修改车辆控制参数:{res}\n")
# res = simulator_instance.get_vehicle_control_info(
#     ["测试车辆1", "环境车辆1", "环境车辆2"]
# )
# print(f"根据车辆ID列表获取车辆控制参数信息的结果:{res}\n")

# res = simulator_instance.set_vehicle_position(
#     vehicle_id="测试车辆1", point=Point(x=-8.75, y=-537.0316, z=0)
# )
# print(f"修改车辆点位信息:{res}\n")

# res = simulator_instance.get_vehicle_position(["测试车辆1", "环境车辆1", "环境车辆2"])
# print(f"根据车辆ID列表获取车辆位置信息的结果:{res}\n")

# res = simulator_instance.set_vehicle_moving_info(vehicle_id="测试车辆1", u=1.1, v=1.2)
# print(f"修改车辆运动信息:{res}\n")

# res = simulator_instance.get_vehicle_moving_info(
#     ["测试车辆1", "环境车辆1", "环境车辆2"]
# )
# print(f"根据车辆ID列表获取车辆运动信息的结果:{res}\n")

# # res = simulator_instance.get_movement_list(junction_id="f")
# # print(f"根据junctionId获取对应movement列表:{res}\n")
# res = simulator_instance.set_vehicle_base_info(
#     vehicle_id="测试车辆1",
#     base_info=ObjBaseInfo(
#         1,
#         2,
#         3,
#         4,
#     ),
# )
# print(f"修改车辆基础信息,:{res}\n")

# res = simulator_instance.get_vehicle_base_info(["测试车辆1"])
# print(f"根据车辆ID列表获取车辆基本信息的结果:{res}\n")

# # res = simulator_instance.set_vehicle_link_nav(
# #     vehicle_id="测试车辆1", link_nav=["sg7_lk0"]
# # )
# # print(f"修改车辆子路段导航信息:{res}\n")

# res = simulator_instance.get_vehicle_navigation_info("测试车辆1")
# print(f"获取车辆导航信息的结果:{res}\n")

# # res = simulator_instance.set_vehicle_destination(vehicle_id="测试车辆1")
# # print(f"修改车辆终点:{res}\n")

# res = simulator_instance.get_ped_id_list()
# print(f"获取行人ID列表:{res}\n")

# res = simulator_instance.get_ped_base_info(ped_id_list=["ped280", "ped100", "ped182"])
# print(f"获取行人基础信息:{res}\n")

# # res = simulator_instance.set_ped_position(
# #     ped_id="ped280", point=Point(x=-8.75, y=-538.5316, z=0)
# # )
# # print(f"修改行人点位信息, 航向角Phi:{res}\n")

# res = simulator_instance.get_nmv_id_list()
# print(f"获取非机动车ID列表:{res}\n")

# # res = simulator_instance.get_nmv_base_info(nmv_id_list=["ped280", "ped100", "ped182"])
# # print(f"获取非机动车基础信息:{res}\n")

# # res = simulator_instance.set_ped_position(
# #     ped_id="ped280", point=Point(x=-8.75, y=-538.5316, z=0), phi=1.2
# # )
# # print(f"修改非机动车点位信息, 航向角Phi:{res}\n")
# res = simulator_instance.stop()
# print(f"停止仿真器:{res}\n")

# ---------------------------
# simulator_instance = api_client.init_simulator_from_config(
#     SimulatorConfig(scenario_id="58821406023938", scenario_version="1")
# )

# res = api_client.train_task.get_scene_id_list(395)
# print(f"训练任务获取场景列表:{res}\n")

# res = simulator_instance.get_map(asset_id="66e525cdb504ceb8d6cd4d9a", asset_version="0")
# print(f"地图查询结果:{res}")

# -----------resource-------------

# res = api_client.resources.get_map(
#     asset_id="66e525cdb504ceb8d6cd4d9a", asset_version="0"
# )
# print(f"获取地图结构:{res}\n")

# ----------------train_task--------------

res = api_client.train_task.get_scene_id_list(395)
print(f"训练任务获取场景列表:{res}\n")

simulator_instance = api_client.init_simulator_from_config(
    SimulatorConfig(
        scenario_id=res.scene_id_list[0], scenario_version=res.scene_version_list[0]
    )
)

print(f"初始化成功过后的仿真器id：{simulator_instance.simulation_id}\n")

print("rrrrrrrrr", simulator_instance.client.headers)

res = simulator_instance.get_vehicle_base_info(["测试车辆1"])
print(f"获取车辆基础信息:{res}\n")
res = simulator_instance.get_vehicle_target_speed("测试车辆1")
print(f"获取车辆目标速度:{res}\n")
for i in range(10):
    step_res = simulator_instance.step()
    print(f"执行第{i}步的结果:{step_res}")
# res = simulator_instance.reset()
# print(f"重置仿真器:{res}\n")
res = simulator_instance.stop()
print(f"停止仿真器:{res}\n")

# for i in range(10):
#     step_res = simulator_instance.step()
#     print(f"执行第{i}步的结果:{step_res}")  # FIXME: 第一步就执行结束了

#     # stop_res = simulator_instance.stop()
#     # print(f"停止仿真器的结果:{stop_res}\n")

#     res = simulator_instance.get_vehicle_id_list()
#     print(f"获取所有车辆ID列表的结果:{res}\n")

#     res = simulator_instance.get_test_vehicle_id_list()  # FIXME: 401
#     print(f"获取测试车辆ID列表的结果:{res}\n")

#     res = simulator_instance.get_vehicle_base_info([])
#     print(f"根据车辆ID列表获取车辆基本信息的结果:{res}\n")

#     res = simulator_instance.get_vehicle_position(
#         ["测试车辆1", "环境车辆1", "环境车辆2"]
#     )
#     print(f"根据车辆ID列表获取车辆位置信息的结果:{res}\n")

#     res = simulator_instance.get_vehicle_moving_info(
#         ["测试车辆1", "环境车辆1", "环境车辆2"]
#     )
#     print(f"根据车辆ID列表获取车辆运动信息的结果:{res}\n")

#     res = simulator_instance.get_vehicle_control_info(
#         ["测试车辆1", "环境车辆1", "环境车辆2"]
#     )
#     print(f"根据车辆ID列表获取车辆控制参数信息的结果:{res}\n")

#     res = simulator_instance.get_vehicle_perception_info("测试车辆1")
#     print(f"根据车辆ID获取车辆感知信息的结果:{res}\n")

#     res = simulator_instance.get_vehicle_planning_info("测试车辆1")
#     print(f"获取车辆规划路径的结果:{res}\n")

#     res = simulator_instance.get_vehicle_navigation_info("测试车辆1")
#     print(f"获取车辆导航信息的结果:{res}\n")

#     res = simulator_instance.get_vehicle_collision_status("测试车辆1")
#     print(f"根据车辆ID获取车辆碰撞状态的结果:{res}\n")

#     res = simulator_instance.set_vehicle_planning_info(
#         vehicle_id="测试车辆1",
#         planning_path=[
#             Point(x=-8.75, y=-537.0316, z=0),
#             Point(x=-8.75, y=-537.5316, z=0),
#             Point(x=-8.75, y=-538.0316, z=0),
#             Point(x=-8.75, y=-538.5316, z=0),
#         ],
#     )
#     print(f"修改车辆规划路径的结果:{res}\n")

#     res = simulator_instance.get_vehicle_planning_info("测试车辆1")
#     print(f"获取车辆规划路径的结果:{res}\n")

#     res = simulator_instance.set_vehicle_control_info(
#         vehicle_id="测试车辆1", ste_wheel=1.2, lon_acc=1.1
#     )
#     print(f"修改车辆控制参数:{res}\n")
#     res = simulator_instance.get_vehicle_control_info(
#         ["测试车辆1", "环境车辆1", "环境车辆2"]
#     )
#     print(f"根据车辆ID列表获取车辆控制参数信息的结果:{res}\n")

#     res = simulator_instance.set_vehicle_position(
#         vehicle_id="测试车辆1", point=Point(x=-8.75, y=-537.0316, z=0)
#     )
#     print(f"修改车辆点位信息:{res}\n")

#     res = simulator_instance.get_vehicle_position(
#         ["测试车辆1", "环境车辆1", "环境车辆2"]
#     )
#     print(f"根据车辆ID列表获取车辆位置信息的结果:{res}\n")

#     res = simulator_instance.set_vehicle_moving_info(
#         vehicle_id="测试车辆1", u=1.1, v=1.2
#     )
#     print(f"修改车辆运动信息:{res}\n")

#     res = simulator_instance.get_vehicle_moving_info(
#         ["测试车辆1", "环境车辆1", "环境车辆2"]
#     )
#     print(f"根据车辆ID列表获取车辆运动信息的结果:{res}\n")

#     # res = simulator_instance.get_movement_list(junction_id="f")
#     # print(f"根据junctionId获取对应movement列表:{res}\n")
#     res = simulator_instance.set_vehicle_base_info(
#         vehicle_id="测试车辆1",
#         base_info=ObjBaseInfo(
#             1,
#             2,
#             3,
#             4,
#         ),
#     )
#     print(f"修改车辆基础信息,:{res}\n")

#     res = simulator_instance.get_vehicle_base_info(["测试车辆1"])
#     print(f"根据车辆ID列表获取车辆基本信息的结果:{res}\n")

#     # res = simulator_instance.set_vehicle_link_nav(
#     #     vehicle_id="测试车辆1", link_nav=["sg7_lk0"]
#     # )
#     # print(f"修改车辆子路段导航信息:{res}\n")

#     res = simulator_instance.get_vehicle_navigation_info("测试车辆1")
#     print(f"获取车辆导航信息的结果:{res}\n")

#     # res = simulator_instance.set_vehicle_destination(vehicle_id="测试车辆1")
#     # print(f"修改车辆终点:{res}\n")

#     res = simulator_instance.get_ped_id_list()
#     print(f"获取行人ID列表:{res}\n")

#     res = simulator_instance.get_ped_base_info(
#         ped_id_list=["ped280", "ped100", "ped182"]
#     )
#     print(f"获取行人基础信息:{res}\n")

#     # res = simulator_instance.set_ped_position(
#     #     ped_id="ped280", point=Point(x=-8.75, y=-538.5316, z=0)
#     # )
#     # print(f"修改行人点位信息, 航向角Phi:{res}\n")

#     res = simulator_instance.get_nmv_id_list()
#     print(f"获取非机动车ID列表:{res}\n")

#     # res = simulator_instance.get_nmv_base_info(nmv_id_list=["ped280", "ped100", "ped182"])
#     # print(f"获取非机动车基础信息:{res}\n")

#     # res = simulator_instance.set_ped_position(
#     #     ped_id="ped280", point=Point(x=-8.75, y=-538.5316, z=0), phi=1.2
#     # )
#     # print(f"修改非机动车点位信息, 航向角Phi:{res}\n")
#     res = simulator_instance.stop()
#     print(f"停止仿真器:{res}\n")
