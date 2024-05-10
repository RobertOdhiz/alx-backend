#!/usr/bin/env python3
""" LIFOCache Module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits BaseCaching """
    def __init__(self):
        """ intializes LIFOCache class """
        super().__init__()

    def put(self, key, item):
        """ Assign item to the value for the key key """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_item_key = next(reversed(self.cache_data))
                del self.cache_data[last_item_key]
                print("DISCARD: {}".format(last_item_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value linked to the key """
        if key is not None:
            return self.cache_data.get(key)
        return None
