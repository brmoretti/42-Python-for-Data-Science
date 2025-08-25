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

        __str__():
            Returns a string representation of the object, excluding
            'first_name' and 'is_alive' attributes.
            The format is 'Vector: (value1, value2, ...)'.

        __repr__():
            Returns a string representation of the object for debugging,
            identical to the output of __str__().
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

    def __str__(self):
        """
        Return a string representation of the object, excluding 'first_name'
        and 'is_alive' attributes.

        The returned string is formatted as 'Vector: (value1, value2, ...)',
        where the values are the remaining attributes of the object in the
        order they appear in the instance's __dict__.
        """
        tmp = self.__dict__.copy()
        for key in ['first_name', 'is_alive']:
            tmp.pop(key, None)
        return f"Vector: {str(tuple(tmp.values()))}"

    def __repr__(self):
        """
        Return a string representation of the object for debugging and
        development.

        This implementation delegates to the __str__ method, so the output of
        __repr__ will be identical to that of __str__.
        """
        return self.__str__()


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
