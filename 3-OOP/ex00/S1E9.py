from abc import ABC, abstractmethod


class Character(ABC):
    '''
    Character is an abstract base class representing a character with a first
    name and a living status.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): Indicates whether the character is alive.

    Methods:
        __init__(first_name: str, is_alive: bool = True):
            Initializes a new Character instance with the given first name and
            living status.

        die():
            Sets the character's 'is_alive' attribute to False, marking the
            character as no longer alive.
    '''
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initializes a new instance of the class.

        Args:
            first_name (str): The first name of the individual.
            is_alive (bool, optional): Indicates if the individual is alive.
            Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Marks the object as no longer alive by setting the 'is_alive'
        attribute to False.
        """
        self.is_alive = False


class Stark(Character):
    '''
    Stark class, derived from Character, represents a member of House Stark.

    Attributes:
        first_name (str): The first name of the Stark character.
        is_alive (bool): Indicates if the character is alive. Defaults to True.

    Methods:
        __init__(first_name: str, is_alive: bool = True):
            Initializes a Stark object with a first name and alive status.
    '''
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initialize the object with a first name and alive status.

        Args:
            first_name (str): The first name of the object.
            is_alive (bool, optional): Indicates if the object is alive.
            Defaults to True.
        """
        super().__init__(first_name, is_alive)
