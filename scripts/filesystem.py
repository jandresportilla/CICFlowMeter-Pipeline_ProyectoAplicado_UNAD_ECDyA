from scripts.config import PCAP_DIR, CSV_RAW_DIR, TMP_DIR, MODELS_DIR, RESULTS_DIR
from scripts.logger import get_logger

logger = get_logger("FileSystem")

def setup_directories():
    """Crea la estructura de carpetas si no existe."""
    dirs = [PCAP_DIR, CSV_RAW_DIR, TMP_DIR, MODELS_DIR, RESULTS_DIR]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    logger.info("Estructura de directorios verificada y lista.")

def clean_tmp_dir():
    """Limpia archivos temporales remanentes."""
    for f in TMP_DIR.glob("*"):
        f.unlink()
    logger.info("Directorio temporal limpiado.")
