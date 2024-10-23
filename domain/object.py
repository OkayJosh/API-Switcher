from dataclasses import dataclass

@dataclass
class User:
    """
    A data class representing a User object.

    This class encapsulates the basic information about a user, including their name, age, and address.
    It is used to represent individual user data in a structured format.

    Attributes:
        name (str): The full name of the user.
        age (int): The age of the user.
        address (str): The address of the user, including relevant details such as street and city.
    """

    name: str
    age: int
    address: str
