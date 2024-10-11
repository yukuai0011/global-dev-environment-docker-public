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
    && curl -O https://example.com/script.sh \
    && chmod +x script.sh
