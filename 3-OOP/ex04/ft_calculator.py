class calculator:
    '''
    A calculator class for performing basic vector operations.

    This class provides static methods to compute the dot product,
    element-wise addition, and element-wise subtraction of two vectors
    represented as lists of floats. All results are printed to the console.

    Methods
    -------
    dotproduct(V1: list[float], V2: list[float]) -> None

    add_vec(V1: list[float], V2: list[float]) -> None

    sous_vec(V1: list[float], V2: list[float]) -> None
        Subtracts two vectors element-wise and prints the resulting vector.
    '''
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates and prints the dot product of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None

        Prints:
            The dot product of V1 and V2 in the format
            'Dot product is: <result>'.
        """
        print(f'Dot product is: {sum(x * y for x, y in zip(V1, V2))}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise and prints the resulting vector.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None

        Prints:
            The element-wise sum of V1 and V2 as a list of floats.
        """
        print(f'Add vector is: {[float(x + y) for x, y in zip(V1, V2)]}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts two vectors element-wise and prints the result.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.

        Returns:
            None

        Prints:
            The element-wise difference between V1 and V2 as a list of floats.
        """
        print(f'Sous vector is: {[float(x - y) for x, y in zip(V1, V2)]}')
