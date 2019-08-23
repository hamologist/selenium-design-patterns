from setuptools import find_packages, setup

setup(
    name='selenium-design-patterns',
    version='0.1',
    description='Package for bootstrapping common Selenium design patterns',
    license='MIT',
    install_requires=[
        'selenium',
    ],
    packages=find_packages()
)
