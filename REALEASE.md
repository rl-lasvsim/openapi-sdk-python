# Python SDK 更新说明

本次更新新增支持两个版本的 SDK 客户端：

- **Fast 版本**：高性能优化，适用于性能敏感场景。
- **结构化版本**：返回结构化的 Python 类对象，字段清晰易用，适合结果处理和调试。
- **IDC 训练SDK说明**：使用ClientFast创建clieant,其他的结果和使用方式没有变化。

---

## Fast 版本使用方法

> 更高性能，适用于批量仿真任务或对响应速度有要求的场景。

```python
from lasvsim_openapi.client_fast import ClientFast
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator_model import SimulatorConfig

def main():
    # 1. 初始化客户端
    cli = ClientFast(
        HttpConfig(
            endpoint="{endpoint}",  # 接口地址
            token="{token}",        # 授权 token
        )
    )

    # 2. 创建模拟器
    simulator = cli.init_simulator_from_config(SimulatorConfig(
        scen_id="{scen_id}",
        scen_ver="{scen_ver}",
        sim_record_id="{sim_record_id}",
    ))

    # 3. 执行仿真步骤
    simulator.step()
    simulator.stop()

if __name__ == "__main__":
    main()
```

## 结构化版本使用方法

```python
from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator_model import SimulatorConfig

def main():
    # 1. 初始化客户端
    cli = Client(
        HttpConfig(
            endpoint="{endpoint}",  # 接口地址
            token="{token}",        # 授权 token
        )
    )

    # 2. 创建模拟器
    simulator = cli.init_simulator_from_config(SimulatorConfig(
        scen_id="{scen_id}",
        scen_ver="{scen_ver}",
        sim_record_id="{sim_record_id}",
    ))

    # 3. 执行仿真步骤
    simulator.step()
    simulator.stop()

if __name__ == "__main__":
    main()
```