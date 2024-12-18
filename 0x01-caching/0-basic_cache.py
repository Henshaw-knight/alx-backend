#!/usr/bin/env python3
""" BasicCache class module """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A caching system with no limit, has the put and get method"""
    def put(self, key, item):
        """Assigns to the dictionary `self.cache_data` the item `value`
        for the key `key`"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to key"""
        if key is None or self.cache_data.get(key) is None:
            # dictionary get method
            return None
        return self.cache_data[key]
