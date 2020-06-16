# Find Pivot Index

# Given an array of integers nums, write a method that returns the "pivot" index of this array.
#
# We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the
# sum of all the numbers to the right of the index.
#
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most
# pivot index.
#
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        j = 0
        c = 0
        while j < len(nums):
            rest = s - c - nums[j]
            if rest == c:
                return j
            c += nums[j]
            j += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.pivotIndex([-1, -1, 0, 0, -1, -1]))
