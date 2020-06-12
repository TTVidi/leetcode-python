# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
# corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def find(i: int, j: int) -> int:
            key = (i, j)
            if key in dp:
                return dp[key]
            if j == 1:
                dp[key] = 1
                return 1
            elif i == 1:
                dp[key] = 1
                return 1
            else:
                k = find(i - 1, j) + find(i, j - 1)
                dp[key] = k
                return k

        return find(m, n)
