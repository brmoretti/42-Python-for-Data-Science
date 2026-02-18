import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random student ID consisting of 15 lowercase ASCII characters.

    Returns:
        str: A random string of 15 lowercase letters (a-z).
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A dataclass representing a student with automatic login generation.

    Attributes:
        name (str): The student's first name.
        surname (str): The student's last name.
        active (bool): Whether the student is currently active.
                        Defaults to True.
        login (str): Auto-generated login combining first letter of name and
                    surname.
        id (str): Unique student identifier, auto-generated using
                    generate_id().
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Initialize the login attribute after dataclass initialization.

        Constructs the login by concatenating the first character of the name
        with the entire surname.

        Returns:
            None
        """
        self.login = self.name[0] + self.surname
