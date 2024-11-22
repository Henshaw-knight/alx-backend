#!/usr/bin/env python3
""" FIFOCache class module """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A caching system with no limit, has the put and get method"""
    def __init__(self):
        """Instantiates the class"""
        super().__init__()

    def put(self, key, item):
        """Assigns to the dictionary `self.cache_data` the item `value`
        for the key `key`
        - if key or item is None, the method do not do anything
        - if the number of items in self.cache_data is higher than
          BaseCaching.MAX_ITEMS, the first item put in cache is discarded
          (FIFO algorithm)
        - DISCARD: with the key discarded followed by a new line is printed
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item_key = next(iter(self.cache_data))
            self.cache_data.pop(first_item_key)
            print("DISCARD: {}".format(first_item_key))

    def get(self, key):
        """Returns the value in self.cache_data linked to key"""
        if key is None or self.cache_data.get(key) is None:
            # dictionary get method
            return None
        return self.cache_data[key]
