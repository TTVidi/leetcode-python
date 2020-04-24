# Minimum Subsequence in Non-Increasing Order
# Given the array nums, obtain a subsequence of the array whose sum of
# elements is strictly greater than the sum of the non included elements in such subsequence.
#
# If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple
# solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be
# obtained by erasing some (possibly zero) elements from the array.
#
# Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in
# non-increasing order.
#
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        sum = 0
        for num in nums:
            sum += num
        result = []
        current = 0
        for num in nums:
            result.append(num)
            sum -= num
            current += num
            if current > sum:
                break
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.minSubsequence([4]))
