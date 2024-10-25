from distutils.core import setup
from setuptools import find_packages

# with open("README.md", mode="r", encoding=UTF_8) as f:
#     readme = f.read()

setup(
    name="qianxing-openapi",
    # version=VERSION,
    description="Qianxing OpenAPI SDK for Python",
    # long_description=readme,
    long_description_content_type="text/markdown",
    author="Zhihong Luo",
    author_email="luozhihong@risenlighten.com",
    url="https://github.com/risenlighten-qianxing/openapi-sdk-python",
    packages=find_packages(),
    install_requires=["requests", "protobuf>3,<4", "httpx"],
    python_requires=">=3.0",
    keywords=["Qianxing", "Lasvsim", "自动驾驶", "OpenAPI"],
    include_package_data=True,
    project_urls={
        "Source": "https://github.com/risenlighten-qianxing/openapi-sdk-python",
    },
)
