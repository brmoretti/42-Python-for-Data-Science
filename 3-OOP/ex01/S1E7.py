from S1E9 import Character


class Baratheon(Character):
    """
    Baratheon class representing a character from the Baratheon family.

    Inherits from Character class and adds specific attributes for Baratheon
    family members.

    Attributes:
        first_name (str): The character's first name.
        is_alive (bool): Whether the character is alive. Defaults to True.
        family_name (str): The family name, set to "Baratheon".
        eyes (str): Eye color, set to "brown".
        hairs (str): Hair color, set to "dark".
    """
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


class Lannister(Character):
    """
    Lannister character class representing members of House Lannister.

    This class inherits from Character and defines specific attributes
    for Lannister family members, including their distinctive physical traits.

    Attributes:
        first_name (str): The character's first name.
        is_alive (bool): Whether the character is alive. Defaults to True.
        family_name (str): The family name, set to "Lannister".
        eyes (str): Eye color, set to "blue".
        hairs (str): Hair color, set to "light".

    Methods:
        __init__(first_name, is_alive): Initializes a Lannister instance with
            the given first name and alive status, setting family-specific
            attributes.
        create_lannister(first_name, is_alive): Class method that creates and
            returns a new Lannister instance.
    """
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
