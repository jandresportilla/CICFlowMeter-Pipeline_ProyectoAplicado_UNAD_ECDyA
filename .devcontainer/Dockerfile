FROM python:3.8.18-bullseye

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    tcpdump \
    libpcap-dev \
    build-essential \
    gcc \
    g++ \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip

RUN pip install \
    numpy \
    scipy \
    pandas \
    tqdm \
    requests \
    scapy==2.4.3 \
    cicflowmeter==0.1.6 \
    jupyterlab \
    ipykernel
