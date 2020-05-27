# Contiguous Array

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum = 0
        dp = {0: 0}
        m = 0
        for i, v in enumerate(nums):
            sum += (v << 1) - 1
            if sum in dp:
                m = max(m, i + 1 - dp[sum])
            else:
                dp[sum] = i + 1
        return m


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxLength([0, 1]))
