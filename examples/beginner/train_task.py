"""
训练任务SDK使用示例。

注意: 使用训练功能需要:
- 注册千行仿真平台账号
- 对平台有一定使用经验
- 正确设置环境变量
"""
import os

from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator_model import SimulatorConfig


def main():
    # 接口地址和授权token
    endpoint = os.getenv("QX_ENDPOINT")  # 线上环境地址: https://qianxing-api.risenlighten.com
    token = os.getenv("QX_TOKEN")  # 登录仿真平台后访问 https://qianxing.risenlighten.com/#/usecenter/personalCenter, 点击最下面按钮复制token

    # 登录训练平台, 选择训练任务
    train_id_str = os.getenv("QX_TRAIN_ID")
    train_id = int(train_id_str)

    # 初始化客户端
    cli = Client(HttpConfig(
        endpoint=endpoint,  # 接口地址
        token=token,  # 授权token
    ))

    # 访问千行平台，通过训练任务ID获取场景信息列表
    scene_id_list = cli.train_task.get_scene_id_list(train_id)

    # 通过场景ID和场景Version初始化仿真器(此案例默认使用场景列表中的第一个场景)
    simulator = cli.init_simulator_from_config(SimulatorConfig(
        scen_id=scene_id_list.scene_id_list[0],
        scen_ver=scene_id_list.scene_version_list[0],
    ))

    try:
        # 运行仿真100步
        for _ in range(100):
            simulator.step()

    finally:
        # 停止仿真器, 释放服务器资源
        simulator.stop()


if __name__ == "__main__":
    main()
