from unittest.mock import patch, Mock
import unittest

from parameterized import parameterized

from utils import get_json


class TestGetJson(unittest.TestCase):
    """
    Tests for the get_json function.
    """

    @parameterized.expand([
        """ Test case 1: Successful request """
        ("http://example.com", {"payload": True}),
        """ Test case 2: Unsuccessful request """
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the get_json function.

        Args:
            test_url (str): The URL to send a GET request to.
            test_payload (dict): The expected response payload.
            mock_get (MagicMock): A mock object for the requests.get function

        Returns:
            None
        """
        """ Set up the mock to return the expected response """
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = test_payload

        """ Call the function and check the result """
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
