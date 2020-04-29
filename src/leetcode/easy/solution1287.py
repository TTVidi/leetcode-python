# Element Appearing More Than 25% In Sorted Array

# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.
#
# Return that integer.
import collections
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        _dict = collections.Counter(arr)
        length = len(arr)
        length >>= 2
        for k, v in _dict.items():
            if v > length:
                return k


if __name__ == '__main__':
    s = Solution()
    print(s.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
