#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import codecs
from collections import Counter


def word_count(source):
    """
    Tally occurancs of a word.  `chunk`s can be io or basestring.

    return:
        <class 'collections.Counter'>
    """
    counter = Counter()
    if (os.path.isfile(source)):
        with codecs.open(source) as source_file:
            for line in source_file:
                counter.update(line.split())
    else:
        counter.update(Counter(str(source).split()))
    ex = {k: v for k, v in counter.iteritems()}
    print ex
    return ex


def condense_meeting_times(times):
    """
    Return information about the continuous blocks of time meetings are
    scheduled for.

    return:
        list of tuples
    """
    running_block = ()
    return [(0,0)]
