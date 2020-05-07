# Majority Element
#
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊
# n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for c in nums:
            if candidate == c:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = c
                    count = 1
        return candidate


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([6, 5, 5, 6, 5]))
