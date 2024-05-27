#!/usr/bin/env python3

"""Test class for testing GithubOrgClient class."""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        # Test case for a valid organization name
        ("google",),
        # Test case for an invalid organization name
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test the org property of the GithubOrgClient class.

        This test case checks that the org property of the GithubOrgClient
        class
        returns the correct organization payload from the Github API.

        Args:
            org_name (str): The name of the organization to test.
            mock_get_json (MagicMock): A mock object for the get_json method.
        """
        # Define the mock payload for the organization
        mock_payload = {"login": org_name}
        # Set the return value of the mock_get_json method to the mock payload
        mock_get_json.return_value = mock_payload

        # Create an instance of the GithubOrgClient class
        client = GithubOrgClient(org_name)
        # Get the org property of the client instance
        result = client.org

        # Assert that the get_json method was called with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        # Assert that the result is equal to the mock payload
        self.assertEqual(result, mock_payload)


if __name__ == '__main__':
    unittest.main()
