# Make Two Arrays Equal by Reversing Sub-arrays

# Given two integer arrays of equal length target and arr.
#
# In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.
#
# Return True if you can make arr equal to target, or False otherwise.
import collections
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        a1 = collections.Counter(arr)
        a2 = collections.Counter(target)
        for k, v in a2.items():
            if k in a1 and a1[k] == v:
                continue
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
