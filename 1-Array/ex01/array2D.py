import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list (matrix) between the specified start and end indices
    along the first axis (rows).

    Args:
        family (list): A 2D list (list of lists) where each sublist represents
        a row.
        start (int): The starting index for the slice (inclusive).
        end (int): The ending index for the slice (exclusive).

    Returns:
        list: A new 2D list containing the sliced rows.

    Raises:
        TypeError: If 'family' is not a list, or if 'start' or 'end' are not
        integers, or if any element in 'family' is not a list.
        ValueError: If the sublists in 'family' do not all have the same
        length.

    Side Effects:
        Prints the shape of the original and sliced arrays.
    """
    try:
        if not isinstance(family, list):
            raise TypeError("family must be a list")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("start and end must be integers")
        if not all(isinstance(item, list) for item in family):
            raise TypeError("All elements in family must be lists")
        line_length = len(family[0])
        if not all(len(item) == line_length for item in family):
            raise AssertionError("Each line has to have the same length")
        arr = np.array(family)
        print(f"My shape is : {arr.shape}")
        arr = arr[start:end]
        print(f"My new shape is : {arr.shape}")
        return arr.tolist()
    except Exception as e:
        print(f"Error on slice_me function: {e}")
        return []
