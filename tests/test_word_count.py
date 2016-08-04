#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import solutions
import time
from os import path


class WordCountTests(unittest.TestCase):

    def stopwatch(event):
        """
        Time a function from start to finish.
        """
        def start_stop(param):
            start = time.time()
            event(param)
            finish = time.time()
            print '\nTime: ' + str(finish - start)
            return event
        return start_stop

    @stopwatch
    def test_correct_return_type(self):
        """
        Assure the correct return type
        """
        results = solutions.word_count('ping')
        self.assertIsInstance(results, dict)

    @stopwatch
    def test_str_input(self):
        """
        Assure the function can take str inputs
        """
        results = solutions.word_count('Test test this is a string test.')
        expected = {
            'Test': 1,
            'test': 2,
            'this': 1,
            'is': 1,
            'a': 1,
            'string': 1
        }
        self.assertEqual(expected, results)

    @stopwatch
    def test_unicode_input(self):
        """
        Assure the function can take unicode inputs
        """
        results = solutions.word_count(u'Test test this is a string test.')
        expected = {
            'Test': 1,
            'test': 2,
            'this': 1,
            'is': 1,
            'a': 1,
            'string': 1
        }
        self.assertEqual(expected, results)

    @stopwatch
    def test_file_input(self):
        """
        Assure the code can take file path inputs
        """
        file = path.join(path.abspath(path.dirname(__file__)), 'test_file')
        result = solutions.word_count(file)
        self.assertGreater(len(result), 1)

    @stopwatch
    def test_empty_input(self):
        """
        Assure the function can deal with an empty string input
        """
        result = solutions.word_count('')
        self.assertIsNotNone(result)
