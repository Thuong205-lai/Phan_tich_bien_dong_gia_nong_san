from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_RAW = BASE_DIR / "data" / "raw"
DATA_PROCESSED = BASE_DIR / "data" / "processed"
REPORTS = BASE_DIR / "reports"

RAW_XLSX = DATA_RAW / "giathitruong_nongsan.xlsx"   # đúng tên file của em
CLEAN_CSV = DATA_PROCESSED / "prices_clean.csv"
QUALITY_JSON = REPORTS / "tables" / "data_quality.json"
