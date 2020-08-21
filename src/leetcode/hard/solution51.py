# N-Queens

# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a
# queen and an empty space respectively.
#
# Example:
#
# Input: 4
# Output: [
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
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def find(i: int, j: int, l: List[int]) -> bool:
            for k, v in enumerate(l):
                if v == j or abs(i - k) == abs(j - v):
                    return False
            return True

        def recurse(i: int, l: List[int]):
            if len(l) == n:
                tp = []
                for v in l:
                    rest = n - v - 1
                    t = (("." * v) + "Q" + "." * rest)
                    tp.append(t)
                res.append(tp)
            else:
                for j in range(n):
                    if find(i, j, l):
                        l.append(j)
                        recurse(i + 1, l)
                        l.pop(-1)

        recurse(0, [])

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
