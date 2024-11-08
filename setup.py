from distutils.core import setup
from setuptools import find_packages

# with open("README.md", mode="r", encoding=UTF_8) as f:
#     readme = f.read()

# 从 requirements.txt 文件中读取依赖项


def parse_requirements(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip() and not line.startswith("#")]


setup(
    name="qianxing-openapi",
    version="0.1.0",
    description="Qianxing OpenAPI SDK for Python",
    # long_description=readme,
    long_description=open("README.md").read(),
    author="Zhihong Luo",
    author_email="luozhihong@risenlighten.com",
    url="https://github.com/risenlighten-qianxing/openapi-sdk-python",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    python_requires=">=3.0",
    keywords=["Qianxing", "Lasvsim", "自动驾驶", "OpenAPI"],
    include_package_data=True,
    project_urls={
        "Source": "https://github.com/risenlighten-qianxing/openapi-sdk-python",
    },
)
