#!/bin/bash
set -e

pushd $APP_DIR

$BOWER --config.interactive=false --allow-root install $BOWER_CONFIG

popd
