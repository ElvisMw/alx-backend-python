#!/usr/bin/env python3

"""
Integration tests for GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class

from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from client import GithubOrgClient


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (org_payload, repos_payload, expected_repos, apache2_repos),
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Test case for GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment.
        """
        cls.get_patcher = patch('client.requests.get')

        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test environment.
        """
        cls.get_patcher.stop()

    def setUp(self):
        """
        Reset the mock object before each test.
        """
        self.mock_get.reset_mock()

    def test_public_repos(self):
        """
        Test the public_repos property.
        """
        # Patch the return value of the requests.get method
        self.mock_get.return_value.json.side_effect = [
            self.org_payload, self.repos_payload
        ]

        client = GithubOrgClient("test-org")
        result = client.public_repos

        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test the public_repos property with Apache 2.0 license.
        """
        # Patch the return value of the requests.get method
        self.mock_get.return_value.json.side_effect = [
            self.org_payload, self.apache2_repos
        ]

        client = GithubOrgClient("test-org")
        result = client.public_repos

        self.assertEqual(result, ["repo1", "repo2"])


if __name__ == '__main__':
    unittest.main()
