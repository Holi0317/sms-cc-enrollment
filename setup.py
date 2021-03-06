#!/usr/bin/env python3
# LICENSE: MIT

from setuptools import setup, find_packages
from enrollment import __version__

setup(
    name='enrollment',
    description='Q&A for 2015 enrollment day',
    version=__version__,
    author='holi0317',
    author_email='holliswuhollis@gmail.com',
    license='MIT',

    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'enrollment = enrollment.enrollment:cli',
        ]
    }
)
