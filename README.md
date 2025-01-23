# Lasvsim OpenAPI SDK for Python

千行仿真平台（Lasvsim）的 Python SDK。提供了一种简单直观的方式来控制和获取自动驾驶场景的仿真。

## 安装

您可以直接从PyPI安装该软件包：

```bash
pip install lasvsim-openapi
```

## 快速开始

以下是 SDK 使用的简单示例：

```python
import os

from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator import SimulatorConfig

# 接口地址
endpoint = os.getenv("QX_ENDPOINT")  # 线上环境地址: https://qianxing-api.risenlighten.com
# 授权token
token = os.getenv("QX_TOKEN")  # 登录仿真平台后访问https://qianxing.risenlighten.com/#/usecenter/personalCenter, 点击最下面按钮复制token

# 登录仿真平台, 选择想要进行联合仿真的任务及剧本
task_id = 0  # 替换为你的任务ID
record_id = 0  # 替换为你的剧本ID

# 1. 初始化客户端
cli = Client(HttpConfig(
    endpoint=endpoint,  # 接口地址
    token=token,  # 授权token
))

# 2. 拷贝剧本, 返回的结构中new_record_id字段就是新创建的剧本ID
# 仿真结束后可到该剧本下查看结果详情
new_record = cli.process_task.copy_record(task_id, record_id)
print("拷贝剧本成功")

# 3. 通过拷贝的场景Id、Version和SimRecordId初始化仿真器
simulator = cli.init_simulator_from_config(
    SimulatorConfig(
        scen_id=new_record.scen_id,
        scen_ver=new_record.scen_ver,
        sim_record_id=new_record.sim_record_id,
    )
)
print("初始化仿真器成功")

try:
    # 获取测试车辆列表
    test_vehicle_list = simulator.get_test_vehicle_id_list()
    print("测试车辆ID列表:", test_vehicle_list)

    # 记录仿真器运行状态(True: 运行中; False: 运行结束), 任务运行过程中持续更新该状态
    is_running = True

    # 使测试车辆环形行驶
    while is_running:
        # 设置方向盘转角10度, 纵向加速度0.05
        ste_wheel = 10.0
        lon_acc = 0.05

        # 设置车辆的控制信息
        simulator.set_vehicle_control_info(
            test_vehicle_list.list[0], ste_wheel, lon_acc
        )

        # 执行仿真器步骤
        step_res = simulator.step()
        print(f"第 {i} 步结果: {step_res}")
        
        is_running = step_res.code.is_running()

    # 可在此处继续调用其他接口, 查看联合仿真文档: https://www.risenlighten.com/#/union

    # 仿真结束后, 到千行仿真平台对应的taskId/recordId下查看联合仿真结果详情
    print(f"https://qianxing.risenlighten.com/#/configuration/circleTask?id={task_id}")

    # 如想直接查看本次联合仿真的回放视频, 可访问下面网址：
    print(f"https://qianxing.risenlighten.com/#/sampleRoad/cartest/?id={task_id}&record_id={new_record.new_record_id}&sim_record_id={new_record.sim_record_id}")

finally:
    # 停止仿真器, 释放服务器资源
    simulator.stop()
```

## 可用API

### 仿真器API

#### 仿真控制
- `init_simulator_from_config(sim_config)`: 从配置初始化仿真器
- `init_simulator_from_sim(simulation_id, addr)`: 从现有仿真初始化仿真器
- `step()`: 仿真前进一步
- `stop()`: 停止仿真
- `reset(reset_traffic_flow)`: 重置仿真器到初始状态，可选择是否重置交通流

#### 车辆API
- `get_vehicle_id_list()`: 获取所有车辆ID
- `get_test_vehicle_id_list()`: 获取测试车辆ID
- `get_vehicle_base_info(id_list)`: 获取车辆基本信息
- `get_vehicle_position(id_list)`: 获取车辆位置
- `get_vehicle_moving_info(id_list)`: 获取车辆运动信息
- `get_vehicle_control_info(id_list)`: 获取车辆控制参数
- `get_vehicle_perception_info(vehicle_id)`: 获取车辆感知信息
- `get_vehicle_reference_lines(vehicle_id)`: 获取可用参考线
- `get_vehicle_planning_info(vehicle_id)`: 获取车辆规划信息
- `get_vehicle_navigation_info(vehicle_id)`: 获取车辆导航信息
- `get_vehicle_collision_status(vehicle_id)`: 检查车辆碰撞状态
- `get_vehicle_target_speed(vehicle_id)`: 获取车辆目标速度
- `set_vehicle_position(vehicle_id, point, phi)`: 设置车辆位置和航向角
- `set_vehicle_control_info(vehicle_id, ste_wheel, lon_acc)`: 设置车辆控制参数
- `set_vehicle_planning_info(vehicle_id, planning_path)`: 设置车辆规划路径
- `set_vehicle_moving_info(vehicle_id, u, v, w, u_acc, v_acc, w_acc)`: 设置车辆运动参数
- `set_vehicle_base_info(vehicle_id, base_info)`: 设置车辆基本信息

#### 交通流API
- `get_traffic_flow_info()`: 获取交通流信息
- `get_traffic_flow_vehicle_info(vehicle_id)`: 获取交通流车辆信息
- `get_traffic_flow_vehicle_list()`: 获取交通流车辆列表
- `get_traffic_flow_vehicle_position(vehicle_id)`: 获取交通流车辆位置
- `get_traffic_flow_vehicle_moving_info(vehicle_id)`: 获取交通流车辆运动信息
- `get_traffic_flow_vehicle_control_info(vehicle_id)`: 获取交通流车辆控制信息

#### 场景API
- `get_scene_info()`: 获取场景信息
- `get_scene_objects()`: 获取场景物体列表
- `get_scene_object_info(object_id)`: 获取场景物体信息
- `get_scene_object_position(object_id)`: 获取场景物体位置
- `get_scene_object_moving_info(object_id)`: 获取场景物体运动信息
- `get_scene_object_control_info(object_id)`: 获取场景物体控制信息

#### 路网API
- `get_lane_info(lane_id)`: 获取车道信息
- `get_lane_list()`: 获取车道列表
- `get_lane_center_line(lane_id)`: 获取车道中心线
- `get_lane_boundary(lane_id)`: 获取车道边界
- `get_lane_width(lane_id)`: 获取车道宽度
- `get_lane_speed_limit(lane_id)`: 获取车道限速
- `get_lane_type(lane_id)`: 获取车道类型
- `get_lane_direction(lane_id)`: 获取车道方向
- `get_lane_predecessor(lane_id)`: 获取前序车道
- `get_lane_successor(lane_id)`: 获取后继车道

#### 路口API
- `get_junction_info(junction_id)`: 获取路口信息
- `get_junction_list()`: 获取路口列表
- `get_junction_center_point(junction_id)`: 获取路口中心点
- `get_junction_boundary(junction_id)`: 获取路口边界
- `get_junction_type(junction_id)`: 获取路口类型
- `get_junction_direction(junction_id)`: 获取路口方向
- `get_junction_predecessor(junction_id)`: 获取前序路口
- `get_junction_successor(junction_id)`: 获取后继路口
- `get_movement_list(junction_id)`: 获取移动列表
