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


def main():
    # 接口地址和授权token
    endpoint = os.getenv(
        "QX_ENDPOINT"
    )  # 线上环境地址: https://qianxing-api.risenlighten.com
    token = os.getenv(
        "QX_TOKEN"
    )  # 登录仿真平台后访问 https://qianxing.risenlighten.com/#/usecenter/personalCenter, 点击最下面按钮复制token

    endpoint = "http://8.146.201.197:30080/test"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjE2LCJvaWQiOjEwMSwibmFtZSI6IuiCluaxiSIsImlkZW50aXR5Ijoibm9ybWFsIiwicGVybWlzc2lvbnMiOltdLCJpc3MiOiJ1c2VyIiwic3ViIjoiTGFzVlNpbSIsImV4cCI6MTc0MjI2NzMzOCwibmJmIjoxNzQxNjYyNTM4LCJpYXQiOjE3NDE2NjI1MzgsImp0aSI6IjE2In0.naAVrCCuGKtrrlc17lxw2ejo4Qvh5-GqpPvIqk00KdE"
    # 登录仿真平台，选择想要进行联合仿真的任务及剧本
    task_id = 8071  # 替换为你的任务ID
    record_id = 10681  # 替换为你的剧本ID

    # 1. 初始化客户端
    cli = Client(
        HttpConfig(
            endpoint=endpoint,  # 接口地址
            token=token,  # 授权token
        )
    )

    # 2. 拷贝剧本, 返回的结构中new_record_id字段就是新创建的剧本ID
    # 仿真结束后可到该剧本下查看结果详情
    new_record = cli.process_task.copy_record(task_id, record_id)

    # 3. 通过拷贝的场景Id、Version和SimRecordId初始化仿真器
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

        # 记录仿真器运行状态(True: 运行中; False: 运行结束), 任务运行过程中持续更新该状态
        is_running = True

        i = 0
        # 使测试车辆环形行驶
        while is_running:
            i += 1
            # 设置方向盘转角10度, 纵向加速度0.05
            ste_wheel = 10.0
            lon_acc = 0.05

            # 设置车辆的控制信息
            simulator.set_vehicle_control_info(
                test_vehicle_list.list[0], ste_wheel, lon_acc
            )

            # 执行仿真器步骤
            step_res = simulator.step()
            is_running = step_res.code.is_running()

        # 可在此处继续调用其他接口, 查看联合仿真文档: https://www.risenlighten.com/#/union

        # 仿真结束后, 到千行仿真平台对应的taskId/recordId下查看联合仿真结果详情
        print(
            f"查看任务: https://qianxing.risenlighten.com/#/configuration/circleTask?id={task_id}"
        )

        # 如想直接查看本次联合仿真的回放视频, 可访问下面网址：
        print(
            f"查看回放: https://qianxing.risenlighten.com/#/sampleRoad/cartest/?id={task_id}&record_id={new_record.new_record_id}&sim_record_id={new_record.sim_record_id}"
        )

    finally:
        # 停止仿真器, 释放服务器资源
        simulator.stop()


if __name__ == "__main__":
    main()
