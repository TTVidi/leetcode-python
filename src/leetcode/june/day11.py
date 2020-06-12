# Sort Colors

# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
# adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        z = 0
        t = len(nums) - 1
        i = 0
        while i <= t:
            if nums[i] == 0:
                nums[i], nums[z] = nums[z], nums[i]
                i += 1
                z += 1
            elif nums[i] == 2:
                nums[i], nums[t] = nums[t], nums[i]
                t -= 1
            else:
                i += 1
        print(nums)


if __name__ == '__main__':
    s = Solution()
    s.sortColors([2, 0, 2, 1, 1, 0])
