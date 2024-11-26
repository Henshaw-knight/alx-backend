#!/usr/bin/env python3
""" LFUCache class module """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A caching system with no limit, has the put and get method"""
    def __init__(self):
        """Instantiates the class"""
        super().__init__()
        self.stack = {}  # Tracks the order of keys for LFU
        # self.discard_list = []

    def put(self, key, item):
        """Assigns to the dictionary `self.cache_data` the item `value`
        for the key `key`
        - if key or item is None, the method does not do anything
        - if the number of items in self.cache_data is higher than
          BaseCaching.MAX_ITEMS, the least frequently used item is discarded
          (LFU algorithm)
        - if more than 1 item are to be discarded, LRU algorithm will
        be used to discard least recently used
        - DISCARD: with the key discarded followed by a new line is printed
        """
        if key and item:
            # if key exists, its value is updated and it is moved to the top
            # of the stack
            if key in self.cache_data:
                current_count = self.stack.pop(key)
            else:
                current_count = 0
            self.cache_data[key] = item
            self.stack[key] = current_count + 1

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                keys = list(self.stack.keys())
                min_count = float('inf')
                min_key = None

                for key, value in self.stack.items():
                    if (value < min_count and keys.index(key)
                            != len(keys) - 1):
                        min_count = value
                        min_key = key
                # self.discard_list.append(min_key)
                # least_frequently_used_key = self.discard_list.pop(0)
                least_frequently_used_key = min_key
                del self.cache_data[least_frequently_used_key]
                self.stack.pop(least_frequently_used_key)
                # self.discard_list.clear()
                print("DISCARD: {}".format(least_frequently_used_key))

    def get(self, key):
        """Returns the value in self.cache_data linked to key"""
        if key is None or self.cache_data.get(key) is None:
            # dictionary get method
            return None
        value = self.stack.pop(key)
        self.stack[key] = value + 1
        return self.cache_data[key]
