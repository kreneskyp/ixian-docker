#!/bin/sh

# pushd $PROJECT_DIR
pushd /srv/ixian_tests/project
nosetests $@
popd
