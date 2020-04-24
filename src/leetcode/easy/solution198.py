# House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain amount
# of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security
# system connected and it will automatically contact the police if two adjacent houses were broken into on the same
# night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
# of money you can rob tonight without alerting the police.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            di = {0: nums[0], 1: max(nums[0], nums[1])}

            i = 2
            while i < len(nums):
                di[i] = max(di[i - 1], di[i - 2] + nums[i])
                i += 1
            return di[i - 1]


if __name__ == '__main__':
    s = Solution()
    l = []
    for i in range(1001):
        l.append(0)
    print(s.rob(l))
