import unittest
import solutions
import time


class CondenseMeetingTimesTest(unittest.TestCase):
    """
    Test the ```condense_meeting_times()``` method
    """

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
    def test_equal_start_times(self):
        """
        Assure that the method can deal with duplicate start times
        """
        times = [(1, 3), (1, 2)]
        expected = [(1, 3)]
        results = solutions.condense_meeting_times(times)
        self.assertEqual(expected, results)

    @stopwatch
    def test_equal_end_times(self):
        """
        Assure that the method can deal with duplicate end times
        """
        times = [(1, 3), (2, 3)]
        expected = [(1, 3)]
        results = solutions.condense_meeting_times(times)
        self.assertEqual(expected, results)

    @stopwatch
    def test_random_ordered_input(self):
        """
        Assure that the method can deal with unorderd input
        """
        times = [
            (2, 4), (1, 7), (5, 9), (4, 8), (11, 14), (12, 13),
            (15, 17), (16, 20), (20, 21), (20, 22), (22, 28)
        ]
        result = solutions.condense_meeting_times(times)
        self.assertIsNotNone(result)

    @stopwatch
    def test_return_start_times_are_ordered(self):
        """
        Assure the method can return ordered results from unordered input.
        It checks that each time block is earlier than the one that
        follows it.
        """
        times = [
            (2, 4), (1, 7), (5, 9), (4, 8), (11, 14), (12, 13),
            (15, 17), (16, 20), (20, 21), (20, 22), (22, 28)
        ]
        result = solutions.condense_meeting_times(times)
        for i, time_block in enumerate(result):
            if (i >= len(result) - 1):
                break
            self.assertLess(time_block, result[i + 1])
