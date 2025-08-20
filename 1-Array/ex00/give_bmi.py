import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculate the BMI (Body Mass Index) for each pair of height and weight.

    Parameters:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: List of BMI values corresponding to each height and
        weight pair.

    Raises:
        TypeError: If inputs are not lists or contain non-numeric values.
        ValueError: If input lists have different lengths.

    Note:
        Height must be provided in meters and weight in kilograms for correct
        results.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must be lists")
    if len(height) != len(weight):
        raise ValueError("height and weight lists must have the same length")
    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("All elements in height must be int or float")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("All elements in weight must be int or float")

    height_arr = np.array(height)
    weight_arr = np.array(weight)
    bmis = weight_arr / (height_arr ** 2)
    return bmis.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Filters BMI values based on a specified limit.

    Args:
        bmi (list[int | float]): A list of BMI values (integers or floats).
        limit (int): The BMI threshold to compare against.

    Returns:
        list[bool]: A list of boolean values where each element is True if the
        corresponding BMI value is greater than the limit, otherwise False.

    Raises:
        TypeError: If 'bmi' is not a list, if 'limit' is not an integer, or if
        any element in 'bmi' is not an int or float.
    """
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")
    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("All elements in bmi must be int or float")
    return [b > limit for b in bmi]
