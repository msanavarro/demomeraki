'''
Created on 23 jul. 2020

@author: msanavarro
'''
from setuptools import find_packages, setup

setup(
    name='server',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
