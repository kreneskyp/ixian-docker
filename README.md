# Ixian.docker

Ixian.docker is an [ixian](https://github.com/kreneskyp/ixian) utility for implementing docker 
build processes. It includes a non-linear implementation of a [multi-stage builder 
pattern](docker.md#pattern). It has builders and tasks for some common build steps.

For more main docs:
https://ixian-docker.readthedocs.io


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
# ixian.py
from ixian.config import CONFIG
from ixian.module import load_module

def init():
    CONFIG.PROJECT_NAME = 'my_project'
    load_module('ixian.modules.docker')
    load_module('ixian.modules.python')
    load_module('ixian.modules.django')
    load_module('ixian.modules.npm')
    load_module('ixian.modules.webpack')
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
