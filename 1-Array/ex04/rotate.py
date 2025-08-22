import numpy as np
from PIL import Image, UnidentifiedImageError
import os


def print_first_and_last(arr: np.ndarray):
    """
    Prints the first three elements of the first and last rows of a NumPy
    array.

    Parameters:
        arr (np.ndarray): A 2D NumPy array.

    Output:
        Prints the first three elements of the first row, an ellipsis, and the
        first three elements of the last row,
        formatted to indicate the start and end of the array.
    """
    print(f"[{arr[0][0:3]}")
    print("...")
    print(f"{arr[-1][0:3]}]")


def crop_squared(im: Image.Image, top_left_corner: tuple[float, float],
                 side_px: float) -> Image.Image:
    """
    Crops a square region from the given image starting at the specified
    top-left corner.

    Args:
        im (Image.Image): The input image to crop.
        top_left_corner (tuple[float, float]): The (left, upper) coordinates
        of the top-left corner of the square crop.
        side_px (float): The length of the sides of the square crop in pixels.

    Returns:
        Image.Image: The cropped square region as a new image.
    """
    (left, upper) = top_left_corner
    (right, lower) = (left + side_px, upper + side_px)
    return im.crop((left, upper, right, lower))


def traspose_2d_array(arr: np.ndarray) -> np.ndarray:
    """
    Transposes a 2D NumPy array (matrix), swapping its rows and columns.

    Parameters:
        arr (np.ndarray): A 2D NumPy array to be transposed.

    Returns:
        np.ndarray: The transposed 2D NumPy array.

    Raises:
        ValueError: If the input array is not at least 2-dimensional.

    Example:
        >>> import numpy as np
        >>> arr = np.array([[1, 2], [3, 4]])
        >>> traspose_2d_array(arr)
        array([[1, 3],
               [2, 4]])
    """
    height, width = arr.shape[:2]
    new_arr = np.empty((width, height), dtype=arr.dtype)
    for i in range(width):
        for j in range(height):
            new_arr[i, j] = arr[j, i].item()
    return new_arr


def create_new_image(arr: np.ndarray) -> Image.Image:
    """
    Creates a grayscale PIL Image from a 2D NumPy array.

    Args:
        arr (np.ndarray): A 2D NumPy array representing pixel intensity values.

    Returns:
        Image.Image: A PIL Image object in grayscale mode ("L") with pixel
        values set from the input array.

    Raises:
        ValueError: If the input array is not at least 2-dimensional.
    """
    height, width = arr.shape[:2]
    im = Image.new("L", (width, height))
    for i in range(width):
        for j in range(height):
            im.putpixel((i, j), int(arr[j, i]))
    return im


def zoom_step(img_path: str) -> np.ndarray:
    """
    Processes an image by cropping it to a square, extracting the
    first channel, and reshaping the array.

    Args:
        img_path (str): The file path to the image to be processed.

    Returns:
        np.ndarray: The processed image as a NumPy array with an added channel
        dimension.

    Raises:
        AssertionError: If the resulting image array is empty.

    Side Effects:
        Prints the shape of the processed image and the first and last
        elements of the array.

    Note:
        Requires the functions `crop_squared` and `print_first_and_last` to be
        defined elsewhere.
        Assumes the use of the PIL.Image and numpy libraries.
    """
    with Image.open(img_path) as im:
        im = crop_squared(im, (450, 100), 400)
        im = im.getchannel(0)
    arr = np.array(im)
    assert arr.size > 0, "image array is empty"
    arr = arr[:, :, np.newaxis]
    print(
        f"The shape of the image is: {arr.shape} "
        f"or {arr.shape[0:-1]}"
    )
    print_first_and_last(arr)
    return arr


def main():
    dir_name = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(dir_name, "animal.jpeg")

    try:
        new_arr = traspose_2d_array(zoom_step(img_path))
        print(f"New shape after Transpose: {new_arr.shape}")
        row0 = np.array2string(new_arr[0], threshold=10, edgeitems=3)
        rown = np.array2string(new_arr[-1], threshold=10, edgeitems=3)
        print(f"[{row0}")
        print(" ...")
        print(f" {rown}]")
        new_im = create_new_image(new_arr)
        new_im.show()
    except (FileNotFoundError, UnidentifiedImageError, ValueError,
            PermissionError, AssertionError) as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
