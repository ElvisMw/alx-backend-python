#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from parameterized import parameterized_class

# Importing fixtures
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

# Importing the class to be tested
from client import GithubOrgClient


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"), [
        (org_payload, repos_payload, expected_repos, apache2_repos),
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Tests for the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the class fixture before running the tests.
        """
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the class fixture after running the tests.
        """
        cls.get_patcher.stop()

    def setUp(self):
        """
        Set up the test fixture before each test method.
        """
        self.mock_get.reset_mock()

    def test_public_repos(self):
        """
        Test the public_repos property of the GithubOrgClient class.
        """
        self.mock_get.side_effect = [self.org_payload, self.repos_payload]

        client = GithubOrgClient("test-org")
        result = client.public_repos

        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test the public_repos property of the GithubOrgClient class
        with a filter
        for Apache 2.0 licenses.
        """
        self.mock_get.side_effect = [self.org_payload, self.apache2_repos]

        client = GithubOrgClient("test-org")
        result = client.public_repos

        self.assertEqual(result, ["repo1", "repo2"])


if __name__ == '__main__':
    unittest.main()
