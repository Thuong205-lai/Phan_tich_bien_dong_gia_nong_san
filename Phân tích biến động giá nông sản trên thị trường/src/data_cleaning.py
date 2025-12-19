import pandas as pd


def load_excel(path):
    # engine openpyxl để đọc .xlsx
    df = pd.read_excel(path, engine="openpyxl")
    df.columns = [c.strip() for c in df.columns]
    return df


def clean_prices(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Chuẩn hoá tên cột giá (nếu file là "Gia(VND/kg)" hoặc "Giá(VND/kg)")
    for c in df.columns:
        if "Gia" in c or "Giá" in c:
            if c != "Gia":
                df = df.rename(columns={c: "Gia"})
            break

    # Chuẩn hoá text
    df["LoaiNongSan"] = df["LoaiNongSan"].astype(str).str.strip()

    # Ép kiểu số
    df["Thang"] = pd.to_numeric(df["Thang"], errors="coerce")
    df["Nam"] = pd.to_numeric(df["Nam"], errors="coerce")
    df["Gia"] = pd.to_numeric(df["Gia"], errors="coerce")  # "abc" -> NaN

    # Tạo Date
    df["Date"] = pd.to_datetime(
        dict(year=df["Nam"], month=df["Thang"], day=1),
        errors="coerce",
    )

    # Loại bản ghi lỗi Date / thiếu LoaiNongSan
    df = df.dropna(subset=["Date", "LoaiNongSan"]).sort_values(["LoaiNongSan", "Date"])

    # FIX CHÍNH: dùng transform để giữ index khớp dataframe
    # Nội suy theo thứ tự thời gian trong từng loại
    df["Gia_clean"] = (
        df.groupby("LoaiNongSan", sort=False)["Gia"]
        .transform(lambda s: s.interpolate(method="linear").ffill().bfill())
    )

    return df
