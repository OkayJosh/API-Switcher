from typing import List
from abc import ABC, abstractmethod

class UserPort(ABC):
    """
    An abstract base class (ABC) that defines the interface for user APIs.

    Any user API implementation (such as internal or external user APIs) must inherit from this class
    and implement the `fetch` method to retrieve user objects.

    This ensures a consistent interface for fetching user data, regardless of the specific source.
    """

    @abstractmethod
    def fetch(self, count: int) -> List[dict]:
        """
        Fetches a specified number of user objects.

        This method must be implemented by any class inheriting from `UserPort`. It defines
        the contract for fetching user data, where `count` specifies the number of users to retrieve.

        Args:
            count (int): The number of users to fetch.

        Returns:
            List[dict]: A list of dictionaries, where each dictionary represents a user object.
        
        Example format:
            [
                {
                    'name': 'John Doe',
                    'age': 30,
                    'address': '123 Main St, Springfield'
                },
                ...
            ]
        """
        pass
