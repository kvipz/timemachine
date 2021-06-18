from setuptools import setup

setup(
name = "TimeConverter",
version = "0.0.1",
author = "Vipin Kumar",

package_dir = {"": "src"},
packages = ["package_main"],
entry_points = {
    'console_scripts': [
        'tc=package_main.cli:tc'
        ],
    },
install_requires=[
    'click >= 8.0.0',
    ]
)
