# Ixian.docker

Ixian.docker is a [ixian]() based utility for implementing docker 
build processes. It includes an implementation of a [multi-stage builder 
pattern](docker.md#pattern). It has builders and tasks for some common build steps.

For more information tasks provided by these modules:
* [Docker](docs/docker.md)
* [Python + Pipenv](docs/python.md)
* [Node + NPM](docs/npm.md)
* [Webpack](docs/webpack.md)
* [Django](docs/django.md)

## Installation


``` 
pip install ixian.docker
```

## Setup

#### Add modules in ixian.py

Add modules for the desired build steps. This will enable their configuration
and tasks.

The [Docker module](docs/docker.md) provides the base 
[project layout](docs/docker.md#layout) used by the other modules. It must be 
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
    'ixian.modules.bower',
)
```

#### Use Tasks

Tasks can be run using `ixian`. Use `--help` to list tasks.

```
ix --help
```

Show help for a task.

```
ix compose --help
```

Show build tree for a task.

```
ix compose --show
```
