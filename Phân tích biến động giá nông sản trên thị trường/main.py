import json
from src.config import RAW_XLSX, CLEAN_CSV, QUALITY_JSON, DATA_PROCESSED
from src.data_cleaning import load_excel, clean_prices
from src.data_quality import quality_report


def main():
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    QUALITY_JSON.parent.mkdir(parents=True, exist_ok=True)

    raw = load_excel(RAW_XLSX)
    df = clean_prices(raw)

    # Xuất CSV sạch (Excel mở không lỗi tiếng Việt)
    df.to_csv(CLEAN_CSV, index=False, encoding="utf-8-sig")

    report = quality_report(df)
    QUALITY_JSON.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("Saved:", CLEAN_CSV)
    print("Saved:", QUALITY_JSON)
    print("Done.")


if __name__ == "__main__":
    main()
