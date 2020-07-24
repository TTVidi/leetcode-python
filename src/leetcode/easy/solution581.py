# Shortest Unsorted Continuous Subarray

# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending
# order, then the whole array will be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        copy = nums.copy()
        copy.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            if copy[i] != nums[i]:
                break
            i += 1
        if i == j:
            return 0
        while i < j:
            if copy[j] != nums[j]:
                break
            j -= 1

        return j - i + 1


if __name__ == '__main__':
    s = Solution()
    print(s.findUnsortedSubarray([1, 2, 4, 5]))
