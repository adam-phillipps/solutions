#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os.path
# import codecs
from collections import Counter


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


# @stopwatch
def word_count(path):
    """
    Tally the duplicates.  `chunk`s can be io or basestring.

    return:
        <class 'collections.Counter'>
    """
    if (os.path.isfile(path)):
        with open(path) as source_file:
            for line in source_file:
                counter = Counter(line.split())
                print counter
    else:
        counter = Counter(str(path).split())
    return counter
