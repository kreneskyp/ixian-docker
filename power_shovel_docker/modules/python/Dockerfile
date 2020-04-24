# ==================================================
#  Python
# ==================================================
ARG FROM_REPOSITORY
ARG FROM_TAG
FROM ${FROM_REPOSITORY}:${FROM_TAG}

COPY root/srv/wet_arms/etc/python $APP_ENV_DIR/etc/python

RUN virtualenv venv
RUN . $APP_ENV_DIR/venv/bin/activate; pip install -r ./etc/python/requirements.txt \
 && . $APP_ENV_DIR/venv/bin/activate; pip install -r ./etc/python/requirements-dev.txt
