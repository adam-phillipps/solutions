#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import codecs
from collections import Counter
import string
from string import punctuation


def word_count(source):
    """
    Tally occurancs of a word, without punctuation.

    parameters:
        string that can be a path to a file
    return:
        <class 'collections.Counter'>
    """
    punc = string.punctuation
    counter = Counter()
    if (os.path.isfile(source)):
        with codecs.open(source) as source_file:
            for line in source_file:
                no_punc_line = [word.strip(punc) for word in line.split()]
                counter.update(no_punc_line)
    else:
        no_punc_line = [word.strip(punc) for word in source.split()]
        counter.update(Counter(no_punc_line))
    return {k: v for k, v in counter.iteritems()}


def condense_meeting_times(times):
    """
    This takes a list of times and returns an organized list with all
    overlapping times ommited.

    parameters:
        list of (start_time, end_time) tuples
    return:
        list of tuples
    """
    # Let python sort, most effeciently.  This yields an easy
    # way to find overlapping time blocks
    times.sort()
    condensed_times = []
    start_time, end_time = times[0]
    for time_block in times:
        if (end_time >= time_block[0]):
            end_time = max(end_time, time_block[1])
        else:
            condensed_times.append((start_time, end_time))
            start_time, end_time = time_block
    condensed_times.append((start_time, end_time))
    return condensed_times
