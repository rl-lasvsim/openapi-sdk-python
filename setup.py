from distutils.core import setup
from setuptools import find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Read requirements from requirements.txt


def parse_requirements(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip() and not line.startswith("#")]


setup(
    name="lasvsim-openapi",
    version="0.1.15",
    description="Lasvsim OpenAPI SDK for Python - A client library for accessing Lasvsim's simulation platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Zhihong Luo",
    author_email="luozhihong@risenlighten.com",
    url="https://github.com/rl-lasvsim/openapi-sdk-python",
    packages=find_packages(),
    install_requires=[
        "urllib3>=2.3.0",
        "ujson>=5.10.0",
    ],
    python_requires=">=3.0",
    keywords=["Qianxing", "Lasvsim", "自动驾驶",
              "OpenAPI", "Simulation", "Autonomous Driving"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        "Source": "https://github.com/rl-lasvsim/openapi-sdk-python",
        "Bug Reports": "https://github.com/rl-lasvsim/openapi-sdk-python/issues",
    },
)
