import os
from setuptools import setup

try:
    # pip >=20
    from pip._internal.network.session import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    try:
        # 10.0.0 <= pip <= 19.3.1
        from pip._internal.download import PipSession
        from pip._internal.req import parse_requirements
    except ImportError:
        # pip <= 9.0.3
        from pip.download import PipSession
        from pip.req import parse_requirements

# from power_shovel_docker import VERSION


DIR = os.path.dirname(os.path.realpath(__file__))

requirements_path = f"{DIR}/requirements.txt"
requirements = [
    str(ir.req) for ir in parse_requirements(requirements_path, session=PipSession())
]


setup(
    name="jack-tar-docker",
    description="Docker modules for jack-tar.",
    version="0.0.1",
    author="Peter Krenesky",
    author_email="kreneskyp@gmail.com",
    maintainer="Peter Krenesky",
    maintainer_email="kreneskyp@gmail.com",
    keywords="tasks, shovel, rake, make, jack-tar, jt, docker",
    long_description=open("%s/README.md" % DIR, "r").read(),
    url="https://github.com/kreneskyp/jack-tar",
    packages=["power_shovel_docker"],
    package_dir={"power_shovel_docker": "power_shovel_docker"},
    install_requires=requirements,
    pbr=True,
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
)
