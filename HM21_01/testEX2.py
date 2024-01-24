# Generated by CodiumAI

from HM21_01.ex2 import find_minimum

import unittest


class TestFindMinimum(unittest.TestCase):

    #  Returns the minimum value in a list of integers.
    def test_returns_minimum_value(self):
        list_of_integers = [5, 3, 8, 2, 9]
        result = find_minimum(list_of_integers)
        self.assertEqual(result, 2)

    #  Returns None if the list is empty.
    def test_returns_none_for_empty_list(self):
        list_of_integers = []
        result = find_minimum(list_of_integers)
        self.assertIsNone(result)

    #  Works correctly with a list of one integer.
    def test_works_with_one_integer(self):
        list_of_integers = [5]
        result = find_minimum(list_of_integers)
        self.assertEqual(result, 5)

    #  Returns None if the input is not a list.
    def test_returns_none_for_non_list_input(self):
        non_list_input = 5
        result = find_minimum(non_list_input)
        self.assertIsNone(result)

    #  Returns None if the input list contains non-integer values.
    def test_returns_none_for_list_with_non_integer_values(self):
        list_with_non_integer_values = [5, 'a', 8, 2, 9]
        result = find_minimum(list_with_non_integer_values)
        self.assertIsNone(result)

    #  Works correctly with a list containing the minimum integer value.
    def test_works_with_minimum_integer_value(self):
        list_of_integers = [5, 3, 8, 2, -9]
        result = find_minimum(list_of_integers)
        self.assertEqual(result, -9)