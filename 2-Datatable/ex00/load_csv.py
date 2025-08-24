import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions: {df.shape}")
    except Exception as e:
        print(f"{type(e).__name__} : {e}")
        return None
    return df
