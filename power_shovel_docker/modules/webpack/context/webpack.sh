#!/bin/bash
set -e

pushd $APP_DIR
$WEBPACK \
	--progress \
	--colors \
	--context $PROJECT_DIR \
	--config $WEBPACK_CONFIG \
	--output-path $WEBPACK_OUTPUT_DIR $@
popd
