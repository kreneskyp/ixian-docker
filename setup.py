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

# from ixian_docker import VERSION


DIR = os.path.dirname(os.path.realpath(__file__))

requirements_path = f"{DIR}/requirements.txt"
requirements = [
    str(ir.req) for ir in parse_requirements(requirements_path, session=PipSession())
]


setup(
    name="ixian-docker",
    description="Docker modules for jack-tar.",
    version="0.0.1",
    author="Peter Krenesky",
    author_email="kreneskyp@gmail.com",
    maintainer="Peter Krenesky",
    maintainer_email="kreneskyp@gmail.com",
    keywords="tasks, shovel, rake, make, ixian, ix, docker",
    long_description=open("%s/README.md" % DIR, "r").read(),
    url="https://github.com/kreneskyp/ixian-docker",
    packages=["ixian_docker"],
    package_dir={"ixian_docker": "ixian_docker"},
    install_requires=requirements,
    pbr=True,
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Build Tools ",
    ],
)
