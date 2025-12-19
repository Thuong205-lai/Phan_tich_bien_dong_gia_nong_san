import numpy as np
import pandas as pd


def quality_report(df: pd.DataFrame) -> dict:
    df = df.copy()

    # Tỉ lệ giá gốc bị lỗi (abc/NaN)
    invalid_price_rate_raw = float(df["Gia"].isna().mean())

    # Outlier theo z-score trên Gia_clean, từng loại
    def outlier_count(s: pd.Series) -> int:
        std = s.std(ddof=0)
        if std == 0 or np.isnan(std):
            return 0
        z = (s - s.mean()) / std
        return int((z.abs() > 3).sum())

    outliers = df.groupby("LoaiNongSan")["Gia_clean"].apply(outlier_count).to_dict()

    return {
        "rows": int(len(df)),
        "n_products": int(df["LoaiNongSan"].nunique()),
        "date_min": str(df["Date"].min().date()),
        "date_max": str(df["Date"].max().date()),
        "missing_rate_by_col": df.isna().mean().round(4).to_dict(),
        "invalid_price_rate_raw": round(invalid_price_rate_raw, 4),
        "outliers_count_by_product": outliers,
    }
