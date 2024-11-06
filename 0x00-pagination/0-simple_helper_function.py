#!/usr/bin/env python3
"""index_range function module"""


def index_range(page, page_size):
    """returns a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return in a list
    for the pagination parameters.
    """
    start_index = page_size * (page - 1)
    end_index = page_size * page
    return (start_index, end_index)
