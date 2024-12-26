# Lasvsim OpenAPI SDK for Python

千行仿真平台的Python SDK。提供了一种简单直观的方式来控制和获取自动驾驶场景的仿真。

## 安装

您可以直接从PyPI安装该软件包：

```bash
pip install lasvsim-openapi
```

## 迁移
执行下面命令修改包名，其中./src为代码目录。修改完成后使用git检查改动。
```bash
grep -rl 'qianxing_openapi' ./src | xargs sed -i '' 's/qianxing_openapi/lasvsim_openapi/g'
```
## 快速开始

以下是SDK使用的简单示例：

```python
from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator import SimulatorConfig
from lasvsim_openapi.request_model import Point

# 初始化客户端
client = Client(
    HttpConfig(
        token="your_token_here",
        endpoint="your_endpoint_here"
    )
)

# 从训练任务中获取可用场景
res = client.train_task.get_scene_id_list(task_id)
print(f"可用场景: {res}")

# 创建仿真器实例
simulator = client.init_simulator_from_config(
    SimulatorConfig(
        scenario_id=res.scene_id_list[0],
        scenario_version=res.scene_version_list[0]
    )
)

# 运行仿真步骤
for i in range(10):
    step_res = simulator.step()
    print(f"第 {i} 步结果: {step_res}")
    # 获取车辆信息
    vehicle_ids = simulator.get_vehicle_id_list()
    print(f"车辆ID列表: {vehicle_ids}")

    # 控制车辆运动
    simulator.set_vehicle_control_info(
        vehicle_id="test_vehicle_1", 
        ste_wheel=1.2,
        lon_acc=1.1
    )

    # 设置车辆位置
    simulator.set_vehicle_position(
        vehicle_id="test_vehicle_1",
        point=Point(x=-8.75, y=-537.0316, z=0)
    )

# 停止仿真
simulator.stop()
```

## 可用API

### 仿真器API

#### 仿真控制
- `init_from_config(sim_config)`: 从配置初始化仿真器
- `init_from_sim(simulation_id, addr)`: 从现有仿真初始化仿真器
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
- `set_vehicle_link_nav(vehicle_id, link_nav)`: 设置车辆链接导航信息
- `set_vehicle_destination(vehicle_id, destination)`: 设置车辆目标点

#### 交通信号灯API
- `get_current_stage(junction_id)`: 获取当前交通信号灯阶段
- `get_movement_signal(movement_id)`: 获取转向信号灯颜色
- `get_signal_plan(junction_id)`: 获取交通信号灯配时方案
- `get_movement_list(junction_id)`: 获取路口转向列表

#### 行人API
- `get_ped_id_list()`: 获取所有行人ID
- `get_ped_base_info(ped_id_list)`: 获取行人基本信息
- `set_ped_position(ped_id, point, phi)`: 设置行人位置和航向角

#### 非机动车API
- `get_nmv_id_list()`: 获取所有非机动车ID
- `get_nmv_base_info(nmv_id_list)`: 获取非机动车基本信息
- `set_nmv_position(nmv_id, point, phi)`: 设置非机动车位置和航向角

### 训练任务API
- `get_scene_id_list(task_id)`: 获取训练任务可用场景列表

### 资源API
- `get_map(asset_id, asset_version)`: 获取特定资源的地图数据

## 系统要求

- Python >= 3.0
- requests >= 2.25.0

## 许可证

## 支持

如需报告错误或请求新功能，请使用[GitHub Issues](https://github.com/risenlighten-qianxing/openapi-sdk-python/issues)页面。
