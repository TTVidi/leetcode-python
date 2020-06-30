# Triangle

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle:
            length = len(triangle)
            li = triangle[0]
            m = li[0]
            for i in range(1, length):
                li.append(li[-1])
                current = triangle[i]
                current[0] = li[0] + current[0]
                m = current[0]
                for j in range(1, len(current)):
                    current[j] = current[j] + min(li[j], li[j - 1])
                    m = min(m, current[j])
                li = current
            return m


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
