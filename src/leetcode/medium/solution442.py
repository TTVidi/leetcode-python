# Find All Duplicates in an Array

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                res.append(idx + 1)
            nums[idx] = -nums[idx]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
