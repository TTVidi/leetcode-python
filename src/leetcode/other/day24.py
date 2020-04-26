# LRU Cache

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following
# operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
# it should invalidate the least recently used item before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.size:
                self.cache.popitem(last=False)
        else:
            self.cache.move_to_end(key)
        self.cache[key] = value


if __name__ == '__main__':
    cache = LRUCache(2)
    print(cache.put(2, 1))
    print(cache.put(2, 2))
    print(cache.get(2))
    print(cache.put(1, 1))
    print(cache.put(4, 1))
    print(cache.get(2))
