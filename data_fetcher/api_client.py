import requests
from typing import List, Dict, Any

def fetch_data_from_source(api_url: str) -> List[Dict[str, Any]]:
    """
    Fetches data from the specified API endpoint.

    Args:
        api_url: The URL of the API endpoint to fetch data from.

    Returns:
        A list of dictionaries representing the JSON response from the API.
        Returns an empty list if the request fails or the response is not valid JSON.

    Raises:
        requests.exceptions.RequestException: If there's an issue with the network request.
    """
    try:
        response = requests.get(api_url, timeout=10) # 10-second timeout
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
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
