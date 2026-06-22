import subprocess
import time
from pathlib import Path
from scripts.logger import get_logger
from scripts.config import TMP_DIR, CHUNK_SIZE_MB

logger = get_logger("CICFlow")

def extract_features(pcap_path: Path, output_csv: Path) -> bool:
    """Extrae características dividiendo el PCAP en chunks para evitar OOM Killer (-15)."""
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    chunk_prefix = TMP_DIR / "chunk_"
    
    logger.info(f"Fragmentando PCAP {pcap_path.name} en bloques de {CHUNK_SIZE_MB}MB...")
    split_cmd = ["tcpdump", "-r", str(pcap_path), "-C", str(CHUNK_SIZE_MB), "-w", str(chunk_prefix)]
    subprocess.run(split_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    chunks = sorted(list(TMP_DIR.glob("chunk_*")))
    if not chunks:
        logger.error("Fallo al fragmentar el archivo PCAP.")
        return False
        
    logger.info(f"Se generaron {len(chunks)} fragmentos. Iniciando extracción...")
    csv_outputs = []
    
    for i, chunk in enumerate(chunks):
        chunk_csv = chunk.with_suffix(".csv")
        cmd = ["cicflowmeter", "-f", str(chunk), "-c", str(chunk_csv)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        
        if r.returncode == 0 and chunk_csv.exists():
            csv_outputs.append(chunk_csv)
        else:
            logger.warning(f"Error en chunk {i+1}: {r.stderr}")
        chunk.unlink() # Liberar espacio inmediatamente
        
    return csv_outputs
