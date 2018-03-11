FROM ubuntu:artful-20180123

###### Builder Boilerplate ####################################################
ADD build /usr/bin/
RUN chmod +x /usr/bin/build
CMD 'build'
###############################################################################

RUN apt-get update --fix-missing && \
    apt-get install -y \
        build-essential \
        libblas-dev \
        libfreetype6-dev \
        libffi-dev \
        liblapack-dev \
        libldap2-dev \
        libpng-dev \
        libpq-dev \
        libsasl2-dev \
        libssl-dev \
        libxml2-dev \
        libxslt-dev \
        pkg-config \
        python3.6-dev \
        python3-pip

RUN pip3 install \
    pipenv


# Virtualenv / PipEnv
ENV PYTHON_VERSION 3.6
ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8s
ENV PIPENV_SHELL_FANCY 1
ENV PIPENV_VENV_IN_PROJECT 1
ENV PIPENV_NOSPIN 1
