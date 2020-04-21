# Contiguous Array
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c, d, m = 0, {0: 0}, 0
        for i, v in enumerate(nums):
            c += 2 * v - 1
            if c in d:
                m = max(m, i + 1 - d[c])
            else:
                d[c] = i + 1
        return m


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxLength([0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0]))
    # print(s.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]))
    # print(s.findMaxLength(
    #     [0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1,
    #      1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0,
    #      0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1]))
