[![Python 3.8.18](https://img.shields.io/badge/python-3.8.18-blue.svg)](https://www.python.org/downloads/release/python-3818/)
[![Scapy 2.4.3](https://img.shields.io/badge/scapy-2.4.3-green.svg)](https://scapy.net/)
[![CICFlowMeter](https://img.shields.io/badge/cicflowmeter-0.1.6-orange.svg)](https://pypi.org/project/cicflowmeter/)

# CICFlowMeter Pipeline - Aplicación del Objetivo 3 del Proyecto de Grado

##Analizar la capacidad de generalización del modelo con mayor eficacia mediante su evaluación en el conjunto de prueba y con datos no vistos del dataset CIC IoT 2023.

**Producción / Inferencia --->>  MLOps**

<img width="629" height="556" alt="image" src="https://github.com/user-attachments/assets/e8490ed6-e695-471b-ba2d-b86a434b0f25" />


Pipeline de la Data, desde la Transformación de un Paquekt Capture .pcap a un archivo de Variables Separadas por Comas .csv, para alli aplicar el Modelo Predictivo ya desarrolado en flujos de tráfico de red No vistos

La Finalidad es montar un devcontainer en GitHub Codespaces que use Python 3.8.18, scapy 2.4.3 y cicflowmeter 0.1.6, igual que en mi Ubuntu on-premises 100% funcional

  Ing. Jaime Andres Portilla Jaimes
  
     Ingeniero en Telecomunicaciones
     Optar el Título de Especializasta en Ciencia de Datos y Analítica
    Escuela de Ciencias Básicas, Tecnología e Ingeniería ECBTI
    Universidad Nacional Abierta y a Distancia UNAD
      Matrícula Profesional: SN290-159014
      Resolución 135   14 Diciembre 2021


      japortillaj@unadvirtual.edu.co

      andres.portilla@unipamplona.edu.co



Desarrollado como Proyecto Aplicado, este entorno está diseñado para una **reproducibilidad absoluta** dentro de contenedores Docker y GitHub Codespaces. Ya que en servicio de nube Colab Google, esta limita por versiones de scrapy antiguas que requiere el cicflowmeter de la CIC de UNB

##  Arquitectura del Pipeline

El flujo de trabajo se divide en dos capas principales:
1. **Motor de Extracción (`scripts/`):** Supera las limitaciones de RAM (OOM Killer) implementando fragmentación (Chunking) de archivos `.pcap` mediante `tcpdump` antes de pasar por `cicflowmeter`.
2. **Capa Analítica (`notebooks/`):** Ejecución secuencial y documentada para experimentación de Machine Learning.

##  Instalación y Reproducibilidad

El proyecto está preconfigurado con un `Dockerfile` que solventa dependencias de bajo nivel (como el bug de `ctypes` de Python 3.8 y la necesidad de `libpcap-dev`).

**Para ejecutar en Codespaces:**
1. Haz clic en `Code` > `Codespaces` > `Create codespace on main`.
2. El contenedor instalará automáticamente todas las dependencias.
3. Abre la carpeta `notebooks/` y ejecuta secuencialmente del `01` al `05`.

## Resultados y Modelos Soportados

El pipeline entrena, compara y extrae la interpretabilidad (SHAP Values) de algoritmos del estado del arte:
* Random Forest & Extra Trees
* XGBoost & LightGBM
* CatBoost & HistGradientBoosting

Evaluado rigurosamente mediante métricas tolerantes al desbalance de clases (MCC, Balanced Accuracy, Precision-Recall AUC).

##  Troubleshooting y FAQ

**Q: Al procesar mi PCAP masivo, el entorno devuelve el error `Return: -15`**
* **A:** Este error corresponde a un `SIGTERM` por agotamiento de RAM. Verifica que el parámetro `CHUNK_SIZE_MB` en `scripts/config.py` esté ajustado a `20`. El pipeline fragmentará el archivo automáticamente para proteger la memoria de Codespaces.

**Q: ¿Por qué usar Python 3.8.18?**
* **A:** Es la versión que garantiza compatibilidad estricta entre la versión nativa de `cicflowmeter` disponible en PyPI y `scapy==2.4.3`, logrando la extracción óptima de 84 características de red.

      
