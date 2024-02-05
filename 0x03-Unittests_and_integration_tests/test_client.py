#!/usr/bin/env python3
""" Parameterize a unit test """
import unittest
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized


def _get_json(url: str) -> Dict:
    """Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()


class TestGithubOrgClient(unittest.TestCase):
    """ a unittest class for the  GithubOrgClient class """

    @parameterized.expand([
        ('google', {"login": "google"}),
        ('abc', {"message": "Not Found"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, respond, mock_get_json):
        """ test org """
        mock_get_json.return_value = Mock(return_value=respond)
        github_client = GithubOrgClient(org_name)
        self.assertEqual(github_client.org(), respond)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """ test public_repos_url method """
        with patch.object(GithubOrgClient,
                          'org', new_callable=PropertyMock) as mock_org:

            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"}

            github_client = GithubOrgClient('google')
            result = github_client._public_repos_url
            expected_url = "https://api.github.com/orgs/google/repos"
            self.assertEqual(result, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ test public_repos method """
        expected_res = 'https://api.github.com/orgs/google/repos'
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_org:
            mock_get_json.return_value = Mock(return_value=expected_res)
            github_client = GithubOrgClient('google')
            result = github_client.public_repos()
            self.assertEqual(result, expected_res)
            mock_get_json.assert_called_once()
