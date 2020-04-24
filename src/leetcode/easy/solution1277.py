# Count Square Submatrices with All Ones
# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        length = max(len(matrix), len(matrix[0]))
        li = []
        sum = 0
        for i, row in enumerate(matrix):
            for j, column in enumerate(row):
                if column == 1:
                    li.append([i, j])
                    sum += 1
        for i in range(length):
            print(i)
        return li


if __name__ == '__main__':
    s = Solution()
    q = s.countSquares([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ])
