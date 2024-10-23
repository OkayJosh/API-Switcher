from typing import List
from domain.object import User
from domain.port import UserPort
import requests

class InternalUserAPI(UserPort):
    """
    A dummy internal implementation of the User API, simulating the fetching of user objects.

    This class generates mock user data with names, ages, and addresses. It is useful for
    testing and development when a real API is not available.

    Methods:
        fetch(count): Returns a list of dummy users with the given count.
    """

    def fetch(self, count: int) -> List[dict]:
        """
        Generates a list of dummy user objects.

        This method creates `count` number of user objects with mocked data, including 
        name, age, and address. The name is constructed as 'josh at {number}', and the
        age and address are based on the loop iteration index.

        Args:
            count (int): The number of dummy users to generate.

        Returns:
            List[dict]: A list of dictionaries representing the dummy user objects.
                Example format:
                [
                    {
                        'name': 'josh at 0',
                        'age': 1,
                        'address': 'my address @ 0'
                    },
                    {
                        'name': 'josh at 1',
                        'age': 2,
                        'address': 'my address @ 1'
                    },
                    ...
                ]

        Example:
            internal_api = InternalUserAPI()
            users = internal_api.fetch(5)
        """
        user_list = []
        for number in range(count):
            user_list.append(User(
                name=f'josh at {number}',
                age=number + 1,
                address=f'my address @ {number}').__dict__)

        return user_list


class ExternalUserAPI(UserPort):
    """
    A User API implementation that fetches real user data from the external API at
    https://dummyjson.com/users.

    This class sends a request to the API to retrieve user data, such as name, age, and address.

    Attributes:
        url_template (str): The base URL with a placeholder for the user count.
        session (requests.Session): A requests session to manage and send HTTP requests.
        prepared_request (requests.PreparedRequest): Stores the prepared request to be sent.
    
    Methods:
        prepare_request(count): Prepares an HTTP GET request with the specified count.
        fetch(count): Sends the prepared request and fetches user data from the API.
    """

    def __init__(self):
        """
        Initializes the ExternalUserAPI instance.

        Sets up the URL template, session, and prepares the necessary infrastructure to fetch
        users from the external API.

        Example:
            external_api = ExternalUserAPI()
        """
        self.url_template = 'https://dummyjson.com/users?limit={count}'
        self.session = requests.Session()
        self.prepared_request = None

    def prepare_request(self, count: int):
        """
        Prepares the HTTP request to retrieve user data by formatting the URL with the provided count.

        The `count` parameter defines the number of users to fetch, and the URL is formatted accordingly.
        A GET request is created and prepared using the `requests.Session` object.

        Args:
            count (int): The number of users to retrieve from the API.

        Raises:
            ValueError: If count is not a positive integer.

        Example:
            external_api.prepare_request(10)
        """
        if count <= 0:
            raise ValueError("The count must be a positive integer.")

        url = self.url_template.format(count=count)
        request = requests.Request('GET', url)
        self.prepared_request = self.session.prepare_request(request)

    def fetch(self, count: int) -> List[dict]:
        """
        Fetches the user data from the external API based on the provided count.

        The method prepares an HTTP GET request to fetch user data, sends the prepared request,
        and processes the JSON response. It extracts user details like name, age, and address,
        then formats them into a list of dictionaries.

        Args:
            count (int): The number of users to retrieve.

        Returns:
            List[dict]: A list of dictionaries, each containing user details.
                Example format:
                [
                    {
                        'name': 'Doe - John',
                        'age': 25,
                        'address': {
                            'city': 'Los Angeles',
                            'street': 'Main St.'
                        }
                    },
                    ...
                ]

        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.

        Example:
            external_api = ExternalUserAPI()
            users = external_api.fetch(5)
        """
        # Prepare the request with the dynamic count parameter
        self.prepare_request(count)

        # Send the prepared request using the session
        response = self.session.send(self.prepared_request)

        # Raise an error for bad HTTP responses
        response.raise_for_status()

        # Parse the response
        user_response = response.json().get('users', [])
        user_list = []
        for user in user_response:
            user_list.append({
                'name': f'{user.get("lastName")} - {user.get("firstName")}',
                'age': user.get("age"),
                'address': user.get("address")
            })

        return user_list


class API:
    """
    A generic API interface that can work with any user data source that implements the UserPort interface.

    This class abstracts the process of fetching users from either an internal or external source, depending
    on the API instance passed.

    Attributes:
        api (UserPort): The user data source (could be internal or external).

    Methods:
        users(count): Fetches the specified number of users from the API.
    """

    def __init__(self, api: UserPort):
        """
        Initializes the API with the specified user data source.

        Args:
            api (UserPort): An instance of a class that implements the UserPort interface.
        
        Example:
            internal_api = InternalUserAPI()
            api = API(internal_api)
        """
        self.api = api

    def users(self, count: int) -> List[dict]:
        """
        Fetches user data from the API instance.

        This method delegates the fetching process to the provided user data source (internal or external)
        and returns a list of user objects.

        Args:
            count (int): The number of users to retrieve.

        Returns:
            List[dict]: A list of user objects from the selected API source.

        Example:
            api = API(InternalUserAPI())
            users = api.users(5)
        """
        return self.api.fetch(count)
