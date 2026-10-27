"""
SDK 感知数据获取示例。

本示例演示如何:
1. 创建联合仿真任务
2. 每个仿真 step 后获取一次感知数据 (第一个 step 执行前也获取一次)

环境变量:
    QX_ENDPOINT   接口地址
    QX_TOKEN      授权token
    QX_TASK_ID    任务ID
    QX_RECORD_ID  剧本ID
    QX_VEHICLE_ID 可选, 被测车辆ID (默认取测试车辆列表第一辆)
    QX_STEPS      可选, 仿真步数 (默认 10)
    QX_INIT_WAIT  可选, 第一个 step 前等待 UE 初始化的秒数 (默认 10)
    QX_OUTDIR     可选, 相机 JPG / 激光雷达 PCD 输出目录 (默认当前目录)
"""

import base64
import os
import time
from datetime import datetime

from lasvsim_openapi.client import Client, SimulatorConfig
from lasvsim_openapi.http_client import HttpConfig, APIError
from lasvsim_openapi.simulator_model import SensorType


def _ts() -> str:
    """当前时间前缀, 毫秒精度, 用于把 SDK 日志与服务端日志对齐。"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


def save_pcd(path: str, frame) -> int:
    """把激光雷达帧写成 PCD v0.7 二进制文件, 返回点数。"""
    raw = base64.b64decode(frame.data) if frame.data else b""
    points = frame.points or len(raw) // 20
    width = frame.width or points
    height = frame.height or 1

    header = (
        "# .PCD v0.7 - Point Cloud Data file format\n"
        "VERSION 0.7\n"
        "FIELDS x y z intensity ring\n"
        "SIZE 4 4 4 4 4\n"
        "TYPE F F F F F\n"
        "COUNT 1 1 1 1 1\n"
        f"WIDTH {width}\n"
        f"HEIGHT {height}\n"
        "VIEWPOINT 0 0 0 1 0 0 0\n"
        f"POINTS {points}\n"
        "DATA binary\n"
    )
    with open(path, "wb") as f:
        f.write(header.encode("ascii"))
        f.write(raw[: points * 20])
    return points


def dump_perception(simulator, vehicle_id, step, cameras, lidars, radars, outdir):
    """获取并保存一次全量感知数据。step 仅用于文件名与日志标识。"""
    print(f"{_ts()} [step {step}]")

    # 相机: data 为 JPEG 载荷的 base64 字符串, 落盘为 .jpg
    for sensor_id in cameras:
        try:
            frame = simulator.get_camera_perception(vehicle_id, sensor_id)
        except APIError as e:
            print(f"{_ts()}   相机 {sensor_id}: 暂无数据 ({e})")
            continue
        jpeg = frame.decode_jpeg()
        if not jpeg:
            print(f"{_ts()}   相机 {sensor_id}: 本帧无图像数据")
            continue
        path = os.path.join(outdir, f"camera_{sensor_id}_step{step:03d}.jpg")
        with open(path, "wb") as f:
            f.write(jpeg)
        print(f"{_ts()}   相机 {sensor_id}: {len(jpeg)} 字节, format={frame.format} -> {path}")

    # 激光雷达: data 为 PCD v0.7 二进制点云的 base64 字符串, 每点 20 字节
    for sensor_id in lidars:
        try:
            frame = simulator.get_lidar_perception(vehicle_id, sensor_id)
        except APIError as e:
            print(f"{_ts()}   激光雷达 {sensor_id}: 暂无数据 ({e})")
            continue
        path = os.path.join(outdir, f"lidar_{sensor_id}_step{step:03d}.pcd")
        points = save_pcd(path, frame)
        print(
            f"{_ts()}   激光雷达 {sensor_id}: {points} 点, "
            f"width={frame.width}, height={frame.height} -> {path}"
        )

    # 毫米波雷达: 返回数组, 每个雷达传感器一项
    for sensor_id in radars:
        try:
            radar_sensors = simulator.get_radar_perception(vehicle_id, sensor_id)
        except APIError as e:
            print(f"{_ts()}   毫米波雷达 {sensor_id}: 暂无数据 ({e})")
            continue
        for radar in radar_sensors:
            print(f"{_ts()}   毫米波雷达 {radar.sensor_id}: {len(radar.objects)} 个目标")
            for obj in radar.objects[:3]:
                print(
                    f"{_ts()}     type={obj.obj_type} range={obj.range:.1f}m "
                    f"radial_vel={obj.radial_vel:.1f}m/s static={obj.is_static}"
                )

    # GNSS / ENU 定位姿态
    try:
        pose = simulator.get_enu_perception(vehicle_id)
        print(
            f"{_ts()}   ENU: enu=({pose.enu_e:.2f}, {pose.enu_n:.2f}, {pose.enu_u:.2f})m "
            f"heading={pose.heading:.2f}° v={pose.velocity:.2f}m/s"
        )
    except APIError as e:
        print(f"{_ts()}   ENU: 暂无数据 ({e})")

    # IMU 采样
    try:
        imu = simulator.get_imu_sample(vehicle_id)
        print(
            f"{_ts()}   IMU: acc=({imu.acc_x:.3f}, {imu.acc_y:.3f}, {imu.acc_z:.3f})m/s² "
            f"gyro=({imu.gyro_x:.4f}, {imu.gyro_y:.4f}, {imu.gyro_z:.4f})rad/s"
        )
    except APIError as e:
        print(f"{_ts()}   IMU: 暂无数据 ({e})")
    print()


def main():
    # 接口地址和授权token
    endpoint = os.getenv("QX_ENDPOINT")
    token = os.getenv("QX_TOKEN")

    # 登录仿真平台, 选择想要进行联合仿真的任务及剧本
    task_id = int(os.getenv("QX_TASK_ID"))
    record_id = int(os.getenv("QX_RECORD_ID"))

    # 可选参数
    vehicle_id = os.getenv("QX_VEHICLE_ID", "")
    steps = int(os.getenv("QX_STEPS", "10"))
    outdir = os.getenv("QX_OUTDIR", ".")
    os.makedirs(outdir, exist_ok=True)

    # 1. 初始化客户端
    cli = Client(
        HttpConfig(
            endpoint=endpoint,
            token=token,
        )
    )

    # 2. 拷贝剧本
    new_record = cli.process_task.copy_record(task_id, record_id)

    # 3. 初始化仿真器
    simulator = cli.init_simulator_from_config(
        SimulatorConfig(
            scen_id=new_record.scen_id,
            scen_ver=new_record.scen_ver,
            sim_record_id=new_record.sim_record_id,
        )
    )

    try:
        # 4. 选择被测车辆
        test_vehicle_list = simulator.get_test_vehicle_id_list()
        if not vehicle_id:
            vehicle_id = test_vehicle_list.list[0]

        # 5. 读取车辆传感器配置, 按类型取出 sensor_id
        sensors = simulator.get_vehicle_sensor_config(vehicle_id).sensors_config
        cameras = [s.sensor_id for s in sensors if s.sensor_type == SensorType.CAMERA]
        lidars = [s.sensor_id for s in sensors if s.sensor_type == SensorType.LIDAR]
        radars = [s.sensor_id for s in sensors if s.sensor_type == SensorType.RADAR]

        print(f"车辆: {vehicle_id}")
        print(f"传感器: camera={len(cameras)} lidar={len(lidars)} radar={len(radars)}")
        print()

        # 6. 第一个 step 执行前取一次
        # init 接口只负责创建并异步拉起仿真, UE 侧初始化与第 0 帧采集都在后台进行,
        # 立刻查询感知会拿到空数据(404)。这里先等待一段时间再查, 用于验证该假设。
        # print(f"等待 {init_wait:.1f}s 让 UE 完成初始化并产出第 0 帧 ...")
        time.sleep(1)

        dump_perception(simulator, vehicle_id, 0, cameras, lidars, radars, outdir)

        # 7. 每个 step 执行后再取一次
        is_running = True
        step = 0
        while is_running and step < steps:
            simulator.set_vehicle_control_info(vehicle_id, ste_wheel=0.0, lon_acc=0.05)
            step_res = simulator.step()
            is_running = step_res.code.is_running()
            step += 1
            dump_perception(simulator, vehicle_id, step, cameras, lidars, radars, outdir)

    finally:
        # 停止仿真器, 释放服务器资源
        simulator.stop()


if __name__ == "__main__":
    main()
