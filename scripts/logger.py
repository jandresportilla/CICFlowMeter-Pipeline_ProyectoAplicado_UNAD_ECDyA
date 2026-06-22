import logging
import sys
from scripts.config import LOG_DIR

LOG_DIR.mkdir(parents=True, exist_ok=True)

def get_logger(name="Pipeline"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # Consola
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        
        # Archivo
        fh = logging.FileHandler(LOG_DIR / "pipeline.log")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger
