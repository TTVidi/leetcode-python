# Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target
# value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
#
# Constraints:
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non decreasing array.
# -10^9 <= target <= 10^9
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def find(left: int, right: int) -> int:
            if left > right:
                return -1
            if left == right:
                if nums[left] == target:
                    return left
                else:
                    return -1
            else:
                middle = (left + right) >> 1
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    return find(middle + 1, right)
                else:
                    return find(left, middle - 1)

        idx = find(0, len(nums))
        if idx >= 0:
            l = idx - 1
            r = idx + 1
            while l >= 0:
                if nums[l] == target:
                    l -= 1
                    continue
                else:
                    break
            while r < len(nums):
                if nums[r] == target:
                    r += 1
                    continue
                else:
                    break
            return [l + 1, r - 1]

        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
