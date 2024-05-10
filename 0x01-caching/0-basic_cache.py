#!/usr/bin/env python3
"""
Basic Cache Module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class inherits from BaseCaching """
    def put(self, key, item):
        """ Assigns self.cache_data the item value for the key """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data dictionary linked to key """
        return self.cache_data.get(key, None)
