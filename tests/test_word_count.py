#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import solutions
import time


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
        """
        results = solutions.word_count('Test test this is a string test')
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
        results = solutions.word_count(u'Test test this is a string test')
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
        result = solutions.word_count('tests/test_file')
        self.assertGreater(len(result), 0)

    @stopwatch
    def test_empty_input(self):
        result = solutions.word_count('')
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
