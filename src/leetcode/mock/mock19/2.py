# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra
# space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            v = nums[i]
            if v < 0:
                v *= -1
            if nums[v - 1] > 0:
                nums[v - 1] = -nums[v - 1]
            i += 1
        rs = []
        for i, v in enumerate(nums):
            if v > 0:
                rs.append(i + 1)
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
