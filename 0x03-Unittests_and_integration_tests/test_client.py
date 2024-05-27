#!/usr/bin/env python3
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
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('client.requests.get')

        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def setUp(self):
        self.mock_get.reset_mock()

    def test_public_repos(self):
        self.mock_get.return_value.json.side_effect =
        [self.org_payload, self.repos_payload]

        client = GithubOrgClient("test-org")
        result = client.public_repos

        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        self.mock_get.return_value.json.side_effect =
        [self.org_payload, self.apache2_repos]

        client = GithubOrgClient("test-org")
        result = client.public_repos

        self.assertEqual(result, ["repo1", "repo2"])


if __name__ == '__main__':
    unittest.main()
