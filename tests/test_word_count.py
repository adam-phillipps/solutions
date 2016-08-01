#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import solutions
from collections import Counter


class WordCountTests(unittest.TestCase):

    def test_correct_return_type(self):
        results = solutions.word_count('README.md')
        self.assertIsInstance(results, Counter)

    def test_str_input(self):
        results = solutions.word_count('Test test this is a string test. yes')
        expected = {
            'Test': 1,
            'test': 2,
            'this': 1,
            'is': 1,
            'a': 1,
            'string': 1
        }
        self.assertEqual(expected, results)

    def test_unicode_input(self):
        self.assertFalse(True)

    def test_unix_timestamps(self):
        self.assertFalse(True)

    def test_iso_8601(self):
        self.assertFalse(True)


if __name__ == '__main__':
    unittest.main()
