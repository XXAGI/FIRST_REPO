import unittest
from unittest.mock import patch, MagicMock
import requests # Import requests for its exceptions

from data_fetcher import api_client

class TestApiClient(unittest.TestCase):

    @patch('data_fetcher.api_client.requests.get')
    def test_fetch_data_from_source_success(self, mock_get):
        """Test successful data fetching."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"id": 1, "title": "Test Todo"}]
        mock_get.return_value = mock_response

        api_url = "http://fakeapi.com/data"
        data = api_client.fetch_data_from_source(api_url)

        mock_get.assert_called_once_with(api_url, timeout=10)
        self.assertEqual(data, [{"id": 1, "title": "Test Todo"}])

    @patch('data_fetcher.api_client.requests.get')
    def test_fetch_data_from_source_http_error(self, mock_get):
        """Test handling of HTTP errors."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
        mock_get.return_value = mock_response

        api_url = "http://fakeapi.com/nonexistent"
        with self.assertRaises(requests.exceptions.HTTPError):
            api_client.fetch_data_from_source(api_url)
        mock_get.assert_called_once_with(api_url, timeout=10)

    @patch('data_fetcher.api_client.requests.get')
    def test_fetch_data_from_source_timeout(self, mock_get):
        """Test handling of timeouts."""
        mock_get.side_effect = requests.exceptions.Timeout("Request timed out")

        api_url = "http://fakeapi.com/slowresponse"
        with self.assertRaises(requests.exceptions.Timeout):
            api_client.fetch_data_from_source(api_url)
        mock_get.assert_called_once_with(api_url, timeout=10)

    @patch('data_fetcher.api_client.requests.get')
    def test_fetch_data_from_source_request_exception(self, mock_get):
        """Test handling of general request exceptions."""
        mock_get.side_effect = requests.exceptions.RequestException("Some connection error")

        api_url = "http://fakeapi.com/connectionerror"
        with self.assertRaises(requests.exceptions.RequestException):
            api_client.fetch_data_from_source(api_url)
        mock_get.assert_called_once_with(api_url, timeout=10)

    @patch('data_fetcher.api_client.requests.get')
    def test_fetch_data_from_source_invalid_json(self, mock_get):
        """Test handling of responses with invalid JSON."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Failed to decode JSON") # requests.exceptions.JSONDecodeError inherits from ValueError
        mock_get.return_value = mock_response

        api_url = "http://fakeapi.com/invalidjson"
        data = api_client.fetch_data_from_source(api_url)

        mock_get.assert_called_once_with(api_url, timeout=10)
        self.assertEqual(data, []) # Expect empty list on JSON decode error as per implementation

if __name__ == '__main__':
    unittest.main()
