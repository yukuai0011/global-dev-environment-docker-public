FROM ubuntu:latest

ARG PYTHON_REQUIREMENTS_URL

ENV SSH_PRIVATE_KEY \
    SSH_PUBLIC_KEY \
    GIT_USER_NAME \
    GIT_USER_EMAIL \
    PYTHON_SCRIPT_SETUP_URL \
    PYTHON_REQUIREMENTS_URL=$PYTHON_REQUIREMENTS_URL

RUN apt-get update && apt-get install -y \
    git \
    git-lfs \
    python3 \
    nodejs \
    curl 


