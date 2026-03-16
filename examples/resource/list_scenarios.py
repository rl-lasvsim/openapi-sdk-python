#!/usr/bin/env python3
"""
ListScenarios API 测试示例

演示如何使用 ListScenarios API 获取场景列表。
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# 加载环境变量（从 workspace 根目录的 .env.local 文件）
root_dir = Path(__file__).parent.parent.parent.parent
env_file = root_dir / ".env.local"
load_dotenv(env_file)

from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig


def main():
    # 初始化客户端
    config = HttpConfig(
        endpoint=os.getenv("QX_ENDPOINT", "http://localhost:8000"),
        token=os.getenv("QX_TOKEN", "your-token-here"),
    )
    client = Client(config=config)

    # ========== 配置区域 ==========
    FOLDER_ID = 0       # 文件夹 ID（可选，0 表示根目录）
    PAGE_NUM = 1        # 页码
    PAGE_SIZE = 10      # 每页数量
    # ============================

    print(f"获取场景列表")
    print(f"文件夹 ID: {FOLDER_ID}")
    print(f"分页：第 {PAGE_NUM} 页，每页 {PAGE_SIZE} 个")
    print("-" * 50)

    try:
        # 获取场景列表
        response = client.resources.list_scenarios(
            folder_id=FOLDER_ID,
            page_num=PAGE_NUM,
            page_size=PAGE_SIZE,
        )

        print(f"✅ 获取成功!")
        print(f"   场景数量：{len(response.list)}")
        print(f"   总数量：{response.page.total if response.page else 'N/A'}")
        print()

        # 打印场景列表
        for i, item in enumerate(response.list, 1):
            print(f"   {i}. {item.name}")
            print(f"      ID: {item.id}")
            print(f"      资产 ID: {item.asset_id}")
            print(f"      版本：{item.asset_version}")
            print(f"      描述：{item.desc}")
            print()

    except Exception as e:
        print(f"❌ 获取失败：{e}")
        raise


if __name__ == "__main__":
    main()
