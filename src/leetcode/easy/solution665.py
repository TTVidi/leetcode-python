# Non-decreasing Array
# Given an array nums with n integers, your task is to check if it could become non-decreasing
# by modifying at most 1 element.
#
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n -
# 2).
#
#
#
# Example 1:
#
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
#
# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one element.
#
#
# Constraints:
#
# 1 <= n <= 10 ^ 4
# - 10 ^ 5 <= nums[i] <= 10 ^ 5
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i = 1
        pre = nums[0]
        length = len(nums)
        while i < len(nums):
            current = nums[i]
            if current < pre:
                break
            pre = current
            i += 1
        if i >= length - 1:
            return True

        if i == 1:
            nums[0] = nums[1]
        else:
            if nums[i] >= nums[i - 2]:
                nums[i - 1] = nums[i - 2]
            else:
                nums[i] = nums[i - 1]

        pre = nums[0]
        for j in range(1, length):
            if nums[j] < pre:
                return False
            pre = nums[j]
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkPossibility([4, 2, 1]))
    print(s.checkPossibility([1, 2, 3, 4]))
    print(s.checkPossibility([1, 2, 3, 2]))
    print(s.checkPossibility([-1, 4, 2, 3]))
    print(s.checkPossibility([4, 2, 3]))
