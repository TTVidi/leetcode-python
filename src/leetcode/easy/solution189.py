# Rotate Array

# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Follow up:
#
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
#
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            t = nums.pop(-1)
            nums.insert(0, t)
            k -= 1
        return None

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        t = nums[l - k:] + nums[:l - k]
        nums[0:] = t
        return None


if __name__ == '__main__':
    s = Solution()
    print(s.rotate2([1, 2, 3, 4, 5, 6, 7], 3))
