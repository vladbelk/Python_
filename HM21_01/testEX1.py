
# Generated by CodiumAI

from HM21_01.ex1 import get_sum_from_list

import unittest

class TestGetSumFromList(unittest.TestCase):

    #  The function returns 0 when an empty list is passed.
    def test_empty_list(self):
        result = get_sum_from_list([])
        self.assertEqual(result, 0)

    #  The function returns the sum of all elements in the list when a list of positive integers is passed.
    def test_positive_integers(self):
        result = get_sum_from_list([1, 2, 3, 4, 5])
        self.assertEqual(result, 15)

    #  The function returns the sum of all elements in the list when a list of negative integers is passed.
    def test_negative_integers(self):
        result = get_sum_from_list([-1, -2, -3, -4, -5])
        self.assertEqual(result, -15)

    #  The function raises a TypeError when a non-list argument is passed.
    def test_non_list_argument(self):
        with self.assertRaises(TypeError):
            get_sum_from_list("not a list")

    #  The function raises a TypeError when a list containing non-numeric elements is passed.
    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            get_sum_from_list([1, 2, "3", 4, 5])

    #  The function returns the correct sum when a list containing only one element is passed.
    def test_single_element(self):
        result = get_sum_from_list([10])
        self.assertEqual(result, 10)
