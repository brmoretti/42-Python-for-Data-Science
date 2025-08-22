import numpy as np
from PIL import Image


def _assertions(array: np.ndarray):
    """
    Validates that the input NumPy array is a non-empty, 3-dimensional RGB
    image array with only non-negative values.

    Parameters:
        array (np.ndarray): The input array to validate.

    Raises:
        AssertionError: If the array is empty.
        AssertionError: If any value in the array is negative.
        AssertionError: If the array does not have exactly 3 dimensions.
        AssertionError: If the third dimension does not have exactly 3
        channels (RGB).
    """

    assert array.size > 0, "empty array"
    assert np.all(array >= 0), "the array can have only positive RGB values"
    assert array.ndim == 3, (
        "array must have 3 dimensions (width, height and RGB)"
    )
    assert array.shape[2] == 3, "array must have 3 channels (RGB)"


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of an input image represented as a NumPy array.

    Parameters:
        array (np.ndarray): The input image as a NumPy array. Must be a valid
        image array.

    Returns:
        np.ndarray: The color-inverted image as a NumPy array. Returns an
        empty array if input validation fails.

    Side Effects:
        Displays the inverted image using PIL's Image.show().

    Raises:
        AssertionError: If the input array does not meet the required
        conditions (handled internally).
    """
    try:
        _assertions(array)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return np.array([])
    image = 255 - array
    Image.fromarray(image).show()
    return image


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Extracts the red channel from an RGB image and returns a new image with
    only the red channel preserved.

    Parameters:
        array (np.ndarray): A 3-dimensional NumPy array representing an RGB
        image.

    Returns:
        np.ndarray: A NumPy array of the same shape as the input, where only
        the red channel is preserved and the green and blue channels are set
        to zero. Returns an empty array if input validation fails.

    Side Effects:
        Displays the resulting image with only the red channel using PIL's
        Image.show().

    Raises:
        AssertionError: If the input array does not meet the required
        conditions (handled internally).
    """
    try:
        _assertions(array)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return np.array([])
    red = array[:, :, 0]
    image = np.zeros_like(array)
    image[:, :, 0] = red
    Image.fromarray(image).show()
    return image


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Extracts the green channel from an RGB image and returns a new image with
    only the green channel preserved.

    Parameters:
        array (np.ndarray): A 3-dimensional NumPy array representing an RGB
        image.

    Returns:
        np.ndarray: A NumPy array of the same shape as the input, where only
        the green channel is preserved and the red and blue channels are set
        to zero. Returns an empty array if input validation fails.

    Side Effects:
        Displays the resulting image with only the green channel using PIL's
        Image.show().

    Raises:
        AssertionError: If the input array does not meet the required
        conditions (handled internally).
    """
    try:
        _assertions(array)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return np.array([])
    green = array[:, :, 1]
    image = np.zeros_like(array)
    image[:, :, 1] = green
    Image.fromarray(image).show()
    return image


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Extracts the blue channel from an RGB image and returns a new image with
    only the blue channel preserved.

    Parameters:
        array (np.ndarray): A 3-dimensional NumPy array representing an RGB
        image.

    Returns:
        np.ndarray: A NumPy array of the same shape as the input, where only
        the blue channel is preserved and the green and red channels are set
        to zero. Returns an empty array if input validation fails.

    Side Effects:
        Displays the resulting image with only the blue channel using PIL's
        Image.show().

    Raises:
        AssertionError: If the input array does not meet the required
        conditions (handled internally).
    """
    try:
        _assertions(array)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return np.array([])
    blue = array[:, :, 2]
    image = np.zeros_like(array)
    image[:, :, 2] = blue
    Image.fromarray(image).show()
    return image


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts a color image represented as a NumPy array to its grayscale
    version.

    This function takes a 3D NumPy array representing an RGB image, computes
    the grayscale value for each pixel by averaging the red, green, and blue
    channels, and returns a new NumPy array where each pixel has the same
    value for all three channels (R=G=B=grey).
    The resulting grayscale image is displayed using PIL's Image.show().

    Parameters:
        array (np.ndarray): A 3D NumPy array of shape (height, width, 3)
        representing an RGB image.

    Returns:
        np.ndarray: A 3D NumPy array of the same shape as the input, where
        each pixel is grayscale. Returns an empty array if input validation
        fails.

    Raises:
        AssertionError: If the input array does not meet the required
        conditions (handled internally).
    """
    try:
        _assertions(array)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return np.array([])
    red = array[:, :, 0].astype(np.uint16)
    green = array[:, :, 1].astype(np.uint16)
    blue = array[:, :, 2].astype(np.uint16)
    grey = ((red + green + blue) / 3).astype(np.uint8)
    image = np.stack((grey, grey, grey), axis=-1)
    Image.fromarray(image).show()
    return image
