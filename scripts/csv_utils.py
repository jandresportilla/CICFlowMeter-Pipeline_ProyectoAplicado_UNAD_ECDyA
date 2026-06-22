import pandas as pd
from pathlib import Path
from scripts.logger import get_logger

logger = get_logger("CSV_Utils")

def merge_chunks(csv_files: list, final_output: Path):
    """Une los CSV generados por cicflowmeter, limpiando los encabezados redundantes."""
    if not csv_files:
        logger.error("No hay archivos CSV para consolidar.")
        return None
        
    logger.info("Consolidando fragmentos CSV...")
    df_list = []
    for f in csv_files:
        try:
            df_temp = pd.read_csv(f)
            df_list.append(df_temp)
        except Exception as e:
            logger.error(f"Error leyendo {f.name}: {e}")
            
    df_final = pd.concat(df_list, ignore_index=True)
    df_final.to_csv(final_output, index=False)
    
    for f in csv_files:
        f.unlink() # Limpiar chunks
        
    logger.info(f"Archivo consolidado guardado en {final_output.name} con {df_final.shape[0]} filas.")
    return df_final
