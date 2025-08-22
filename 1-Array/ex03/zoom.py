from load_image import ft_load
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


def main():
    """
    Main function to load an image, crop a specific region, extract its first
    channel, convert it to a NumPy array, and display the result. Prints the
    shape and contents of the processed array. Handles file and image errors
    gracefully.

    Steps:
    1. Constructs the image path relative to the script location.
    2. Loads the image as a NumPy array using `ft_load`.
    3. Crops a 400x400 region from coordinates (450, 100).
    4. Extracts the first channel of the cropped image.
    5. Converts the result to a NumPy array and adds a new axis.
    6. Prints the new shape and array contents.
    7. Displays the cropped image.
    8. Handles exceptions such as file not found, image errors, and empty
    arrays.
    """
    img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "animal.jpeg")
    arr = ft_load(img_path)
    print_first_and_last(arr) if arr.size != 0 else exit(1)

    try:
        with Image.open(img_path) as im:
            im = crop_squared(im, (450, 100), 400)
            im = im.getchannel(0)
            arr = np.array(im)
            assert arr.size > 0, "image array is empty"
            arr = arr[:, :, np.newaxis]
            print(f"New shape after slicing: {arr.shape} or {arr.shape[0:-1]}")
            print_first_and_last(arr)
            im.show()
    except (FileNotFoundError, UnidentifiedImageError, ValueError,
            PermissionError, AssertionError) as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
