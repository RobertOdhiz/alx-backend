#!/usr/bin/env python3
from base_caching import BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    """LRUCache class inherits from BaseCaching"""

    def __init__(self):
        """Initialize LRUCache"""
        super().__init__()
        self.lru_cache = OrderedDict()

    def put(self, key, item):
        """Assigns item value for the key in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = next(iter(self.lru_cache))
                del self.cache_data[lru_key]
                del self.lru_cache[lru_key]
                print("DISCARD:", lru_key)

            self.cache_data[key] = item
            self.lru_cache[key] = None

    def get(self, key):
        """Returns the value associated with the given key"""
        if key is not None:
            if key in self.lru_cache:
                del self.lru_cache[key]
                self.lru_cache[key] = None
            return self.cache_data.get(key)
        return None
