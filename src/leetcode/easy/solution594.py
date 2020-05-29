# Longest Harmonious Subsequence

# We define a harmounious array as an array where the difference between its maximum value and its minimum value is
# exactly 1.
#
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its
# possible subsequences.
#
import collections
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ma = collections.Counter(nums)
        m = 0
        for i, v in ma.items():
            next = i + 1
            if next in ma:
                m = max(m, v + ma[next])
        return m


if __name__ == '__main__':
    s = Solution()
    print(s.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
