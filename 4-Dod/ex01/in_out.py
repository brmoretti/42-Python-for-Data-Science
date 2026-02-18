def square(x: int | float) -> int | float:
    """
    Calculate the square of a number.

    Args:
        x: A numeric value (int or float).

    Returns:
        The square of the input value (int or float).
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Calculate x raised to the power of x.

    Args:
        x: A numeric value (int or float) to be raised to itself.

    Returns:
        int | float: The result of x raised to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Create a closure that applies a function iteratively to an initial value.

    This function returns an inner function that maintains state across calls.
    Each time the inner function is called, it applies the provided function
    an increasing number of times to the initial value.

    Args:
        x (int | float): The initial numeric value to be transformed.
        function: A callable that takes a numeric value and returns a
        transformed value.

    Returns:
        object: An inner function that when called, applies the function
                iteratively to the initial value x. On the first call,
                function is applied once.
                On the second call, function is applied twice, and so on.
    """
    count = 0

    def inner() -> float:
        nonlocal count
        nonlocal x
        count += 1
        result = x
        for _ in range(count):
            result = function(result)
        return result
    return inner
