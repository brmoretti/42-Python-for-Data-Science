from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initialize a Baratheon instance.

        Args:
            first_name (str): The first name of the Baratheon.
            is_alive (bool, optional): Whether the Baratheon is alive.
                            Defaults to True.

        Attributes:
            family_name (str): The family name, set to "Baratheon".
            eyes (str): Eye color, set to "brown".
            hairs (str): Hair color, set to "dark".
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        Return a string representation of the Baratheon character.

        This method delegates to the parent class's __str__ implementation
        to provide a consistent string representation across the class
        hierarchy.

        Returns:
            str: A string representation of the character, inherited from the
            parent class.
        """
        return super().__str__()

    def __repr__(self):
        """
        Return a string representation of the object.

        This method is called by the repr() built-in function and by string
        conversions (reverse quotes) to compute the official string
        representation of an object. The returned string should be a valid
        Python expression that could be used to recreate an object with the
        same value.

        Returns:
            str: A string representation of the object.
        """
        return super().__repr__()


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initialize a Lannister character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
                            Defaults to True.

        Returns:
            None
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        Return a string representation of the Baratheon character.

        This method delegates to the parent class's __str__ implementation
        to provide a consistent string representation across the class
        hierarchy.

        Returns:
            str: A string representation of the character, inherited from the
            parent class.
        """
        return super().__str__()

    def __repr__(self):
        """
        Return a string representation of the object.

        This method is called by the repr() built-in function and by string
        conversions (reverse quotes) to compute the official string
        representation of an object. The returned string should be a valid
        Python expression that could be used to recreate an object with the
        same value.

        Returns:
            str: A string representation of the object.
        """
        return super().__repr__()

    @classmethod
    def create_lannister(
        cls, first_name: str, is_alive: bool = True
    ) -> "Lannister":
        """
        Create a new Lannister instance.

        This class method is a factory method for creating Lannister objects
        with a simplified interface.

        Args:
            first_name (str): The first name of the Lannister.
            is_alive (bool, optional): Whether the Lannister is alive.
                                Defaults to True.

        Returns:
            Lannister: A new instance of the Lannister class.
        """
        return cls(first_name, is_alive)
