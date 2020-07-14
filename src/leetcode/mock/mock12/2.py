# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product
# of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4] Output: [24,12,8,6] Constraint: It's guaranteed that the product of the elements of any prefix or
# suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up: Could you solve it with constant space complexity? (The output array does not count as extra space for
# the purpose of space complexity analysis.)
#
#
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        for num in nums:
            if num == 0:
                if zero == 0:
                    zero = 1
                else:
                    zero = 2
                    product = 0
            else:
                product *= num

        rs = []
        for num in nums:
            if num == 0:
                if zero == 1:
                    rs.append(product)
                else:
                    rs.append(0)
            else:
                if zero > 0:
                    rs.append(0)
                else:
                    rs.append(product // num)
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([0, 2, 3, 4]))
