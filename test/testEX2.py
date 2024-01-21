# Generated by CodiumAI

from homework.ex2_14_01 import find_and_replace_reserved_words

import unittest


class TestFindAndReplaceReservedWords(unittest.TestCase):

    #  The function replaces all occurrences of reserved words with their uppercase version.
    def test_replace_reserved_words_with_uppercase(self):
        text = "This is a reserved word"
        reserved_words = ["reserved"]
        expected_result = "This is a RESERVED word"

        result = find_and_replace_reserved_words(text, reserved_words)

        self.assertEqual(result, expected_result)

    #  The function returns the modified text.
    def test_return_modified_text(self):
        text = "This is a reserved word"
        reserved_words = ["reserved"]

        result = find_and_replace_reserved_words(text, reserved_words)

        self.assertEqual(result, text.upper())

    #  The function works correctly when the text contains no reserved words.
    def test_no_reserved_words_in_text(self):
        text = "This is a normal text"
        reserved_words = ["reserved"]

        result = find_and_replace_reserved_words(text, reserved_words)

        self.assertEqual(result, text)

    #  The function works correctly when the text is empty.
    def test_empty_text(self):
        text = ""
        reserved_words = ["reserved"]

        result = find_and_replace_reserved_words(text, reserved_words)

        self.assertEqual(result, text)

    #  The function works correctly when the reserved words list is None.
    def test_none_reserved_words_list(self):
        text = "This is a reserved word"
        reserved_words = None

        result = find_and_replace_reserved_words(text, reserved_words)

        self.assertEqual(result, text)

    #  The function works correctly when the reserved words list contains empty strings.
    def test_empty_strings_in_reserved_words_list(self):
        text = "This is a reserved word"
        reserved_words = ["reserved", ""]

        result = find_and_replace_reserved_words(text, reserved_words)

        self.assertEqual(result, "This is a RESERVED word")