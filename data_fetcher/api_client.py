import requests # 'requests' is a popular third-party library for making HTTP requests.
from typing import List, Dict, Any

def fetch_data_from_source(api_url: str) -> List[Dict[str, Any]]:
    """
    Fetches data from the specified API endpoint.
    Uses the 'requests' library to perform a GET request.

    Args:
        api_url: The URL string of the API endpoint.

    Returns:
        A list of dictionaries containing the parsed JSON data.
    """
    try:
        # Perform an HTTP GET request to the specified URL.
        # timeout=10 ensures the request doesn't hang indefinitely if the server is slow.
        response = requests.get(api_url, timeout=10)

        # raise_for_status() checks if the response contains an error status code (e.g., 404, 500).
        # If it does, it raises an HTTPError exception.
        response.raise_for_status()

        # .json() parses the response body as JSON and returns it as a Python object (list/dict).
        return response.json()
    except requests.exceptions.Timeout:
        print(f"Request to {api_url} timed out.")
        raise
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.status_code} {response.text}")
        raise
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred during the request to {api_url}: {req_err}")
        raise
    except ValueError as json_err: # Handle cases where response is not JSON
        print(f"Failed to decode JSON from response: {json_err}")
        return []
