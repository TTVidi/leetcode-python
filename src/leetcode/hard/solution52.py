# N-Queens II

# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
# Example:
#
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Accepted
# 136,670
# Submissions
# 236,208
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        def find(i: int, j: int, l: List[int]) -> bool:
            for k, v in enumerate(l):
                if v == j or abs(i - k) == abs(j - v):
                    return False
            return True

        def recurse(i: int, l: List[int]) -> int:
            if len(l) == n:
                return 1
            else:
                k = 0
                for j in range(n):
                    if find(i, j, l):
                        l.append(j)
                        k += recurse(i + 1, l)
                        l.pop(-1)
                return k

        return recurse(0, [])


if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(4))
