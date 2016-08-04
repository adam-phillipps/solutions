import unittest
import solutions
import time
import datetime


class CondenseMeetingTimesTest(unittest.TestCase):
    """
    Test the ```condense_meeting_times()``` function
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
        Assure that the function can deal with duplicate start times
        """
        times = [(1, 3), (1, 2)]
        expected = [(1, 3)]
        results = solutions.condense_meeting_times(times)
        self.assertEqual(expected, results)

    @stopwatch
    def test_equal_end_times(self):
        """
        Assure that the function can deal with duplicate end times
        """
        times = [(1, 3), (2, 3)]
        expected = [(1, 3)]
        results = solutions.condense_meeting_times(times)
        self.assertEqual(expected, results)

    @stopwatch
    def test_random_ordered_input(self):
        """
        Assure that the function can deal with unorderd input
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
        Assure the function can return ordered results from unordered input.
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

    @stopwatch
    def test_iso_dates(self):
        """
        Clumsily assure that the function's functionality is functional,
        while functioning with iso dates.
        """
        delta_one = datetime.timedelta(hours=1)
        delta_two = datetime.timedelta(hours=2)
        delta_three = datetime.timedelta(hours=3)
        start_time_a = datetime.datetime.now().isoformat()
        end_time_a = (datetime.datetime.now() + delta_two).isoformat()
        start_time_b = (datetime.datetime.now() + delta_one).isoformat()
        end_time_b = (datetime.datetime.now() + delta_three).isoformat()
        times = [
            (start_time_a, end_time_a),
            (start_time_b, end_time_b)
        ]
        result = solutions.condense_meeting_times(times)
        self.assertListEqual(result, [(start_time_a, end_time_b)])
