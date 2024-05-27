#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @patch('client.GithubOrgClient.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        mock_public_repos_url.return_value =
        "https://api.github.com/orgs/test-org/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        client = GithubOrgClient("test-org")
        result = client.public_repos

        mock_get_json.assert_called_once_with
        ("https://api.github.com/orgs/test-org/repos")
        self.assertEqual(result, ["repo1", "repo2"])


if __name__ == '__main__':
    unittest.main()
