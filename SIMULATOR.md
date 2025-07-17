# simulator
仿真器接口列表
## 主要功能分类

### 基础仿真控制
- `step()` - 推进仿真一步
- `stop()` - 停止仿真
- `reset()` - 重置仿真器，可选择是否重置交通流

### 地图与信号灯相关
- `get_current_stage()` - 获取路口当前阶段
- `get_movement_signal()` - 获取转向信号灯状态
- `get_signal_plan()` - 获取路口信号配时方案
- `get_movement_list()` - 获取路口转向列表
- `next_stage()` - 切换到下一个信号灯阶段

### 车辆信息查询
- `get_vehicle_id_list()` - 获取所有车辆ID列表
- `get_test_vehicle_id_list()` - 获取测试车辆ID列表
- `get_vehicle_base_info()` - 获取车辆基本信息
- `get_vehicle_position()` - 获取车辆位置信息
- `get_vehicle_moving_info()` - 获取车辆运动状态
- `get_vehicle_control_info()` - 获取车辆控制信息
- `get_vehicle_perception_info()` - 获取车辆感知信息
- `get_vehicle_reference_lines()` - 获取车辆参考线
- `get_vehicle_planning_info()` - 获取车辆规划信息
- `get_vehicle_navigation_info()` - 获取车辆导航信息
- `get_vehicle_collision_status()` - 获取车辆碰撞状态
- `get_vehicle_target_speed()` - 获取车辆目标速度
- `get_vehicle_sensor_config()` - 获取车辆传感器配置

### 车辆控制接口
- `set_vehicle_control_info()` - 设置车辆控制信息(方向盘角度、纵向加速度)
- `set_vehicle_moving_info()` - 设置车辆运动状态
- `set_vehicle_base_info()` - 设置车辆基本信息
- `set_vehicle_planning_info()` - 设置车辆规划路径
- `set_vehicle_position()` - 设置车辆位置
- `set_vehicle_link_nav()` - 设置车辆导航路径
- `set_vehicle_destination()` - 设置车辆目的地

### 行人相关
- `get_ped_id_list()` - 获取行人ID列表
- `get_ped_base_info()` - 获取行人基本信息
- `set_ped_position()` - 设置行人位置

### 非机动车相关
- `get_nmv_id_list()` - 获取非机动车ID列表
- `get_nmv_base_info()` - 获取非机动车基本信息
- `set_nmv_position()` - 设置非机动车位置

### 其他参与者信息
- `get_step_spawn_id_list()` - 获取当前步新生成的参与者ID列表
- `get_participant_base_info()` - 获取参与者基本信息
- `get_participant_moving_info()` - 获取参与者运动信息
- `get_participant_position()` - 获取参与者位置信息

### 高级功能
- `set_vehicle_road_perception_info()` - 设置车辆道路感知信息
- `set_vehicle_obstacle_perception_info()` - 设置车辆障碍物感知信息
- `set_vehicle_extra_metrics()` - 设置车辆额外指标
- `set_vehicle_local_paths()` - 设置车辆局部路径
- `get_idc_vehicle_nav()` - 获取IDC车辆导航信息
- `idc_step()` - IDC仿真步进