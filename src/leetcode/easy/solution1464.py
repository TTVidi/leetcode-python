# Maximum Product of Two Elements in an Array

# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum
# value of (nums[i]-1)*(nums[j]-1).
#
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = 0
        m2 = 0
        if nums[0] > nums[1]:
            m1 = nums[0]
            m2 = nums[1]
        else:
            m1 = nums[1]
            m2 = nums[0]
        for i in range(2, len(nums)):
            if nums[i] >= m1:
                m2 = m1
                m1 = nums[i]
            elif nums[i] > m2:
                m2 = nums[i]
        return (m2 - 1) * (m1 - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([3, 4, 5, 2]))
