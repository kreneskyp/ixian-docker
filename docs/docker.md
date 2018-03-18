# Docker

Core docker layout and other utility tasks. Features for creating images and
running containers are included. 

## Features
### Layout
TODO describe the layout defined by the docker module

* /srv - project
* /srv/my_project

### Multi-stage Builder Pattern
TODO describe the multi-stage builder pattern.

### Auto-volumes
Builder modules may specify `volumes` and `dev_volumes` that will be mounted in 
prod and dev environments. This allows modules to contribute build artifacts to
the runtime. The modules are mounted automatically by `compose` and `run`

## Config
## Targets
## Tasks
## Utils
