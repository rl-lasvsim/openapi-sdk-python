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

## 本地仿真
具体例子参考：examples/beginnr/local_sim.py
创建本地仿真client：
```python
from lasvsim_openapi.client import Client

# 初始化客户端
cli = Client(
    local_mode=True,
)
```

### 升级opensim
执行命令升级opensim：
```bash
python -c "import lasvsim_openapi.opensim;lasvsim_openapi.opensim.upgrade_opensim()"
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
- `set_vehicle_control_info(vehicle_id, ste_wheel, lon_acc, drive_force_front_axle, drive_force_rear_axle, brake_force_fl, brake_force_fr, brake_force_rl, brake_force_rr)`: 设置车辆控制参数
- `set_vehicle_planning_info(vehicle_id, planning_path)`: 设置车辆规划路径
- `set_vehicle_moving_info(vehicle_id, u, v, w, u_acc, v_acc, w_acc)`: 设置车辆运动参数
- `set_vehicle_base_info(vehicle_id, base_info)`: 设置车辆基本信息

---

## set_vehicle_control_info 接口使用说明

### 概述

`set_vehicle_control_info` 用于设置测试车辆的控制参数，支持**运动学控制**和**动力学控制**两种模式。

### 函数签名

```python
simulator.set_vehicle_control_info(
    vehicle_id: str,
    ste_wheel: Optional[float] = None,
    lon_acc: Optional[float] = None,
    drive_force_front_axle: float = 0.0,
    drive_force_rear_axle: float = 0.0,
    brake_force_fl: float = 0.0,
    brake_force_fr: float = 0.0,
    brake_force_rl: float = 0.0,
    brake_force_rr: float = 0.0,
) -> SetVehicleControlInfoRes
```

### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `vehicle_id` | str | - | 车辆 ID |
| `ste_wheel` | float | None | 方向盘转角 [度] |
| `lon_acc` | float | None | 纵向加速度 [m/s²] |
| `drive_force_front_axle` | float | 0.0 | 前轴驱动力 [N] |
| `drive_force_rear_axle` | float | 0.0 | 后轴驱动力 [N] |
| `brake_force_fl` | float | 0.0 | 左前轮制动力 [N] |
| `brake_force_fr` | float | 0.0 | 右前轮制动力 [N] |
| `brake_force_rl` | float | 0.0 | 左后轮制动力 [N] |
| `brake_force_rr` | float | 0.0 | 右后轮制动力 [N] |

### 控制模式

#### 1. 运动学控制（推荐用于简单场景）

```python
# 方向盘转角 5 度，纵向加速度 0.1 m/s²
simulator.set_vehicle_control_info(
    vehicle_id="vehicle_1",
    ste_wheel=5.0,
    lon_acc=0.1,
)
```

#### 2. 动力学控制（高保真仿真）

```python
# 后轮驱动，前轮制动
simulator.set_vehicle_control_info(
    vehicle_id="vehicle_1",
    drive_force_rear_axle=500.0,  # 后轴驱动力 500N
    brake_force_fl=100.0,         # 左前轮制动力 100N
    brake_force_fr=100.0,         # 右前轮制动力 100N
)
```

#### 3. 组合控制

```python
# 转向 + 后轴驱动
simulator.set_vehicle_control_info(
    vehicle_id="vehicle_1",
    ste_wheel=3.0,
    drive_force_rear_axle=400.0,
)
```

### 注意事项

1. **参数优先级**：当同时设置 `lon_acc` 和驱动力/制动力时，动力学参数优先
2. **单位**：角度单位为度 [°]，力单位为牛顿 [N]，加速度单位为 m/s²
3. **默认值**：未指定的参数使用默认值 0.0
4. **四轮独立制动**：可分别控制每个车轮的制动力，实现差动制动效果

### 测试脚本

参考 `tests/test_cosim_task.py`，包含 7 个测试用例覆盖所有控制参数组合。