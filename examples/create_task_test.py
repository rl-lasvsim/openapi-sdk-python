#!/usr/bin/env python3
"""
CreateTask API 测试示例

演示如何使用 ListScenarios 获取场景列表，然后使用 CreateTask 创建仿真任务。
"""

import os
from dotenv import load_dotenv

# 加载环境变量（从 workspace 根目录的 .env.local 文件）
env_file = "/home/hone/data/openapisdk/.env.local"
load_dotenv(env_file)

from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.process_task_model import ScenarioRef


def main():
    # 初始化客户端
    config = HttpConfig(
        endpoint=os.getenv("QX_ENDPOINT", "http://localhost:8000"),
        token=os.getenv("QX_TOKEN", "your-token-here"),
    )
    client = Client(config=config)

    # ========== 配置区域 ==========
    TASK_NAME = "AEB 测试任务"
    FOLDER_ID = 0  # 可选，0 表示根目录
    # ============================

    print("=" * 60)
    print("Step 1: 获取场景列表")
    print("=" * 60)

    try:
        # 获取场景列表
        scenarios_res = client.resources.list_scenarios(
            folder_id=FOLDER_ID,
            page_num=1,
            page_size=10,
        )

        print(f"✅ 场景列表获取成功!")
        print(f"   当前页数量：{len(scenarios_res.list)}")
        print(f"   总数量：{scenarios_res.page.total if scenarios_res.page else 'N/A'}")
        print()

        # 检查是否有场景
        if not scenarios_res.list or len(scenarios_res.list) == 0:
            print("❌ 没有可用的场景，无法创建任务")
            return

        # 使用第一个场景
        first_scenario = scenarios_res.list[0]
        print(f"选择第一个场景:")
        print(f"   名称：{first_scenario.name}")
        print(f"   ID: {first_scenario.id}")
        print(f"   资产 ID: {first_scenario.asset_id}")
        print(f"   版本：{first_scenario.asset_version}")
        print()

        # 构建场景引用
        SCENE_INFOS = [
            ScenarioRef(
                map_name="test_map",  # 默认地图名称，可根据实际情况调整
                scenario_asset_id=first_scenario.asset_id,
                scenario_asset_version=first_scenario.asset_version,
                scenario_name=first_scenario.name,
                scenario_id=first_scenario.id,  # uint64 类型
                source_record_id=0,  # 如果没有源记录，设为 0
            ),
        ]

        print("=" * 60)
        print("Step 2: 创建仿真任务")
        print("=" * 60)
        print(f"任务名称：{TASK_NAME}")
        print(f"文件夹 ID: {FOLDER_ID}")
        print(f"场景数量：{len(SCENE_INFOS)}")
        print("-" * 60)

        # 创建任务
        response = client.process_task.create_task(
            name=TASK_NAME,
            scene_v2_infos=SCENE_INFOS,
            folder_id=FOLDER_ID,
        )

        print(f"✅ 任务创建成功!")
        print(f"   任务 ID: {response.id}")
        print(f"   记录 ID 列表：{response.record_ids}")
        print()

    except Exception as e:
        print(f"❌ 操作失败：{e}")
        raise


if __name__ == "__main__":
    main()
