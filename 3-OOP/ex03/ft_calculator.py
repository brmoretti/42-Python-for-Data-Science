class calculator:
    '''
    A calculator class that performs in-place arithmetic operations on a list
    of numbers.

    This class supports addition, subtraction, multiplication, and division
    with a scalar value, modifying the internal list and printing the result
    after each operation.

    Attributes:
        _list (list): The list of numbers to be manipulated.

    Methods:
        __init__(list):
            Initializes the calculator with the provided list.

        __add__(object):
            Adds a scalar value to each element of the internal list and
            prints the updated list.

        __mul__(object):
            Multiplies each element of the internal list by a scalar value and
            prints the updated list.

        __sub__(object):
            Subtracts a scalar value from each element of the internal list
            and prints the updated list.

        __truediv__(object):
            Divides each element of the internal list by a scalar value and
            prints the updated list.
            If division by zero is attempted, prints an error message instead.
    '''
    def __init__(self, list):
        """
        Initializes the object with the provided list.

        Args:
            list (list): The list to be stored in the object.
        """
        self._list = list

    def __add__(self, object) -> None:
        """
        Adds a given object to each element of the internal list and prints
        the updated list.

        Args:
            object: The value to add to each element of the internal list.

        Returns:
            None
        """
        for idx in range(len(self._list)):
            self._list[idx] = self._list[idx] + object
        print(self._list)

    def __mul__(self, object) -> None:
        """
        Multiplies each element of the internal list by the given object
        (scalar) in-place.

        Args:
            object (int or float): The value to multiply each element of the
            list by.

        Returns:
            None

        Side Effects:
            Modifies the internal list by multiplying each element by the
            given object.
            Prints the updated list to the standard output.
        """
        for idx in range(len(self._list)):
            self._list[idx] = self._list[idx] * object
        print(self._list)

    def __sub__(self, object) -> None:
        """
        Subtracts a given value from each element of the internal list.

        Args:
            object (numeric): The value to subtract from each element of the
            list.

        Returns:
            None

        Side Effects:
            Modifies the internal list in place and prints the updated list.
        """
        for idx in range(len(self._list)):
            self._list[idx] = self._list[idx] - object
        print(self._list)

    def __truediv__(self, object) -> None:
        """
        Implements the division (/) operator for the object.

        Divides each element of the internal list (`self._list`) by the given
        `object`.
        If `object` is zero, prints an assertion error message and does not
        perform the division.

        Args:
            object (numeric): The value by which to divide each element of the
            list.

        Returns:
            None

        Side Effects:
            Modifies `self._list` in place and prints the updated list or an
            error message.
        """
        try:
            assert object != 0, "division by zero"
        except AssertionError as e:
            print(f"AssertionError: {e}")
            return
        for idx in range(len(self._list)):
            self._list[idx] = self._list[idx] / object
        print(self._list)
