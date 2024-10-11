FROM ubuntu:latest

ARG PYTHON_REQUIREMENTS_URL
ARG PYTHON_SCRIPT_SETUP_URL

RUN apt-get update \
    && apt-get install -y \
    git \
    git-lfs \
    python3 \
    python3-pip \
    nodejs \
    curl \
    && curl -o requirements.txt $PYTHON_REQUIREMENTS_URL \
    && curl -o setup.py $PYTHON_SCRIPT_SETUP_URL

RUN pip3 --version

RUN pip3 install pandas