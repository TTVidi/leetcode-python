# Product of Array Except Self Given an array nums of n integers where n > 1,  return an array output such that
# output[i] is equal to the product of all the elements of nums except nums[i].
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        i = 0
        while i < len(nums):
            p = nums[i]
            if nums[i] == 0:
                if zero_count == 0:
                    p = 1
                else:
                    product = 0
                    break
                zero_count += 1
            product *= p
            i += 1
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                if zero_count > 0:
                    nums[i] = 0
                else:
                    nums[i] = product // nums[i]
            else:
                if zero_count == 1:
                    nums[i] = product
            i += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([0, 1, 2, 3, 4]))
