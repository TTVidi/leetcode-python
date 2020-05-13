# Top K Frequent Elements

# Given a non-empty array of integers, return the k most frequent elements.
import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _map = collections.Counter(nums)
        _li = []
        _set = set()
        values = list(_map.values())
        values.sort(reverse=True)
        while k > 0:
            k -= 1
            _set.add(values.pop(0))
        for k, v in _map.items():
            if v in _set:
                _li.append(k)
        return _li


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3, 3, 3], 2))
