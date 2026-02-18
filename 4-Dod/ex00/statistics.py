from typing import Any


def _mean(numbers: list, length: int) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers (list): A list of numeric values.
        length (int): The number of elements in the list.

    Returns:
        float: The arithmetic mean of the numbers.

    Raises:
        ZeroDivisionError: If length is 0.
    """
    total = 0
    for n in numbers:
        total += n
    return total / length


def _sort_numbers(numbers: list, length: int) -> list:
    """
    Sort a list of numbers in ascending order using bubble sort algorithm.

    Args:
        numbers (list): A list of numeric values to be sorted.
        length (int): The number of elements to sort in the list.

    Returns:
        list: The sorted list in ascending order.
    """
    i = 0
    while i < length - 1:
        j = i + 1
        while j < length:
            if numbers[i] > numbers[j]:
                tmp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = tmp
            j += 1
        i += 1
    return numbers


def _median(sorted_numbers: list, length: int) -> float | int:
    """
    Calculate the median of a sorted list of numbers.

    For odd-length lists, returns the middle element.
    For even-length lists, returns the average of the two middle elements.

    Args:
        sorted_numbers (list): A sorted list of numeric values.
        length (int): The number of elements in the sorted_numbers list.

    Returns:
        float | int: The median value. Returns an int for odd-length lists,
                     or a float for even-length lists (average of two middle
                     values).
    """
    if length % 2 == 1:
        return sorted_numbers[length // 2]
    else:
        return (sorted_numbers[length // 2 - 1] +
                sorted_numbers[length // 2]) / 2


def _quartile(sorted_numbers: list, length: int) -> list:
    """
    Calculate the first and third quartiles of a sorted list of numbers.

    Args:
        sorted_numbers (list): A sorted list of numbers.
        length (int): The length of the sorted list.

    Returns:
        list: A list containing two floats [Q1, Q3], where Q1 is the first
            quartile and Q3 is the third quartile.

    Note:
        - For odd-length lists, quartiles are calculated by selecting elements
          at specific positions.
        - For even-length lists, quartiles are calculated as the average of
          adjacent elements at the quartile positions.
    """
    if length % 2 == 1:
        mid = length // 2
        q1 = sorted_numbers[mid // 2]
        q3 = sorted_numbers[mid + mid // 2]
    else:
        q1 = (sorted_numbers[length // 4 - 1] +
              sorted_numbers[length // 4]) / 2
        q3 = (sorted_numbers[3 * length // 4 - 1] +
              sorted_numbers[3 * length // 4]) / 2
    return [float(q1), float(q3)]


def _var(numbers: list, mean: float, length: int) -> float:
    """
    Calculate the variance of a list of numbers.

    Args:
        numbers: A list of numeric values.
        mean: The mean (average) of the numbers.
        length: The number of elements to consider in the list.

    Returns:
        float: The variance of the numbers, computed as the average of the
               squared differences from the mean.

    Raises:
        ZeroDivisionError: If length is 0.
    """
    i = 0
    acc = 0.0
    while i < length:
        acc += (numbers[i] - mean) ** 2
        i += 1
    return acc / length


def _std(numbers: list, mean: float, length: int) -> float:
    """
    Calculate the standard deviation of a list of numbers.

    The standard deviation is the square root of the variance,
    which measures how spread out the numbers are from the mean.

    Args:
        numbers: A list of numeric values.
        mean: The mean (average) of the numbers.
        length: The number of elements in the list.

    Returns:
        float: The standard deviation of the numbers.

    Raises:
        ZeroDivisionError: If length is 0.
    """
    return _var(numbers, mean, length) ** (1 / 2)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate and print various statistical measures for given numerical
    arguments.

    Parameters
    ----------
    *args : int or float
        Variable length argument list of numerical values to compute
        statistics on.
        Only int and float types are accepted.
    **kwargs : str
        Keyword arguments specifying which statistics to compute and print.
        Supported keys are:
        - "mean": Arithmetic mean of the values
        - "median": Middle value of sorted values
        - "quartile": Quartile values of the dataset
        - "std": Standard deviation of the values
        - "var": Variance of the values

    Returns
    -------
    None
        Prints the requested statistics to stdout.

    Notes
    -----
    - If no numerical arguments are provided and statistics are requested,
      "ERROR" is printed for each statistic.
    - Invalid statistic names in kwargs are silently ignored.
    - The function prints one statistic per line in the format:
    "statistic : value"

    Examples
    --------
    >>> ft_statistics(1, 2, 3, 4, 5, mean="mean", median="median")
    mean : 3.0
    median : 3
    """
    length = 0
    try:
        for n in args:
            if not isinstance(n, (int, float)):
                raise ValueError("Only numbers are allowed as arguments")
            length += 1

        numbers = list(args)
        mean = _mean(numbers, length)
        sorted = _sort_numbers(numbers[:], length)
        for key, value in kwargs.items():
            match value:
                case "mean":
                    print(f"mean : {mean}")
                case "median":
                    print(f"median : {_median(sorted, length)}")
                case "quartile":
                    print(f"quartile : {_quartile(sorted, length)}")
                case "std":
                    print(f"std : {_std(sorted, mean, length)}")
                case "var":
                    print(f"var : {_var(sorted, mean, length)}")
                case _:
                    pass
    except ValueError as e:
        print(f"ValueError: {e}")
    except ZeroDivisionError:
        for key, value in kwargs.items():
            if (length == 0 and value in ["mean", "median", "quartile", "std",
                                          "var"]):
                print("ERROR")
