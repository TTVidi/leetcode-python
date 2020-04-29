# Minimum Value to Get Positive Step by Step Sum

# Given an array of integers nums, you start with an initial positive value startValue.
#
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
#
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.
#
#
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        _min = nums[0]
        _sum = nums[0]
        for i in range(1, len(nums)):
            _sum += nums[i]
            if _sum <= 0:
                _min = min(_min, _sum)
        if _min < 0:
            return -_min + 1
        return 1


if __name__ == '__main__':
    s = Solution()
    print(s.minStartValue([1, 2, 3, 5, 6, 7, 8]))
