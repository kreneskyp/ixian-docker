import os
from setuptools import find_packages, setup

from pip.download import PipSession
from pip.req import parse_requirements

from power_shovel import VERSION


DIR = os.path.dirname(os.path.realpath(__file__))

requirements_path = '%s/requirements.txt' % DIR
requirements = [
    str(ir.req)
    for ir in parse_requirements(requirements_path, session=PipSession())]

setup(
    name='power_shovel.docker',
    version=VERSION,
    author='Peter Krenesky',
    author_email='kreneskyp@gmail.com',
    maintainer='Peter Krenesky',
    maintainer_email='kreneskyp@gmail.com',
    keywords='tasks, shovel, rake, make, power_shovel, docker',
    description='Docker multi-stage builder for power_shovel.',
    long_description=open('%s/README.md' % DIR, 'r').read(),
    url='https://github.com',
    packages=['power_shovel_docker'],
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ]
)
