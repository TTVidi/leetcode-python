# Largest Divisible Subset


# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in
# this subset satisfies:
#
# Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# Example 2:
#
# Input: [1,2,4,8]
# Output: [1,2,4,8]
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if nums:
            nums.sort()
            res = []
            dp = {}
            dp[0] = [nums[0]]

            def find(idx: int) -> List[int]:
                if idx in dp:
                    return dp[idx]
                l = []
                k = nums[idx]
                for i in range(idx):
                    if k % nums[i] == 0:
                        r = find(i)
                        if len(r) >= len(l):
                            l = r.copy()
                l.append(nums[idx])
                dp[idx] = l
                return l

            for i in range( len(nums)):
                t = find(i)
                if len(t) >= len(res):
                    res = t

            return res


if __name__ == '__main__':
    s = Solution()
    print(s.largestDivisibleSubset([1, 2, 4, 8]))
    print(s.largestDivisibleSubset([1]))
