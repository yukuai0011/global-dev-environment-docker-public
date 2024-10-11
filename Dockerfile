FROM ubuntu:latest

ARG PYTHON_REQUIREMENTS_URL
ARG PYTHON_SCRIPT_SETUP_URL

RUN apt-get update \
    && apt-get install -y \
    git \
    git-lfs \
    python3 \
    nodejs \
    curl \
    && curl -o requirements.txt $PYTHON_REQUIREMENTS_URL \
    && curl -o setup.py $PYTHON_SCRIPT_SETUP_URL \
    && pip3 install -r requirements.txt \