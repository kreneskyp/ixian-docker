# Power_shovel.docker

Power_shovel.docker is a [power_shovel]() based utility for implementing docker 
build processes. It includes an implementation of a [multi-stage builder 
pattern](docker.md#pattern). It has builders and tasks for some common build steps.

For more information tasks provided by these modules:
* [Docker](docs/docker.md)
* [Python + Pipenv](docs/python.md)
* [Node + NPM](docs/npm.md)
* [Webpack](docs/webpack.md)
* [Django](docs/django.md)

## Installation

TODO: Not in pypi yet but eventually...

``` 
pip install power_shovel.docker
```

## Setup

#### Add modules in shovel.py

Add modules for the desired build steps. This will enable their configuration
and tasks.

The [Docker module](docs/docker.md) provides the base 
[project layout](docs/docker.md#layout) used by the other modules. It must be 
enabled for the others to function. 

```python
from power_shovel.config import CONFIG
from power_shovel.module import load_modules

CONFIG.PROJECT_NAME = 'my_project'
load_modules(
    'power_shovel.modules.docker',
    'power_shovel.modules.python',
    'power_shovel.modules.django',
    'power_shovel.modules.npm',
    'power_shovel.modules.webpack',
    'power_shovel.modules.bower',
)
```

#### Use Tasks

Tasks can be run using `shovel`. Use `--help` to list tasks.  

```
shovel --help 
```

Show help for a task.

```
shovel compose --help 
```

Show build tree for a task.

```
shovel compose --show 
```
