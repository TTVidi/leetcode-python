# Find Lucky Integer in an Array

# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
#
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is
# no lucky integer return -1.
#
import collections
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        rs = -1
        _dict = collections.Counter(arr)

        for k, v in _dict.items():
            if k == v:
                rs = max(rs, k)
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.findLucky([2, 2, 2, 3, 3]))
