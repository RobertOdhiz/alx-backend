#!/usr/bin/env python3
""" FIFOCache Module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching """
    def __init__(self):
        """ Initializes FIFOCache """
        super().__init__()

    def put(self, key, item):
        """ assigns to the Dictionary the item value for the key key """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_item_key = next(iter(self.cache_data))
                del self.cache_data[first_item_key]
                print("DISCARD: {}".format(first_item_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value associated linked to the key """
        if key is not None:
            return self.cache_data.get(key)
