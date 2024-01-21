# Generated by CodiumAI
from io import StringIO
from unittest.mock import patch

from homework.ex9_14_01 import print_line

import unittest


class TestPrintLine(unittest.TestCase):

    #  prints a horizontal line of length n with a given symbol
    def test_print_horizontal_line(self):
        length = 5
        direction = "горизонтальна"
        symbol = "*"
        expected_output = "*****"

        with patch('sys.stdout', new = StringIO()) as fake_out:
            print_line(length, direction, symbol)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    #  prints a vertical line of length n with a given symbol
    def test_print_vertical_line(self):
        length = 5
        direction = "вертикальна"
        symbol = "*"
        expected_output = "*\n*\n*\n*\n*"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_line(length, direction, symbol)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    #  prints an empty line when length is 0
    def test_print_empty_line(self):
        length = 0
        direction = "горизонтальна"
        symbol = "*"
        expected_output = ""

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_line(length, direction, symbol)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    #  prints nothing when length is negative
    def test_print_negative_length(self):
        length = -5
        direction = "горизонтальна"
        symbol = "*"
        expected_output = ""

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_line(length, direction, symbol)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    #  prints nothing when length is not an integer
    def test_print_non_integer_length(self):
        length = "5"
        direction = "горизонтальна"
        symbol = "*"
        expected_output = ""

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_line(length, direction, symbol)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    #  prints nothing when direction is None
    def test_print_none_direction(self):
        length = 5
        direction = None
        symbol = "*"
        expected_output = ""

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_line(length, direction, symbol)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)