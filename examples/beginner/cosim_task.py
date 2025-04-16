"""
SDK联合仿真示例。

本示例演示如何:
1. 创建联合仿真任务
2. 控制仿真器
3. 查看仿真结果

注意: 使用联合仿真功能需要:
- 注册千行仿真平台账号
- 对平台有一定使用经验
- 正确设置环境变量
"""

import os

from lasvsim_openapi.client import Client, SimulatorConfig
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator_model import SimulatorConfig
from lasvsim_openapi.simulator_model import LocalMap
from lasvsim_openapi.simulator_model import Polygon
from lasvsim_openapi.client_fast import ClientFast

def main():
    # 接口地址和授权token
    endpoint = os.getenv(
        "QX_ENDPOINT"
    )  # 线上环境地址: https://qianxing-api.risenlighten.com
    token = os.getenv(
        "QX_TOKEN"
    )  # 登录仿真平台后访问 https://qianxing.risenlighten.com/#/usecenter/personalCenter, 点击最下面按钮复制token


    task_id_str = os.getenv("QX_TASK_ID")
    record_id_str = os.getenv("QX_RECORD_ID")

    # 登录仿真平台，选择想要进行联合仿真的任务及剧本
    task_id = int(task_id_str)  # 替换为你的任务ID
    record_id = int(record_id_str)  # 替换为你的剧本ID

    # 1. 初始化客户端
    cli = ClientFast(
        HttpConfig(
            endpoint=endpoint,  # 接口地址
            token=token,  # 授权token
        )
    )

    # 2. 拷贝剧本, 返回的结构中new_record_id字段就是新创建的剧本ID
    # 仿真结束后可到该剧本下查看结果详情
    # new_record = cli.process_task.get_record_scenario(task_id, record_id)
    new_record = cli.process_task.copy_record(task_id, record_id)

    # 3. 通过拷贝的场景Id、Version和SimRecordId初始化仿真器
    simulator = cli.init_simulator_from_config(
        SimulatorConfig(
            scen_id=new_record['scen_id'],
            scen_ver=new_record['scen_ver'],
            sim_record_id=new_record['sim_record_id'],
            # scen_id=new_record.scen_id,
            # scen_ver=new_record.scen_ver
        )
    )

    try:
        # 获取测试车辆列表
        test_vehicle_list = simulator.get_test_vehicle_id_list()
        print(f"测试车辆列表: {test_vehicle_list}")
        for i in range(100):
            simulator.step()
        simulator.stop()

    finally:
        # 停止仿真器, 释放服务器资源
        simulator.stop()


if __name__ == "__main__":
    main()