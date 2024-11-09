#!/usr/bin/env python3
"""index_range function module"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """returns a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return in a list
    for the pagination parameters.
    """
    start_index = page_size * (page - 1)
    end_index = page_size * page
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        verifies that arguments gotten are integers greater than 0 and
        returns a list of lists of appropriate datasets
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        try:
            result_list = []
            result = index_range(page, page_size)
            start_row = result[0] + 1
            end_row = result[1] + 1
            with open(self.DATA_FILE) as file:
                csv_reader = csv.reader(file)

                for i, row in enumerate(csv_reader):
                    if start_row <= i < end_row:
                        result_list.append(row)
                    elif i >= result[1]:
                        break
            return result_list
        except exception as e:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        Returns a dictionary with the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no prev. page
        total_pages: the total number of pages in the dataset as an integer
        """
        with open(self.DATA_FILE) as file:
            csv_reader = csv.reader(file)
            row_count = sum(1 for row in csv_reader) - 1
            # subtract to remove header count
        dataset = self.get_page(page, page_size)
        return {
                "page_size": len(dataset),
                "page": page,
                "data": dataset,
                "next_page": None if len(dataset) < 1 else page + 1,
                "prev_page": None if page <= 1 else page - 1,
                "total_pages": math.ceil(row_count / page_size)
                }
