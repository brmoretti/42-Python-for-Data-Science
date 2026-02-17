from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    King class that inherits from both Baratheon and Lannister.

    Represents a king character with attributes for eyes and hair color,
    including methods to get and set these attributes with validation.

    Attributes:
        first_name (str): The first name of the king.
        is_alive (bool): Whether the king is alive. Defaults to True.
        eyes (str): The color of the king's eyes. Defaults to "brown".
        hairs (str): The shade of the king's hair. Defaults to "dark".

    Methods:
        get_eyes() -> str: Returns the current eye color.
        set_eyes(color: str) -> None: Sets the eye color with validation.
            Valid options: "black", "blue", "brown", "gray", "green"
        get_hairs() -> str: Returns the current hair shade.
        set_hairs(shade: str) -> None: Sets the hair shade with validation.
            Valid options: "dark", "light"
    """
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initialize a DiamondTrap instance.

        Args:
            first_name (str): The name of the DiamondTrap.
            is_alive (bool, optional): Whether the DiamondTrap is alive.
                            Defaults to True.

        Returns:
            None
        """
        super().__init__(first_name, is_alive)
        self.eyes = "brown"
        self.hairs = "dark"

    def get_eyes(self) -> str:
        """
        Get the eyes attribute of the object.

        Returns:
            str: The eyes attribute value.
        """
        return self.eyes

    def set_eyes(self, color: str):
        """
        Set the eye color of the character.

        Args:
            color (str): The eye color to set. Must be a string and one of the
                        following: "black", "blue", "brown", "gray", or
                        "green".

        Raises:
            AssertionError: If color is not a string or not a valid eye color
                        option. Error message is printed to console.

        Returns:
            None
        """
        try:
            assert isinstance(color, str), "color is not atr type"
            color = color.lower()
            assert color in [
                "black", "blue", "brown", "gray", "green"
            ], "color is not a valid option"
            self.eyes = color
        except AssertionError as e:
            print(f"AssertionError: {e}")

    def get_hairs(self) -> str:
        """
        Retrieve the hair shade.

        Returns:
            str: hair shade.
        """
        return self.hairs

    def set_hairs(self, shade: str):
        """
        Set the hair shade for the character.

        Args:
            shade (str): The hair shade to set. Must be a string with a value
                        of either "dark" or "light" (case-insensitive).

        Raises:
            AssertionError: If shade is not a string or if shade is not a valid
                            option ("dark" or "light").

        Note:
            The method catches AssertionError exceptions and prints them
            instead of raising them.
        """
        try:
            assert isinstance(shade, str), "color is not atr type"
            shade = shade.lower()
            assert shade in [
                "dark", "light"
            ], "shade is not a valid option"
            self.hairs = shade
        except AssertionError as e:
            print(f"AssertionError: {e}")
