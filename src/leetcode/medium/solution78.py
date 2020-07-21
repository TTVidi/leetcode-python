#  Subsets
# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rs = []
        temp = []
        for num in nums:
            if rs:
                for v in rs:
                    temp.append(v)
                    c = v.copy()
                    c.append(num)
                    temp.append(c)
            temp.append([num])
            rs = temp
            temp = []
        rs.append([])
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3, 4]))
