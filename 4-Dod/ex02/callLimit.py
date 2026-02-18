from typing import Any


def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        nonlocal count

        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            count += 1
            try:
                assert count <= limit, f"{function} call too many times"
                return function(*args, **kwds)
            except AssertionError as e:
                print(f"Error: {e}")
        return limit_function
    return callLimiter
