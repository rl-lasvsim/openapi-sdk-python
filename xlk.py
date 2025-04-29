import os
import sys

from lasvsim_openapi.client import Client, SimulatorConfig
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator_model import SimulatorConfig
from lasvsim_openapi.simulator_model import Obstacle


def xlk():
    endpoint = "http://qianxing-api.risenlighten.com"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjcsIm9pZCI6MTAxLCJuYW1lIjoi572X5b-X5rSqIiwiaWRlbnRpdHkiOiJub3JtYWwiLCJwZXJtaXNzaW9ucyI6W10sImlzcyI6InVzZXIiLCJzdWIiOiJMYXNWU2ltIiwiZXhwIjoxNzQzNzUxNzI0LCJuYmYiOjE3NDMxNDY5MjQsImlhdCI6MTc0MzE0NjkyNCwianRpIjoiNyJ9.jm0DKwVtYjdcnKbdSiTgAzacU4lDcdH2CFOE6mVHb4w"
    # 登录仿真平台，选择想要进行联合仿真的任务及剧本
    task_id = 11219  # 替换为你的任务ID
    record_id = 27008  # 替换为你的剧本ID

    # 1. 初始化客户端
    cli = Client(
        HttpConfig(
            endpoint=endpoint,  # 接口地址
            token=token,  # 授权token
        )
    )

    # # 2. 拷贝剧本, 返回的结构中new_record_id字段就是新创建的剧本ID
    # # 仿真结束后可到该剧本下查看结果详情
    # new_record = cli.process_task.copy_record(task_id, record_id)

    # # 3. 通过拷贝的场景Id、Version和SimRecordId初始化仿真器
    # simulator = cli.init_simulator_from_config(
    #     SimulatorConfig(
    #         scen_id=new_record.scen_id,
    #         scen_ver=new_record.scen_ver,
    #         sim_record_id=new_record.sim_record_id,
    #     )
    # )

    res = cli.process_task.get_record_scenario(task_id, record_id)
    simulator = cli.init_simulator_from_config(
        SimulatorConfig(
            scen_id=res.scen_id,
            scen_ver=res.scen_ver,
        )
    )
    try:
        # 获取测试车辆列表
        test_vehicle_list = simulator.get_test_vehicle_id_list()

        # 记录仿真器运行状态(True: 运行中; False: 运行结束), 任务运行过程中持续更新该状态
        is_running = True

        # 使测试车辆环形行驶
        while is_running:
            res = simulator.get_vehicle_reference_lines(test_vehicle_list.list[0])
            if (
                len(res.reference_lines) > 1
                # and len(res.reference_lines[1].lane_ids) > 0
                # and res.reference_lines[1].lane_ids[0] == "d089_5757_1895_bd6b"
                and len(res.reference_lines[1].points) == 4
            ):
                print("xxxxxxxxx", res, "\n")

            # 执行仿真器步骤
            step_res = simulator.step()
            is_running = step_res.code.is_running()

        # 可在此处继续调用其他接口, 查看联合仿真文档: https://www.risenlighten.com/#/union

        # 仿真结束后, 到千行仿真平台对应的taskId/recordId下查看联合仿真结果详情
        print(
            f"查看任务: https://qianxing.risenlighten.com/#/configuration/circleTask?id={task_id}"
        )

        # 如想直接查看本次联合仿真的回放视频, 可访问下面网址：
        # print(
        #     f"查看回放: https://qianxing.risenlighten.com/#/sampleRoad/cartest/?id={task_id}&record_id={new_record.new_record_id}&sim_record_id={new_record.sim_record_id}"
        # )

    finally:
        # 停止仿真器, 释放服务器资源
        simulator.stop()


if __name__ == "__main__":
    xlk()
