from PIL import Image, UnidentifiedImageError
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

    Raises:
        Prints an error message if the file is not found, the image cannot be
        identified, the file is not a valid image, or the loaded array is
        empty.
    """
    try:
        with Image.open(path) as im:
            arr = np.array(im)
        assert arr.size > 0, f"loaded from {path} array is empty"
        print(f"The shape of image is: {arr.shape}")
        return arr
    except (FileNotFoundError, UnidentifiedImageError, ValueError,
            PermissionError, AssertionError) as e:
        print(f"{type(e).__name__}: {e}")
    return np.array([])
