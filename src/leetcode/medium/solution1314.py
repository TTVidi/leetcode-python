# Matrix Block Sum

# Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all
# elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
#
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        i_len = len(mat)
        j_len = len(mat[0])
        memo = [[0] * j_len for i in range(i_len)]
        rs = [[0] * j_len for i in range(i_len)]
        memo[0][0] = mat[0][0]
        for i, r in enumerate(mat):
            for j, v in enumerate(r):
                _r_sum = 0
                _c_sum = 0
                for k in range(j):
                    _r_sum += mat[i][k]
                for k in range(i):
                    _c_sum += mat[k][j]

                if i >= 1 and j >= 1:
                    memo[i][j] = memo[i - 1][j - 1] + _r_sum + _c_sum + mat[i][j]
                else:
                    memo[i][j] = _r_sum + _c_sum + mat[i][j]

        def get_memo(i: int, j: int) -> int:
            if i < 0:
                return 0
            elif i >= i_len:
                i = i_len - 1
            if j < 0:
                return 0
            elif j >= j_len:
                j = j_len - 1

            return memo[i][j]

        for i, r in enumerate(rs):
            for j, v in enumerate(r):
                top_left = get_memo(i - K - 1, j - K - 1)
                bottom_left = get_memo(i + K, j - K - 1)
                top_right = get_memo(i - K - 1, j + K)
                bottom_right = get_memo(i + K, j + K)
                rs[i][j] = bottom_right - bottom_left - top_right + top_left
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))
