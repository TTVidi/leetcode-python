# Maximum Average Subarray I

# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum
# average value. And you need to output the maximum average value.
#
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]
        m = s
        j = k
        while j < len(nums):
            s = s + nums[j] - nums[j - k]
            m = max(m, s)
            j += 1
        return m / k
