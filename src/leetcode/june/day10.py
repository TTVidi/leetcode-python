# Search Insert Position

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
# would be if it were inserted in order.
#
# You may assume no duplicates in the array.
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def find(left: int, right: int) -> int:
            if nums[left] >= target:
                return left
            if nums[right] == target:
                return right
            if nums[right] < target:
                return right + 1
            middle = (left + right) >> 1
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                return find(left + 1, middle)
            if nums[middle] < target:
                return find(middle, right - 1)

        return find(0, len(nums) - 1)

    def searchInsert1(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] >= target:
                return left
            if nums[right] == target:
                return right
            if nums[right] < target:
                return right + 1
            middle = (left + right) >> 1
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                left += 1
                right = middle
            if nums[middle] < target:
                left = middle
                right -= 1
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert1([1, 3, 5, 6], 7))
