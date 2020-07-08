# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
# extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
#
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        s = 0
        for v in nums:
            if v == val:
                break
            else:
                s += 1
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([2]
                          , 2))
