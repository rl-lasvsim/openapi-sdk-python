"""
仿真器手动控制模块。
"""
import os
import sys
from dataclasses import dataclass

from lasvsim_openapi.client import Client
from lasvsim_openapi.http_client import HttpConfig
from lasvsim_openapi.simulator import Simulator

try:
    import curses
except ImportError:
    print("本示例需要curses模块。请先安装它。")
    sys.exit(1)


@dataclass
class ControlConfig:
    """控制配置。"""
    ste_wheel_per_press: float  # "a"、"d"键的方向盘转角增量
    lon_acc_per_press: float  # "s"、"w"键的纵向加速度增量

    @classmethod
    def new(cls, ste_wheel: float, lon_acc: float) -> "ControlConfig":
        """创建新的控制配置。"""
        return cls(ste_wheel_per_press=ste_wheel, lon_acc_per_press=lon_acc)


class ManualControl:
    """仿真器手动控制。"""

    def __init__(self, conf: ControlConfig):
        """初始化手动控制。
        
        参数:
            conf: 控制配置
        """
        self.client = Client(HttpConfig(
            token=os.getenv("QX_TOKEN"),
            endpoint=os.getenv("QX_ENDPOINT"),
        ))
        self.config = conf
        self.simulator: Simulator = None
        self.controlled_vehicle = ""

    def start(self, task_id: int, record_id: int, control_vehicle: str = "测试车辆1"):
        """启动手动控制。
        
        参数:
            task_id: 任务ID
            record_id: 剧本ID
            control_vehicle: 要控制的车辆，默认为"测试车辆1"
        """
        self.controlled_vehicle = control_vehicle

        # 拷贝剧本
        copied_record = self.client.process_task.copy_record(task_id, record_id)

        # 初始化仿真器
        self.simulator = self.client.init_simulator_from_config({
            "scen_id": copied_record.scen_id,
            "scen_ver": copied_record.scen_ver,
            "sim_record_id": copied_record.sim_record_id,
        })

        try:
            self._run_interactive()
        finally:
            # 停止仿真器
            self.simulator.stop()

    def _run_interactive(self):
        """运行交互控制循环。"""
        # 初始化curses
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        try:
            # 打印说明
            stdscr.addstr(0, 0, "输入控制 (w/s/a/d, 按Ctrl+C退出):")
            stdscr.refresh()

            while True:
                # 获取按键输入
                c = stdscr.getch()
                
                if c == ord('w'):
                    self.simulator.set_vehicle_control_info(
                        self.controlled_vehicle, 
                        None, 
                        self.config.lon_acc_per_press
                    )
                    stdscr.addstr(1, 0, "前进 (w)")
                elif c == ord('s'):
                    self.simulator.set_vehicle_control_info(
                        self.controlled_vehicle,
                        None,
                        -self.config.lon_acc_per_press
                    )
                    stdscr.addstr(1, 0, "后退 (s)")
                elif c == ord('a'):
                    self.simulator.set_vehicle_control_info(
                        self.controlled_vehicle,
                        -self.config.ste_wheel_per_press,
                        None
                    )
                    stdscr.addstr(1, 0, "左转 (a)")
                elif c == ord('d'):
                    self.simulator.set_vehicle_control_info(
                        self.controlled_vehicle,
                        self.config.ste_wheel_per_press,
                        None
                    )
                    stdscr.addstr(1, 0, "右转 (d)")
                elif c == 3:  # Ctrl+C
                    break
                else:
                    stdscr.addstr(1, 0, "无效输入。")

                stdscr.clrtoeol()
                stdscr.refresh()

                # 仿真器步进
                self.simulator.step()

        finally:
            # 清理curses
            curses.nocbreak()
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()
