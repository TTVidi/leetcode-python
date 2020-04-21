# Move Zeroes Given an array nums, write a function to move all 0's to the end of it while maintaining the relative
# order of the non-zero elements.
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = -1
        i = 0
        while i < len(nums):
            if nums[i] != 0 and i > current >= 0:
                nums[current], nums[i] = nums[i], nums[current]
                current += 1
            else:
                if nums[i] == 0 and current < 0:
                    current = i
            i += 1


if __name__ == '__main__':
    s = Solution()
    l2 = [0, 1, 0, 3, 12]
    # l2 = [1, 0, 0, 3, 12]
    s.moveZeroes(l2)
    print(l2)
