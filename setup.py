from setuptools import setup

setup(
name = "timemachine",
version = "0.0.1",
author = "Vipin Kumar",
author_email = "k.vipz88@gmail.com",
description = "A template for Python package",

package_dir = {"": "src"},
packages = ["package_main"],

# packages = find_packages(
#    where = "src"
#)

entry_points = {
    'console_scripts': [
        'tm=package_main.cli:tm'
        ],
    },
install_requires=[
    'click >= 8.0.0',
    ]
)
