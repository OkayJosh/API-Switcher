import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

django.setup()

from domain.interface import InternalUserAPI, ExternalUserAPI, API

# init_db = SqliteConnection().schema_defination('users')
def create_user_api(api_type: str = 'internal') -> API:
    """
    Factory method to create the appropriate User API instance based on the type.

    Args:
        api_type (str): The type of API to use, either 'internal' (mock) or 'external' (real).

    Returns:
        API: An instance of the `API` class, initialized with either an internal or external user API.

    Raises:
        ValueError: If the provided `api_type` is not recognized.
    """
    if api_type == 'internal':
        return API(api=InternalUserAPI())
    elif api_type == 'external':
        return API(api=ExternalUserAPI())
    else:
        raise ValueError(f"Unknown API type: {api_type}. Please choose 'internal' or 'external'.")


if __name__ == '__main__':
    # Unified API access, caller doesn't need to know the underlying API type
    internal_api = create_user_api(api_type='internal')
    # external_api = create_user_api(api_type='external')

    # Fetch users from both internal and external APIs
    result_internal = internal_api.users(count=10)
    # result_external = external_api.users(count=20)

    internal_api.save_data_in_db(result_internal)

    # Display the results
    print("### Internal API Result (Mock Data) ###")
    print(internal_api.fetch_from_db())

    print("\n######################################\n")

    print("### External API Result (Real Data) ###")
    # print(result_external)
