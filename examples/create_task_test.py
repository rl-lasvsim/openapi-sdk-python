#!/usr/bin/env python3
"""
CreateTask API 测试示例

演示如何使用 ListScenarios 获取场景列表，然后使用 CreateTask 创建仿真任务，
最后初始化仿真并运行。
"""

import os
from dotenv import load_dotenv

# 加载环境变量（从 workspace 根目录的 .env.local 文件）
env_file = "/home/hone/data/openapisdk/.env.local"
load_dotenv(env_file)

from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.process_task_model import ScenarioRef
from lasvsim_openapi.simulator_model import SimulatorConfig


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
    MAX_SIM_STEP = 10  # 最大仿真步数（测试用，设小一点）
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
        create_res = client.process_task.create_task(
            name=TASK_NAME,
            scene_v2_infos=SCENE_INFOS,
            folder_id=FOLDER_ID,
        )

        task_id = create_res.id
        record_ids = create_res.record_ids

        print(f"✅ 任务创建成功!")
        print(f"   任务 ID: {task_id}")
        print(f"   记录 ID 列表：{record_ids}")
        print()

        # 检查是否有记录 ID
        if not record_ids or len(record_ids) == 0:
            print("❌ 没有生成记录 ID，无法启动仿真")
            return

        record_id = record_ids[0]
        print(f"使用第一个记录 ID: {record_id}")
        print()

        print("=" * 60)
        print("Step 3: 初始化仿真")
        print("=" * 60)
        print(f"场景 ID: {first_scenario.id}")
        print(f"场景版本：{first_scenario.asset_version}")
        print(f"记录 ID: {record_id}")
        print("-" * 60)

        # 初始化仿真器
        sim_config = SimulatorConfig(
            scen_id=str(first_scenario.asset_id),
            scen_ver=first_scenario.asset_version,
            sim_record_id=str(record_id),
        )
        sim_config.max_step = MAX_SIM_STEP

        simulator = client.init_simulator_from_config(sim_config)

        print(f"✅ 仿真初始化成功!")
        print(f"   仿真 ID: {simulator.simulator_fast.simulation_id}")
        print()

        print("=" * 60)
        print("Step 4: 运行仿真（测试步数：{}）".format(MAX_SIM_STEP))
        print("=" * 60)
        print("-" * 60)

        # 运行仿真（逐步执行）
        step_count = 0
        try:
            for i in range(MAX_SIM_STEP):
                print(f"   第 {step_count} 步 start")
                step_res = simulator.step()
                print(f"   第 {step_count} 步 end")
                step_count = i + 1
                
                # 检查仿真是否结束
                if not step_res.code.is_running():
                    print(f"✅ 仿真在第 {step_count} 步结束")
                    print(f"   结束码：{step_res.code}")
                    break
                
                print(f"   第 {step_count} 步")
            
            print()
            print(f"✅ 仿真运行完成!")
            print(f"   总步数：{step_count}")
            print()

        except Exception as e:
            print(f"⚠️  仿真运行遇到错误：{type(e).__name__}")
            print(f"   消息：{e}")
            print(f"   已执行步数：{step_count}")
            print()
            print("注意：仿真运行需要仿真引擎支持。")
            print("如果看到 gRPC 相关错误，说明仿真环境未完全配置。")
            print("但 API 调用流程（任务创建、仿真初始化）已验证通过。")
            print()

        # 停止仿真
        print("=" * 60)
        print("Step 5: 停止仿真")
        print("=" * 60)
        
        try:
            stop_res = simulator.stop()
            print(f"✅ 仿真已停止")
            print()
        except Exception as stop_err:
            print(f"⚠️  停止仿真时遇到错误：{type(stop_err).__name__}")
            print(f"   这可能是因为仿真已经异常结束")
            print()
        
        # 执行总结
        print("=" * 60)
        print("📝 执行总结")
        print("=" * 60)
        print(f"✅ 场景列表获取：成功")
        print(f"✅ 任务创建：成功 (ID: {task_id})")
        print(f"✅ 仿真初始化：成功 (ID: {simulator.simulator_fast.simulation_id})")
        if step_count > 0:
            print(f"✅ 仿真运行：部分成功 (执行 {step_count} 步)")
        else:
            print(f"⚠️  仿真运行：未执行或失败")
        print()
        print("🎉 测试完成！")

    except Exception as e:
        print(f"❌ 操作失败：{e}")
        raise


if __name__ == "__main__":
    main()
