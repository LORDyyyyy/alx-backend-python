#!/usr/bin/env python3
""" Parameterize a unit test """
import unittest
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ a unittest class for the  GithubOrgClient class """

    @parameterized.expand([('google', {"login": "google"}), ('abc', {"message": "Not Found"})])
    @patch('client.get_json')
    def test_org(self, org_name, respond, mock_get_json):
        """ test org """
        mock_get_json.return_value = respond
        github_client = GithubOrgClient(org_name)
        self.assertEqual(github_client.org(), mock_get_json.return_value)
        mock_get_json.assert_called_once()
