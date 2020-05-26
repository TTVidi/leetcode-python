# Sort Colors

# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
# adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        zero_idx = 0
        two_idx = len(nums) - 1
        i = 0
        while i <= two_idx:
            if nums[i] == 0:
                swap(i, zero_idx)
                zero_idx += 1
                i += 1
            elif nums[i] == 2:
                swap(i, two_idx)
                two_idx -= 1
            elif nums[i] == 1:
                i += 1
        print(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.sortColors([2, 0, 1]))
