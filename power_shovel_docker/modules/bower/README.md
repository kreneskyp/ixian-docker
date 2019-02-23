# Bower

Provides integrations for using bower package manager in Docker images. 

Bower packages are installed in the image. The packages may be updated in local
dev environments using npm tasks.

## Task

##### build_bower
`build_bower`

Install bower packages. This calls `bower.sh` via `compose`. `{BUILD_OPTIONS}` 
are passed in along with command line args.

##### bower
`bower [...]`

Run bower package manager via `compose`.


## Config Options
##### BIN
Path to bower executable in docker image.

Default: `"{NPM.NODE_MODULES_DIR}/.bin/bower"`


##### BUILD_OPTIONS
Options to pass to `{BIN}` when running `build_bower`


##### COMPONENTS_DIR
Location of components directory in docker filesystem. 

Default: `"{DOCKER.APP_DIR}/bower_components"`


##### COMPONENTS_VOLUME
Name of Docker volume that stores bower_components. This volume is mounted 
automatically by `compose`.

Default: `"{PROJECT_NAME}.bower_components"`


##### CONFIG_FILE
Filename of bower config file.

Default: `"bower.json"`


##### CONFIG_FILE_PATH
Full path to bower config file.

Default: `"'{DOCKER.PROJECT_DIR}/{BOWER.CONFIG_FILE}"`


##### MODULE_DIR
Directory where module files are found. This will point to a subdirectory of 
where package is installed. 
