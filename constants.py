from pathlib import Path

BASE_FILE_DIR = Path("/tmp") # donde almaceno los archivos
ROOT_DIR = Path().resolve().parent # ruta padre donde se encuentra mi proyecto
SQL_DIR = ROOT_DIR / "data-challenge-dbt/sql" # ruta donde estan mis archivos sql
SETTINGS_DIR = ROOT_DIR / "data-challenge-dbt"

# Nombres de tablas
CINE_TABLE_NAME = "raw_cine"
MUSEO_TABLE_NAME = "raw_museo"
BIBLIOTECA_TABLE_NAME = "raw_biblioteca"

# Lista con nombres de las tablas
TABLE_NAMES = [
    CINE_TABLE_NAME,
    MUSEO_TABLE_NAME,
    BIBLIOTECA_TABLE_NAME,
]