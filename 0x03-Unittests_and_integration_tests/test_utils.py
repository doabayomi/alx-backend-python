#!/usr/bin/env python3
"""Tests for utils.py methods
"""
import unittest
from unittest.mock import patch, Mock
import utils
from utils import memoize
from typing import Mapping, Sequence, Any, Dict
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Tests the utils.access_nested_map() function
    """
    @parameterized.expand([
        ("one_element", {"a": 1}, ("a",), 1),
        ("one_levels", {"a": {"b": 2}}, ("a",), {'b': 2}),
        ("two_levels", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name: str, nested_map: Mapping,
                               path: Sequence, expected: Any):
        """Tests the access_nested_map() function normally
        """
        self.assertEqual(utils.access_nested_map(nested_map,
                                                 path), expected)

    @parameterized.expand([
        ("empty_nested_map", {}, ("a",)),
        ("invalid_path", {"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, name: str, nested_map: Mapping,
                                         path: Sequence):
        """Tests for exceptions in the access_nested_map() functions
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test object for the utils.get_json() function
    """
    @parameterized.expand([
        ("with_payload", "http://example.com", {"payload": True}),
        ("without_payload", "http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, name: str, test_url: str,
                      test_payload: Dict, mock_get: Mock):
        """Tests get_json() with mock calls.
        """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(utils.get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=33) as mock_get:
            instance = TestClass()
            self.assertEqual(instance.a_property, 33)
            mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
