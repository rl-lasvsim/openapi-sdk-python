"""
联合仿真 set_vehicle_control_info 接口测试脚本。

测试新增的控制参数:
- drive_force_front_axle: 前轴驱动力 [N]
- drive_force_rear_axle: 后轴驱动力 [N]
- brake_force_fl: 左前轮制动力 [N]
- brake_force_fr: 右前轮制动力 [N]
- brake_force_rl: 左后轮制动力 [N]
- brake_force_rr: 右后轮制动力 [N]

环境变量:
- QX_ENDPOINT: API 地址 (可选，默认线上环境)
- QX_TOKEN: 授权 token
- QX_TASK_ID: 任务 ID
- QX_RECORD_ID: 剧本 ID
"""

import os
import time

from lasvsim_openapi.client import Client, SimulatorConfig
from lasvsim_openapi.http_client import HttpConfig


def main():
    # ========== 配置 ==========
    endpoint = os.getenv(
        "QX_ENDPOINT", "https://qianxing-api.risenlighten.com"
    )
    token = os.getenv("QX_TOKEN")
    task_id_str = os.getenv("QX_TASK_ID")
    record_id_str = os.getenv("QX_RECORD_ID")

    if not token or not task_id_str or not record_id_str:
        print("错误：请设置环境变量 QX_TOKEN, QX_TASK_ID, QX_RECORD_ID")
        print("示例:")
        print("  export QX_TOKEN='your_token'")
        print("  export QX_TASK_ID='123'")
        print("  export QX_RECORD_ID='456'")
        return

    task_id = int(task_id_str)
    record_id = int(record_id_str)

    print(f"连接仿真平台：{endpoint}")
    print(f"任务 ID: {task_id}, 剧本 ID: {record_id}")
    print("-" * 60)

    # ========== 初始化 ==========
    cli = Client(
        HttpConfig(
            endpoint=endpoint,
            token=token,
        )
    )

    # 拷贝剧本
    print("1. 拷贝剧本...")
    new_record = cli.process_task.copy_record(task_id, record_id)
    print(f"   新剧本 ID: {new_record.new_record_id}")

    # 初始化仿真器
    print("2. 初始化仿真器...")
    simulator = cli.init_simulator_from_config(
        SimulatorConfig(
            scen_id=new_record.scen_id,
            scen_ver=new_record.scen_ver,
            sim_record_id=new_record.sim_record_id,
        )
    )

    try:
        # 获取测试车辆列表
        test_vehicle_list = simulator.get_test_vehicle_id_list()
        if not test_vehicle_list.list:
            print("错误：未找到测试车辆")
            return

        vehicle_id = test_vehicle_list.list[0]
        print(f"3. 测试车辆：{vehicle_id}")
        print("-" * 60)

        # ========== 测试用例 ==========
        test_cases = [
            {
                "name": "基础控制 - 方向盘 + 加速度",
                "params": {"ste_wheel": 5.0, "lon_acc": 0.1},
                "steps": 10,
            },
            {
                "name": "前轴驱动力控制",
                "params": {"drive_force_front_axle": 500.0},
                "steps": 10,
            },
            {
                "name": "后轴驱动力控制",
                "params": {"drive_force_rear_axle": 500.0},
                "steps": 10,
            },
            {
                "name": "四轮独立制动 - 前轮",
                "params": {"brake_force_fl": 200.0, "brake_force_fr": 200.0},
                "steps": 10,
            },
            {
                "name": "四轮独立制动 - 后轮",
                "params": {"brake_force_rl": 200.0, "brake_force_rr": 200.0},
                "steps": 10,
            },
            {
                "name": "组合控制 - 驱动力 + 制动",
                "params": {
                    "drive_force_front_axle": 300.0,
                    "brake_force_rl": 100.0,
                    "brake_force_rr": 100.0,
                },
                "steps": 10,
            },
            {
                "name": "组合控制 - 方向盘 + 驱动力",
                "params": {
                    "ste_wheel": 3.0,
                    "drive_force_rear_axle": 400.0,
                },
                "steps": 10,
            },
        ]

        for i, case in enumerate(test_cases, 1):
            print(f"\n测试 {i}/{len(test_cases)}: {case['name']}")
            print(f"   参数：{case['params']}")

            is_running = True
            step_count = 0

            while is_running and step_count < case["steps"]:
                # 调用 set_vehicle_control_info
                simulator.set_vehicle_control_info(
                    vehicle_id=vehicle_id,
                    **case["params"],
                )

                # 执行一步仿真
                step_res = simulator.step()
                is_running = step_res.code.is_running()
                step_count += 1

                # 每步输出车辆状态
                if step_count % 5 == 0:
                    moving_info = simulator.get_vehicle_moving_info([vehicle_id])
                    if moving_info.moving_info_dict and vehicle_id in moving_info.moving_info_dict:
                        info = moving_info.moving_info_dict[vehicle_id]
                        print(
                            f"   步骤 {step_count}: "
                            f"速度={info.u:.2f} m/s, "
                            f"加速度={info.u_acc:.4f} m/s²"
                        )

            print(f"   完成 {step_count} 步")
            time.sleep(0.5)  # 短暂间隔

        print("-" * 60)
        print("\n✅ 所有测试完成!")

        # 输出结果链接
        print(f"\n查看任务：https://qianxing.risenlighten.com/#/configuration/circleTask?id={task_id}")
        print(f"查看回放：https://qianxing.risenlighten.com/#/sampleRoad/cartest/?id={task_id}&record_id={new_record.new_record_id}&sim_record_id={new_record.sim_record_id}")

    finally:
        # 停止仿真器
        print("\n停止仿真器...")
        simulator.stop()
        print("完成")


if __name__ == "__main__":
    main()
