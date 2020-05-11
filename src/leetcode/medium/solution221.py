# Maximal Square

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix:
            square = 0
            _s = set()
            _c = set()
            r = len(matrix)
            c = len(matrix[0])
            for i, v in enumerate(matrix):
                for j, k in enumerate(v):
                    if k == "1":
                        _s.add(str(i + 1) + "," + str(j + 1))
                        _c.add(str(i + 1) + "," + str(j + 1))

            while square < min(r, c) and _s:
                square += 1
                temp = set()
                for v in _s:
                    vs = v.split(",")
                    i = int(vs[0])
                    j = int(vs[1])

                    contains = True
                    for k in range(square + 1):
                        v0 = str(i + square) + "," + str(k + j)
                        v1 = str(i + k) + "," + str(j + square)
                        if _c.__contains__(v0) and _c.__contains__(v1):
                            continue
                        else:
                            contains = False
                            break
                    if contains:
                        temp.add(str(i) + "," + str(j))
                _s = temp
            return square * square
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.maximalSquare(
        [["1", "1", "0", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "1", "1", "1", "1"]]))
