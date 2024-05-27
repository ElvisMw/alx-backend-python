#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        # Set up the mock to return the test payload
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = test_payload

        # Call the function being tested
        result = get_json(test_url)

        # Check that the mock was called correctly
        mock_get.assert_called_once_with(test_url)
        # Check that the function returned the expected result
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
