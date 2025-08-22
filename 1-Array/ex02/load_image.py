
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the specified file path and returns it as a NumPy
    array.

    Parameters:
        path (str): The file path to the image.

    Returns:
        np.ndarray: The image represented as a NumPy array. If loading fails,
        returns an empty array.

    Side Effects:
        Prints the shape of the loaded image if successful.
        Prints error messages if loading fails.

    Raises:
        Exception: For any errors encountered during loading. Note that
        AssertionError is handled internally and not raised to the caller.
    """
    try:
        with Image.open(path) as im:
            arr = np.array(im)
            assert arr.size > 0, f"failed to load {path}"
            print(f"The shape of image is: {arr.shape}")
        return arr
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"{type(e).__name__} : {e}")
    return np.array([])
