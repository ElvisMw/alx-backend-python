#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        mock_org.return_value = {"repos_url":
                                 "https://api.github.com/orgs/test-org/repos"}

        client = GithubOrgClient("test-org")
        result = client._public_repos_url

        self.assertEqual(result, "https://api.github.com/orgs/test-org/repos")


if __name__ == '__main__':
    unittest.main()
