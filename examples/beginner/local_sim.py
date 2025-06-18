"""
SDK联合仿真示例。

本示例演示如何进行本地联合仿真:
1. 创建联合仿真任务
2. 控制仿真器

"""

import os

from lasvsim_openapi.client import Client, SimulatorConfig
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator_model import SimulatorConfig


def main():
    # 接口地址和授权token
    endpoint = os.getenv(
        "QX_ENDPOINT"
    )  # 线上环境地址: https://qianxing-api.risenlighten.com
    token = os.getenv(
        "QX_TOKEN"
    )  # 登录仿真平台后访问 https://qianxing.risenlighten.com/#/usecenter/personalCenter, 点击最下面按钮复制token

    # 初始化客户端
    cli = Client(
        config=HttpConfig(
            endpoint=endpoint,  # 接口地址
            token=token,  # 授权token
        ),
        local_mode=True,
    )

    # 通过拷贝的场景Id、Version和SimRecordId初始化仿真器
    simulator = cli.init_simulator_from_config(
        SimulatorConfig(
            scen_id='left',
            scen_ver='行人.json',
        )
    )

    try:
        # 获取测试车辆列表
        test_vehicle_list = simulator.get_test_vehicle_id_list()

        # 记录仿真器运行状态(True: 运行中; False: 运行结束), 任务运行过程中持续更新该状态
        is_running = True

        # 使测试车辆环形行驶
        while is_running:
            # 加速直线行驶
            ste_wheel = 0
            lon_acc = 0.05

            # 设置车辆的控制信息
            simulator.set_vehicle_control_info(
                test_vehicle_list.list[0], ste_wheel, lon_acc
            )

            # 执行仿真器步骤
            step_res = simulator.step()
            is_running = step_res.code.is_running()

    finally:
        # 停止仿真器, 释放服务器资源
        simulator.stop()


if __name__ == "__main__":
    main()