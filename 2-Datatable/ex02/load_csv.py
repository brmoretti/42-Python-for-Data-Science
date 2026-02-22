import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        path (str): The file path to the CSV file to be loaded.

    Returns:
        pd.DataFrame | None: A pandas DataFrame containing the data from the
                            CSV file, or None if an exception occurs during
                            loading.

    Prints:
        - On success: The dimensions of the loaded dataset in the format
          "Loading dataset of dimensions: (rows, columns)".
        - On failure: The exception type and error message in the format
          "{ExceptionType} : {error_message}".

    Examples:
        >>> df = load("data.csv")
        Loading dataset of dimensions: (1000, 10)
        >>> df.shape
        (1000, 10)
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions: {df.shape}")
    except Exception as e:
        print(f"{type(e).__name__} : {e}")
        return None
    return df
