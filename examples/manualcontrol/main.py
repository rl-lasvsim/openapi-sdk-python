"""
手动控制示例的主入口。
"""
import argparse

from manual_control import ControlConfig, ManualControl


def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(
        description="一个处理w/s/a/d输入来控制千行仿真的命令行工具"
    )
    parser.add_argument("--task-id", type=int, required=True,
                      help="任务ID")
    parser.add_argument("--record-id", type=int, required=True,
                      help="剧本ID")
    parser.add_argument("--vehicle", type=str, default="测试车辆1",
                      help="要控制的车辆（默认：测试车辆1）")
    parser.add_argument("--ste-wheel", type=float, default=30.0,
                      help="每次按键的方向盘转角（默认：30.0）")
    parser.add_argument("--lon-acc", type=float, default=5.0,
                      help="每次按键的纵向加速度（默认：5.0）")
    
    args = parser.parse_args()

    # 创建控制配置
    config = ControlConfig.new(
        ste_wheel=args.ste_wheel,
        lon_acc=args.lon_acc
    )

    # 创建并启动手动控制
    control = ManualControl(config)
    control.start(args.task_id, args.record_id, args.vehicle)


if __name__ == "__main__":
    main()
