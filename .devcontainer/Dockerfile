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


# 3. EL TRUCO MAESTRO: Crear un parche transparente para Python 3.8
# Esto intercepta la llamada interna defectuosa de Scapy y la corrige automáticamente
RUN echo 'import ctypes.util\n\
orig = ctypes.util.find_library\n\
def safe_find(name):\n\
    if name == "libc": return orig("c")\n\
    return orig(name)\n\
ctypes.util.find_library = safe_find' > /usr/local/lib/python3.8/site-packages/sitecustomize.py

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
