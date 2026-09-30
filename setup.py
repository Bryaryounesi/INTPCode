from setuptools import setup, find_packages

setup(
    name="cvtools",
    version="0.2.0",
    author="Bryar Younesi",
    author_email="bryaryounesi@gmail.com",
    license="Custom Source-Available (BUSL-1.1 style)",
    packages=find_packages(include=["cvtools", "cvtools.*"]),
    install_requires=[
        "opencv-python",
        "numpy",
        "pandas",
    ],
    python_requires=">=3.10",
)
