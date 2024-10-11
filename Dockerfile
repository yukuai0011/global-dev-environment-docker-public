FROM ubuntu:latest

ARG PYTHON_REQUIREMENTS_URL
ARG PYTHON_SCRIPT_SETUP_URL

RUN apt-get update \
    && apt-get install -y \
    git \
    git-lfs \
    python3-pip \
    python3-full \
    nodejs \
    curl \
    build-essential \
    libglu1-mesa \
    libxi6 \
    libxrender1 \
    libxmu6 \
    libglu1-mesa-dev \
    libxi-dev \
    libxrender-dev \
    libxmu-dev \
    && curl -o requirements.txt $PYTHON_REQUIREMENTS_URL \
    && curl -o setup.py $PYTHON_SCRIPT_SETUP_URL

RUN pip3 install --upgrade -r requirements.txt --break-system-packages --no-dependencies || true
