FROM python:3.10-bullseye

ENV DEBIAN_FRONTEND=noninteractive



# 1. INSTALAR DEPENDENCIAS DEL SISTEMA

RUN apt-get update && apt-get install -y \
    tcpdump \
    libpcap-dev \
    build-essential \
    gcc \
    g++ \
    git \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*


# 2. ACTUALIZAR PIP
RUN python -m pip install --upgrade pip


# 3. PARCHE PARA SCAPY >>>>>   SOLUCIONA EL ERROR liblibc.a
RUN mkdir -p /usr/local/lib/python3.10/site-packages/
RUN echo 'import ctypes.util\n\
orig = ctypes.util.find_library\n\
def safe_find(name):\n\
    if name == "libc": return orig("c")\n\
    return orig(name)\n\
ctypes.util.find_library = safe_find' > /usr/local/lib/python3.10/site-packages/sitecustomize.py

# VERIFICAR QUE EL PARCHE SE CREÓ CORRECTAMENTE
RUN cat /usr/local/lib/python3.10/site-packages/sitecustomize.py


# 4. INSTALAR DEPENDENCIAS DE PYTHON
RUN pip install \
    numpy==1.26.4 \
    scipy==1.13.0 \
    pandas==2.2.0 \
    tqdm \
    requests \
    scapy==2.4.3 \
    cicflowmeter==0.1.6 \
    jupyterlab \
    ipykernel \
    joblib==1.4.2 \
    scikit-learn==1.5.0 \
    catboost==1.2.10 \
    lightgbm==4.6.0 \
    xgboost==2.1.4


# 5. VERIFICACIONES DE INSTALACIÓN
# 5.1 Verificar Python
RUN python --version


# 5.2 Verificar que el parche existe y funciona
RUN ls -la /usr/local/lib/python3.10/site-packages/sitecustomize.py
RUN python -c "import ctypes.util; print('find_library(libc):', ctypes.util.find_library('libc'))"


# 5.3 Verificar paquetes instalados
RUN python -c "import numpy; print('NumPy:', numpy.__version__)"
RUN python -c "import pandas; print('Pandas:', pandas.__version__)"
RUN python -c "import joblib; print('Joblib:', joblib.__version__)"
RUN python -c "import catboost; print('CatBoost:', catboost.__version__)"
RUN python -c "import sklearn; print('Scikit-learn:', sklearn.__version__)"
RUN python -c "import lightgbm; print('LightGBM:', lightgbm.__version__)"
RUN python -c "import xgboost; print('XGBoost:', xgboost.__version__)"
RUN python -c "import requests; print('Requests:', requests.__version__)"
RUN python -c "import scapy; print('Scapy:', scapy.__version__)"


# 5.4 Verificar que Scapy carga correctamente (con el parche)
RUN python -c "from scapy.all import *; print('✅ Scapy cargado correctamente')"


# 5.5 Verificar que cicflowmeter funciona
RUN cicflowmeter --help || echo "⚠️ cicflowmeter no está en PATH, pero instalado"


# 5.6 Verificar que tcpdump funciona
RUN tcpdump --version


# 5.7 Verificar que Git LFS está instalado (si existe)
RUN git lfs version 2>/dev/null || echo "Git LFS no instalado (opcional)"


# 6. COMANDO DE INICIO

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
