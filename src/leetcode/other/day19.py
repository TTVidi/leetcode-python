# Search in Rotated Sorted Array
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(l,r):
            if l > r:
                return -1
            m = (r+l)//2
            if nums[m] == target:
                return m
            if nums[l] <= target < nums[m] or (nums[m] <= nums[r]  and not nums[m] < target <= nums[r]):
                return helper(l,m-1)
            else:
                return helper(m+1, r)
        return helper(0,len(nums)-1)


if __name__ == '__main__':
    s = Solution()
    print(s.search([4, 5, 6, 7, 8, 9, 1, 2, 3], 1))
