#!/usr/bin/env python3
"""
This module contains unit tests for the memoize decorator.
"""
import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """
    Test class for the memoize decorator.
    """

    def test_memoize(self):
        """
        Test the memoize decorator by checking that the decorated method is only
        called once and the result is cached.
        """

        class TestClass:
            """
            Test class for the memoize decorator.
            """

            def a_method(self):
                """
                Method to be decorated.
                """
                return 42

            @memoize
            def a_property(self):
                """
                Method decorated with the memoize decorator.
                """
                return self.a_method()

        # Patch the method to return a known value and assert that the decorated
        # method is only called once.
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            instance = TestClass()
            self.assertEqual(instance.a_property, 42)
            self.assertEqual(instance.a_property, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
