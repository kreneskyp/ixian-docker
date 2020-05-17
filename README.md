# Ixian.docker

Ixian.docker is an [ixian](https://github.com/kreneskyp/ixian) utility for implementing docker 
build processes. It includes a non-linear implementation of a [multi-stage builder 
pattern](docker.md#pattern). It has builders and tasks for some common build steps.

For more information tasks provided by these modules:
* [Docker](docs/bak/docker.md)
* [Python + Pipenv](docs/bak/python.md)
* [Node + NPM](docs/bak/npm.md)
* [Webpack](docs/bak/webpack.md)
* [Django](docs/django.md)

## Installation


``` 
pip install ixian.docker
```

## Setup

#### Add modules in ixian.py

Add modules for the desired build steps. This will enable their configuration
and tasks.

The [Docker module](docs/bak/docker.md) provides the base 
[project layout](docs/bak/docker.md#layout) used by the other modules. It must be 
enabled for the others to function. 

```python
from ixian.config import CONFIG
from ixian.module import load_modules

CONFIG.PROJECT_NAME = 'my_project'
load_modules(
    'ixian.modules.docker',
    'ixian.modules.python',
    'ixian.modules.django',
    'ixian.modules.npm',
    'ixian.modules.webpack',
)
```

#### Use Tasks

Tasks can be run using `ixian`. Use `--help` to list tasks.

```
ix help
```

Show help for a task

```
ix compose --help
```

Show ixian builtin help and status for task

```
ix --help compose
```
