# User API Project

This project provides an abstraction for fetching user data from different sources. It includes two types of APIs:
- **Internal User API**: A mock API that generates fake user data.
- **External User API**: An API that fetches real user data from an external service.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/OkayJosh/API-Switcher
   cd API-Switcher
   
2. **Create and activate a virtual environment:**

##### You can use venv (Python's built-in virtual environment module) to create a virtual environment.

   ```bash
    python -m venv .venv
   ```

For Windows:

```bash
  .venv\Scripts\activate
```

For macOS/Linux:
```bash
source .venv/bin/activate
```

3. **install the requirements packages for the project:**

```bash
    pip install -r requirements.txt
```

## How It Works

The project abstracts away the usage of different user APIs by providing a unified interface for both internal (mock) and external (real) data sources. It allows switching between the internal and external APIs seamlessly using a factory method.

### Key Classes

- **`User`**: A simple data class that represents a user with attributes like `name`, `age`, and `address`.
- **`UserPort`**: An abstract base class (interface) that defines the contract for user APIs, requiring them to implement the `fetch` method.
- **`InternalUserAPI`**: A mock API implementation that generates fake user data.
- **`ExternalUserAPI`**: An API that fetches real user data from an external service (`https://dummyjson.com/users`).
- **`API`**: A wrapper that interacts with either the internal or external API to fetch user data.

## Usage
```python
from domain.interface import create_user_api

# Create internal API instance
internal_api = create_user_api(api_type='internal')

# Fetch 5 users from the internal API
result = internal_api.users(count=5)
print(result)

```

### Running the Application

To run the application, simply execute the `main.py` file. The script will fetch user data from both the internal (mock) API and the external API and display the results.

```bash
python starter.py
```


