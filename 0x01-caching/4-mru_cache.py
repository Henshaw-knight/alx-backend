#!/usr/bin/env python3
""" MRUCache class module """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A caching system with no limit, has the put and get method"""
    def __init__(self):
        """Instantiates the class"""
        super().__init__()
        self.stack = []  # Tracks the order of keys for LIFO

    def put(self, key, item):
        """Assigns to the dictionary `self.cache_data` the item `value`
        for the key `key`
        - if key or item is None, the method does not do anything
        - if the number of items in self.cache_data is higher than
          BaseCaching.MAX_ITEMS, the most recently used item is discarded
          (MRU algorithm)
        - DISCARD: with the key discarded followed by a new line is printed
        """
        if key and item:
            # if key exists, its value is updated and it is moved to the top
            # of the stack
            if key in self.cache_data:
                self.stack.remove(key)
            self.cache_data[key] = item
            self.stack.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # discard last item put in cache (LIFO algorithm)
                most_recently_used_key = self.stack.pop(-2)
                del self.cache_data[most_recently_used_key]
                print("DISCARD: {}".format(most_recently_used_key))

    def get(self, key):
        """Returns the value in self.cache_data linked to key"""
        if key is None or self.cache_data.get(key) is None:
            # dictionary get method
            return None
        self.stack.remove(key)
        self.stack.append(key)
        return self.cache_data[key]
