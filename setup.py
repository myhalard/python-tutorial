from setuptools import setup

setup(
    name="yourcli",
    version="0.0.1",
    py_modules=["cli_tool"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "cli-tool = cli_tool:cli",
        ],
    },
)
