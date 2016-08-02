import unittest
import solutions
import time


class CondenseMeetingTimesTest(unittest.TestCase):

    def stopwatch(event):
        """
        Time a function from start to finish.
        """
        def start_stop(param):
            start = time.time()
            event(param)
            finish = time.time()
            print 'Time: ' + str(finish - start)
            return event
        return start_stop

    @stopwatch
    def test_equal_start_times(self):
        times = [(1, 3), (1, 2)]
        expected = [(1, 3)]
        results = solutions.condense_meeting_times(times)
        self.assertEqual(expected, results)

    @stopwatch
    def test_equal_end_times(self):
        times = [(1, 3), (2, 3)]
        expected = [(1, 3)]
        results = solutions.condense_meeting_times(times)
        self.assertEqual(expected, results)

    @stopwatch
    @unittest.skip('Test not implemented yet')
    def test_random_ordered_input(self):
        self.fail('Not Implemented yet')
