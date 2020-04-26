# Jump Game

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = len(nums) - 1
        pre = idx
        while idx >= 0:
            if idx + nums[idx] >= pre:
                pre = idx
            idx -= 1
        return pre == 0


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([0,2,3]))
