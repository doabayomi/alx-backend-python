#!/usr/bin/env python3
"""Tests client.py methods and properties
"""
import unittest
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class
    """
    @parameterized.expand([
        ("google_test", "google"),
        ("abc_test", "abc")
    ])
    @patch('client.get_json')
    def test_org(self, name: str, org_name: str, mock_get: Mock):
        """Tests the org() property
        """
        mock_get.return_value = {'name': org_name}
        instance = GithubOrgClient(org_name)
        self.assertEqual(instance.org, {'name': org_name})
        mock_get.assert_called_once_with(instance.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """Test the _public_repos_url property
        """
        instance = GithubOrgClient('test_org')
        test_payload = {
            'name': 'test_org',
            'repos_url': 'www.github.com/test_org/'
        }
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock,
                          return_value=test_payload):
            self.assertEqual(instance._public_repos_url,
                             test_payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get: Mock):
        """Tests the public_repos property
        """
        test_payload = [
                {'name': 'First Project'},
                {'name': 'Second Project'},
                {'name': 'Third Project', 'license': {'key': 'test_key'}},
                {'name': 'Penultimate Project',
                 'license': {'key': 'test_key'}},
                {'name': 'Capstone Project'}
        ]
        mock_get.return_value = test_payload
        expected_result = [repo["name"] for repo in test_payload]

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_repo:
            mock_repo.return_value = 'mocked_url'

            instance = GithubOrgClient('test_org')
            actual_result = instance.public_repos()
            self.assertEqual(actual_result, expected_result)
            mock_get.assert_called_once()
            mock_repo.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, expected: bool):
        """Tests the has_licence method
        """
        instance = GithubOrgClient('test_org')
        self.assertEqual(instance.has_license(repo, license_key),
                         expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Features integration """
    @classmethod
    def setUpClass(cls):
        """method called before tests"""
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """method called after tests"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
