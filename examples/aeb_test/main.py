#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AEB (自动紧急制动) 接口测试示例

本示例演示如何使用 SDK 的 set_aeb_status 接口来设置车辆的 AEB 状态。

环境变量:
    QX_ENDPOINT: 仿真平台接口地址 (默认：https://qianxing-api.risenlighten.com)
    QX_TOKEN: 授权 token
    QX_TASK_ID: 任务 ID
    QX_RECORD_ID: 剧本 ID

使用方法:
    export QX_ENDPOINT="https://qianxing-api.risenlighten.com"
    export QX_TOKEN="your_token_here"
    export QX_TASK_ID=123
    export QX_RECORD_ID=456
    python examples/aeb_test/main.py

AEB 状态说明:
    - emergency_braking: 紧急制动状态，True 表示触发紧急制动
    - first_collision_warning: 第一次碰撞预警报警，True 表示触发预警
    - second_collision_warning: 第二次碰撞预警报警，True 表示触发二次预警
"""
import os

from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator_model import SimulatorConfig


def main():
    # ========== 可配置的 AEB 状态范围 ==========
    # 格式：(起始步，结束步) - 左闭右开区间 [start, end)
    # 例如：(10, 20) 表示第 10-19 步触发该状态
    
    FIRST_WARNING_RANGE = (10, 20)      # 第一次碰撞预警范围
    SECOND_WARNING_RANGE = (20, 30)     # 第二次碰撞预警范围
    EMERGENCY_BRAKING_RANGE = (30, 40)  # 紧急制动范围
    
    MAX_STEPS = 1000000  # 总仿真步数
    # =========================================

    # 接口地址和授权 token
    endpoint = os.getenv(
        "QX_ENDPOINT", "https://qianxing-api.risenlighten.com"
    )
    token = os.getenv("QX_TOKEN")

    # 登录仿真平台，选择想要进行联合仿真的任务及剧本
    task_id_str = os.getenv("QX_TASK_ID")
    record_id_str = os.getenv("QX_RECORD_ID")
    
    if not token:
        raise ValueError("请设置环境变量 QX_TOKEN")
    if not task_id_str or not record_id_str:
        raise ValueError("请设置环境变量 QX_TASK_ID 和 QX_RECORD_ID")
    
    task_id = int(task_id_str)
    record_id = int(record_id_str)

    # 1. 初始化客户端
    cli = Client(
        HttpConfig(
            endpoint=endpoint,
            token=token,
        )
    )

    # 2. 拷贝剧本
    new_record = cli.process_task.copy_record(task_id, record_id)
    print(f"✓ 剧本拷贝成功，新剧本 ID: {new_record.new_record_id}")

    # 3. 通过拷贝的场景 Id、Version 和 SimRecordId 初始化仿真器
    simulator = cli.init_simulator_from_config(
        SimulatorConfig(
            scen_id=new_record.scen_id,
            scen_ver=new_record.scen_ver,
            sim_record_id=new_record.sim_record_id,
        )
    )
    print(f"✓ 仿真器初始化成功，仿真 ID: {simulator.simulator_fast.simulation_id}")

    try:
        # 4. 获取测试车辆列表
        test_vehicle_list = simulator.get_test_vehicle_id_list()
        if not test_vehicle_list.list:
            raise ValueError("未找到测试车辆")
        
        target_vehicle = test_vehicle_list.list[0]
        print(f"✓ 使用测试车辆：{target_vehicle}")

        # 打印 AEB 配置
        print("\n" + "=" * 60)
        print("AEB 状态配置:")
        print("=" * 60)
        print(f"  第一次碰撞预警：步 {FIRST_WARNING_RANGE[0]} - {FIRST_WARNING_RANGE[1] - 1}")
        print(f"  第二次碰撞预警：步 {SECOND_WARNING_RANGE[0]} - {SECOND_WARNING_RANGE[1] - 1}")
        print(f"  紧急制动：      步 {EMERGENCY_BRAKING_RANGE[0]} - {EMERGENCY_BRAKING_RANGE[1] - 1}")
        print(f"  总仿真步数：    {MAX_STEPS}")
        print("=" * 60 + "\n")

        # 5. 仿真循环
        step_count = 0
        
        print(f"开始仿真...")
        print("-" * 60)
        
        while step_count < MAX_STEPS:
            # 每次循环默认重置为 False，不受上一次设置影响
            emergency_braking = False
            first_collision_warning = False
            second_collision_warning = False
            
            # 根据仿真步数范围设置 AEB 状态
            if FIRST_WARNING_RANGE[0] <= step_count < FIRST_WARNING_RANGE[1]:
                first_collision_warning = True
            elif SECOND_WARNING_RANGE[0] <= step_count < SECOND_WARNING_RANGE[1]:
                second_collision_warning = True
            elif EMERGENCY_BRAKING_RANGE[0] <= step_count < EMERGENCY_BRAKING_RANGE[1]:
                emergency_braking = True
            
            # 调用 AEB 接口设置状态
            simulator.set_aeb_status(
                vehicle_id=target_vehicle,
                emergency_braking=emergency_braking,
                first_collision_warning=first_collision_warning,
                second_collision_warning=second_collision_warning
            )
            
            # 设置车辆控制信息（保持匀速行驶）
            ste_wheel = 0.0
            lon_acc = 0.05
            simulator.set_vehicle_control_info(
                target_vehicle, ste_wheel, lon_acc
            )

            # 执行仿真器步骤
            step_res = simulator.step()
            step_count += 1
            
            # 检查仿真状态
            if not step_res.code.is_running():
                print(f"[Step {step_count}] 仿真结束，状态码：{step_res.code.value}, 消息：{step_res.message}")
                break
            
            # 每 10 步打印一次进度
            if step_count % 10 == 0:
                print(f"[Step {step_count}] 仿真进行中...")

        print("-" * 60)
        print(f"✓ 仿真完成，总共执行 {step_count} 步")

        # 6. 打印查看链接
        print("\n查看任务:")
        print(f"  https://qianxing.risenlighten.com/#/configuration/circleTask?id={task_id}")
        print("\n查看回放:")
        print(f"  https://qianxing.risenlighten.com/#/sampleRoad/cartest/?id={task_id}&record_id={new_record.new_record_id}&sim_record_id={new_record.sim_record_id}")

    finally:
        # 7. 停止仿真器，释放服务器资源
        simulator.stop()
        print("\n✓ 仿真器已停止")


if __name__ == "__main__":
    main()
