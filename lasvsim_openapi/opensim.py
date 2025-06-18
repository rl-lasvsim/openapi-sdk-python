import platform
import sysconfig
from pathlib import Path
import urllib3
import os
import subprocess
import atexit
import socket

# 禁用 SSL 警告（仅测试用，生产环境应配置正确证书）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

download_urls = {
    "Windows": {
        "x86_64": "https://example.com/windows-x86_64.exe",
        "x86": "https://example.com/windows-x86.exe",
    },
    "Linux": {
        "x86_64": "https://qianxing.risenlighten.com/desktop-release/opensim/opensim",
        "arm64": "https://example.com/linux-arm64.bin",
    },
    "Darwin": {  # macOS
        "x86_64": "https://example.com/macos-x86_64",
        "arm64": "https://qianxing.risenlighten.com/desktop-release/opensim/opensim-darwin-arm64",
    },
}

dest_ext = {
    "Windows": ".exe",
    "Linux": "",
    "Darwin": "",
}

def get_system_arch():
    """获取操作系统架构（x86_64, arm64, etc.）"""
    machine = platform.machine().lower()
    if machine in ("x86_64", "amd64"):
        return "x86_64"
    elif machine in ("arm64", "aarch64"):
        return "arm64"
    elif machine.startswith("arm"):
        return "arm"
    elif machine == "i386":
        return "x86"
    else:
        return machine  # 其他架构（如 riscv, ppc64le 等）

def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 0))  # 0表示随机端口
        s.listen(1)
        port = s.getsockname()[1]
    return port

def get_python_bin_dir():
    """获取 Python 的 bin/Scripts 目录"""
    if platform.system() == "Windows":
        return Path(sysconfig.get_path("scripts"))
    else:
        return Path(sysconfig.get_path("scripts"))  # 或 sysconfig.get_path("purelib") / "../bin"


class OpensimRunConfig:
    sys_arch: str
    download_url: str
    dest_path: Path
    run_dir: Path
    run_port: int

    def __init__(self):
        system = platform.system()

        self.sys_arch = get_system_arch()
        self.download_url = download_urls[system][self.sys_arch]
        self.run_dir = get_python_bin_dir()
        self.run_port = get_free_port()  # 默认端口
        self.dest_path =  self.run_dir / ("opensim"+dest_ext[system])

def download_file(url, save_path):
    # 创建连接池
    http = urllib3.PoolManager()
    
    # 发送 GET 请求
    response = http.request('GET', url, preload_content=False)
    
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # 写入文件
        with open(save_path, 'wb') as out:
            while True:
                data = response.read(1024)
                if not data:
                    break
                out.write(data)
    finally:
        # 释放连接
        response.release_conn()


def run_opensim() -> OpensimRunConfig:
    """运行 OpenSim"""
    config = OpensimRunConfig()
    
    # 检查是否已存在文件
    if not config.dest_path.exists():
        # 下载 OpenSim
        print(f"Downloading Opensim from {config.download_url} to {config.dest_path}")
        download_file(config.download_url, config.dest_path)
        # 设置可执行权限（Linux/macOS）
        if platform.system() != "Windows":
            config.dest_path.chmod(0o755)
        print(f"Opensim downloaded to {config.dest_path}. You can run it using:")

    # 方式2：启动后不等待它结束
    process = subprocess.Popen([config.dest_path, 'run','--addr', f':{config.run_port}', '--local_resource'],
                            # stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,text=True)
    atexit.register(lambda: process.terminate())
    print(f"opensim started（PID: {process.pid}）, address: http://localhost:{config.run_port}")
    print(f"data dir: {os.getcwd()}/data/scenarios")
    return config

def upgrade_opensim():
    """更新 OpenSim"""
    config = OpensimRunConfig()

    print(f"Downloading Opensim from {config.download_url} to {config.dest_path}")
    download_file(config.download_url, config.dest_path)
    # 设置可执行权限（Linux/macOS）
    if platform.system() != "Windows":
        config.dest_path.chmod(0o755)
    print(f"OpenSim upgraded to {config.dest_path}")


# upgrade_opensim()
# run_opensim()
# import time
# time.sleep(3)  # 等待 OpenSim 启动
# python -c "import lasvsim_openapi.opensim;lasvsim_openapi.opensim.upgrade_opensim()"