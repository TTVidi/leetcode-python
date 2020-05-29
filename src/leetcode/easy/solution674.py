# Longest Continuous Increasing Subsequence

# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        m = 0
        if nums:
            m = 1
            c = 1
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    c += 1
                else:
                    m = max(m, c)
                    c = 1
            m = max(m, c)
        return m


if __name__ == '__main__':
    s = Solution()
    print(s.findLengthOfLCIS([1, 3, 5, 7]))
