def prepare_data(df, features, target):
    required = features + [target]
    missing = [name for name in required if name not in df.columns]
    if missing:
        raise ValueError("Missing required CSV columns: " + ", ".join(missing))
    data = df.copy()
    for name in required:
        data[name] = __import__("pandas").to_numeric(data[name], errors="coerce")
    data = data.dropna(subset=[target])
    data = data[data[target].isin([0, 1])]
    if data.empty:
        raise ValueError("No usable rows. The target must contain 0 or 1.")
    return data
