from load_image import ft_load
import numpy as np
from PIL import Image, UnidentifiedImageError
import os


def print_first_and_last(arr: np.ndarray):
    print(f"[{arr[0][0:3]}")
    print("...")
    print(f"{arr[-1][0:3]}]")


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

    (left, upper) = (450, 100)
    (right, lower) = (left + 400, upper + 400)

    try:
        with Image.open(img_path) as im:
            im = im.crop((left, upper, right, lower))
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
