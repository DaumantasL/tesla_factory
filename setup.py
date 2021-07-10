from setuptools import find_packages, setup

with open('README.md') as r:
    readme = r.read()

setup(
    name='pytest_examples',
    version="0.0.1",
    description='Reference package for unit tests',
    long_description=readme,
    packages=find_packages(exclude=('tests')),
    install_requires=[
        
    ],
)
