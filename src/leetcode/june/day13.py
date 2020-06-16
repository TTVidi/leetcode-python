# Largest Divisible Subset

# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in
# this subset satisfies:
#
# Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        return []


if __name__ == '__main__':
    s = Solution()
    print(s.largestDivisibleSubset([1, 8, 4, 2]))
