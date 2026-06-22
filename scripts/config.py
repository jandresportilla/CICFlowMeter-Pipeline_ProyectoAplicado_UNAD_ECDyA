from pathlib import Path

# Rutas Base
BASE_DIR = Path("/workspaces/CICFlowMeter-Pipeline_ProyectoAplicado_UNAD_ECDyA")
PCAP_DIR = BASE_DIR / "pcap_files"
CSV_RAW_DIR = BASE_DIR / "csv_raw"
TMP_DIR = BASE_DIR / ".tmp_cicflowmeter"
LOG_DIR = BASE_DIR / "logs"
MODELS_DIR = BASE_DIR / "outputs/models"
RESULTS_DIR = BASE_DIR / "outputs/results"

# Parámetros de Extracción
CHUNK_SIZE_MB = 20  # Límite seguro para RAM en Codespaces (7.7GB totales)
