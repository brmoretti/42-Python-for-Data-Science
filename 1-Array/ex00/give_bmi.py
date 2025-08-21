def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculates the Body Mass Index (BMI) for each pair of height and weight.

    Args:
        height (list[int | float]): A list of heights (in meters).
        weight (list[int | float]): A list of weights (in kilograms).

    Returns:
        list[int | float]: A list containing the BMI values for each
        corresponding height and weight pair.

    Raises:
        TypeError: If height or weight is not a list, or if any element in
        height or weight is not an int or float.
        ValueError: If height and weight lists have different lengths, or if
        any value in height or weight is non-positive.

    Notes:
        If an exception occurs, an error message is printed and the function
        returns an empty list.
    """
    bmis = []
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("height and weight must be lists")
        if len(height) != len(weight):
            raise ValueError(
                "height and weight lists must have the same length"
            )
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)):
                raise TypeError("all elements in height must be int or float")
            if not isinstance(w, (int, float)):
                raise TypeError("all elements in weight must be int or float")
            if h <= 0 or w <= 0:
                raise ValueError("height and weight must be non-negative")
            bmis.append(w / (h ** 2))
        return bmis
    except Exception as e:
        print(f"Error on give_bmi function: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Filters a list of BMI values by a specified limit.

    Args:
        bmi (list[int | float]): A list of BMI values (integers or floats).
        limit (int): The BMI threshold to compare against.

    Returns:
        list[bool]: A list of boolean values where each element is True if the
        corresponding BMI value is greater than the limit, otherwise False.

    Raises:
        TypeError: If bmi is not a list, limit is not an integer, or any
        element in bmi is not an int or float.
        ValueError: If any BMI value in the list is negative.

    Notes:
        If an exception occurs, an error message is printed and the function
        returns an empty list.

    Example:
        >>> apply_limit([22.5, 27.3, 18.9], 25)
        [False, True, False]
    """
    try:
        if not isinstance(bmi, list):
            raise TypeError("bmi must be a list")
        if not isinstance(limit, int):
            raise TypeError("limit must be an integer")
        if not all(isinstance(b, (int, float)) for b in bmi):
            raise TypeError("All elements in bmi must be int or float")
        if not all(b >= 0 for b in bmi):
            raise ValueError("All BMI values must be non-negative")
        return [b > limit for b in bmi]
    except Exception as e:
        print(f"Error on apply_limit function: {e}")
        return []
