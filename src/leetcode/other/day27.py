# Maximal Square

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
from typing import List


class Solution:
    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        h = len(matrix)
        if h == 0:
            return 0
        w = len(matrix[0])
        dp = [0] * (w + 1)
        lmax = 0
        prev = 0
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = 1 + min(prev, dp[j - 1], dp[j])
                    lmax = max(lmax, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return lmax * lmax

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        _i_length = len(matrix)
        if _i_length == 0:
            return 0
        _j_length = len(matrix[0])

        _length = min(_i_length, _j_length)
        _li = []
        for i, v in enumerate(matrix):
            for j, l in enumerate(v):
                if l == "1":
                    _li.append([i, j])

        if not _li:
            return 0
        base = 1
        while _li:
            _temp = []
            for v in _li:
                i = v[0]
                j = v[1]
                _next_i = i + base
                _next_j = j + base
                if _next_i < _i_length and _next_j < _j_length:
                    _is_success = True
                    for k in range(base + 1):
                        if matrix[i + base][j + k] == '0' or matrix[i + k][j + base] == '0':
                            _is_success = False
                            break
                    if _is_success:
                        _temp.append([i, j])
            if _temp:
                _li = _temp
                base += 1
            else:
                return base * base


if __name__ == '__main__':
    s = Solution()
    print(s.maximalSquare2(
        [["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]]))
