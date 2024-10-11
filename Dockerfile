FROM ubuntu:latest

ARG SSH_PRIVATE_KEY
ARG SSH_PUBLIC_KEY
ARG GIT_USER_NAME
ARG GIT_USER_EMAIL
ARG PYTHON_SCRIPT_SETUP_URL
ARG PYTHON_REQUIREMENTS_URL

ENV SSH_PRIVATE_KEY=$SSH_PRIVATE_KEY
ENV SSH_PUBLIC_KEY=$SSH_PUBLIC_KEY
ENV GIT_USER_NAME=$GIT_USER_NAME
ENV GIT_USER_EMAIL=$GIT_USER_EMAIL
ENV PYTHON_SCRIPT_SETUP_URL=$PYTHON_SCRIPT_SETUP_URL
ENV PYTHON_REQUIREMENTS_URL=$PYTHON_REQUIREMENTS_URL

RUN apt-get update && apt-get install -y \
    git \
    git-lfs \
    python3 \
    nodejs \


