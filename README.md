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


---

Desarrollado como Proyecto Aplicado, este entorno está diseñado para una **reproducibilidad absoluta** dentro de contenedores Docker y GitHub Codespaces. Ya que en servicio de nube Colab Google, esta limita por versiones de scrapy antiguas que requiere el cicflowmeter de la CIC de UNB


  File "/content/micromamba/envs/cic38/lib/python3.8/ctypes/util.py", line 100, in _is_elf
    with open(filename, 'br') as thefile:
FileNotFoundError: [Errno 2] No such file or directory: b'liblibc.a'
---------------------------------------------------------------------------
CalledProcessError                        Traceback (most recent call last)
/tmp/ipykernel_14454/144793733.py in <cell line: 0>()
----> 1 get_ipython().run_cell_magic('bash', '', 'set -e\n\nexport MAMBA_ROOT_PREFIX=/content/micromamba\n\nPCAP="/content/drive/MyDrive/TG-Esp-DataScience-Analytics/pcap_files/DoS-TCP_Flood10.pcap"\nOUTDIR="/content/cicflow_work"\nmkdir -p "$OUTDIR"\n\nrm -f "$OUTDIR/DoS-TCP_Flood10.csv"\n\n/content/bin/micromamba run -n cic38 cicflowmeter -f "$PCAP" -c "$OUTDIR/DoS-TCP_Flood10.csv"\n\necho "Archivo generado:"\nls -lh "$OUTDIR/DoS-TCP_Flood10.csv"\necho\necho "Primeras líneas:"\nhead -n 5 "$OUTDIR/DoS-TCP_Flood10.csv"\n')

4 frames
<decorator-gen-103> in shebang(self, line, cell)

/usr/local/lib/python3.12/dist-packages/IPython/core/magics/script.py in shebang(self, line, cell)
    243             sys.stderr.flush()
    244         if args.raise_error and p.returncode!=0:
--> 245             raise CalledProcessError(p.returncode, cell, output=out, stderr=err)
    246 
    247     def _run_script(self, p, cell, to_close):

CalledProcessError: Command 'b'set -e\n\nexport MAMBA_ROOT_PREFIX=/content/micromamba\n\nPCAP="/content/drive/MyDrive/TG-Esp-DataScience-Analytics/pcap_files/DoS-TCP_Flood10.pcap"\nOUTDIR="/content/cicflow_work"\nmkdir -p "$OUTDIR"\n\nrm -f "$OUTDIR/DoS-TCP_Flood10.csv"\n\n/content/bin/micromamba run -n cic38 cicflowmeter -f "$PCAP" -c "$OUTDIR/DoS-TCP_Flood10.csv"\n\necho "Archivo generado:"\nls -lh "$OUTDIR/DoS-TCP_Flood10.csv"\necho\necho "Primeras l\xc3\xadneas:"\nhead -n 5 "$OUTDIR/DoS-TCP_Flood10.csv"\n'' returned non-zero exit status 1.

<img width="1818" height="858" alt="image" src="https://github.com/user-attachments/assets/60a93243-c3a1-4c92-afd1-8379105b2223" />
---




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

El pipeline de la aplicación de los diferentes modelos de Clasificación Multiclase, 8 Family y Binario
* XGBoost
* LightGBM
* CatBoost 
* HistGradientBoosting
Como los Random Forest, son tan pesados, Superiores a 2GB en su almacenamiento, se hace dificil su implemnetación en Nube, de manera Free. Pues la idea, en mi caso, no es pagar servicios cloud dedicados, o de Nube Privada.


## Reflexiones de Aplicación a muestras de ejemplo y Transición a MLOps

La materialización de este pipeline en un entorno Cloud interactivo nació de un planteamiento propuesto de manera personal, de manera clara: trascender las tradicionales diapositivas de sustentación. La intención es proporcionar tanto a los jurados, como al director, como dejar plasmado en mis repositorios Github que debo ir creciendo, a modo de portafolio y proyectos trabajados, un enlace directo en su navegador para realizar una defensa interactiva, convirtiendo los Notebooks de Jupyter en una herramienta metodológica viva que expone paso a paso de la arquitectura y ciencia de datos y el modelo predictivo en total funcionalidad y aplicado.

Además, esta decisión responde a una estrategia de mitigación de riesgos tecnológicos. Aunque el proyecto del Modelo de aprendizaje automatico supervisado fue diseñado y desarrollado originalmente en un entorno on-premises sobre Linux (Ubuntu) utilizando el IDE Spyder, las plataformas de videoconferencia como MS Teams suelen presentar inestabilidades históricas en sistemas UNIX durante sesiones de alta demanda. Para garantizar la plena certeza de la conexión durante la sustentación virtual, la presentación se realizará desde un equipo local con Windows 11, delegando todo el cómputo intensivo y las dependencias de red a la nube.

De esta forma, la implementación se eleva a un escenario de MLOps a muy pequeña escala, dando alcance directo y práctico al tercer objetivo específico del proyecto: comprobar la eficacia y el poder de generalización del modelo frente a muestras de tráfico masivo no vistas, ejecutando inferencias en un escenario de tiempo cercano al real (near real-time).


### El Reto Técnico: De Google Colab a Contenedores Docker
La migración de un entorno local a la nube representó el mayor desafío técnico de esta fase. Un despliegue que toma apenas un par de días en una máquina Ubuntu local, requirió más de una semana de investigación y adaptación en servicios Cloud.

Inicialmente, el esfuerzo se centró en Google Colab, plataforma utilizada habitualmente en las actividades académicas de la Universidad. Sin embargo, las políticas restrictivas de dicho entorno generaron colisiones insalvables con las dependencias de bajo nivel requeridas por la herramienta oficial de la Universidad de New Brunswick (CIC). La incompatibilidad entre versiones antiguas de scapy, cicflowmeter y el kernel de Python 3.8 de Colab provocó fallos de ejecución en el subproceso y la generación de archivos .csv corruptos o vacíos, arrojando excepciones críticas del sistema:

La superación de este obstáculo requirió explorar caminos alternativos de Cloud Computing fuera de las herramientas preconfiguradas. A través del autoaprendizaje, la solución definitiva se logró orquestando un contenedor Docker a medida mediante GitHub Codespaces. Este enfoque no solo resolvió los conflictos de compatibilidad de red a nivel de sistema operativo, sino que permitió afianzar competencias avanzadas en infraestructura en la nube, resultando en un entorno de reproducibilidad absoluta.

## Nota sobre el Dashboard 📊 de Detección (IDS)
Cabe mencionar que el dashboard integrado para la monitorización de alertas en el Notebook final, construido mediante seaborn y matplotlib, presenta un diseño funcional e intencionalmente sencillo. El desarrollo de interfaces gráficas o visualizaciones avanzadas de ciberseguridad escapa al alcance formal de los objetivos propuestos en este Proyecto Aplicado. Su propósito fundamental es metodológico: ilustrar el flujo continuo de predicciones y constatar visualmente el excelente desempeño del algoritmo al clasificar intrusiones complejas en secuencias temporales casi reales.


##  Troubleshooting y FAQ

**Q: Al procesar mi PCAP masivo, el entorno devuelve el error `Return: -15`**
* **A:** Este error corresponde a un `SIGTERM` por agotamiento de RAM. Verifica que el parámetro `CHUNK_SIZE_MB` en `scripts/config.py` esté ajustado a `20`. El pipeline fragmentará el archivo automáticamente para proteger la memoria de Codespaces.

**Q: ¿Por qué usar Python 3.8.18?**
* **A:** Es la versión que garantiza compatibilidad estricta entre la versión nativa de `cicflowmeter` disponible en PyPI y `scapy==2.4.3`, logrando la extracción óptima de 84 características de red.

      
