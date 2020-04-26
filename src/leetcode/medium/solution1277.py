# Count Square Submatrices with All Ones
# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row_length = len(matrix)
        column_length = len(matrix[0])
        li = []
        sum = 0
        for i, row in enumerate(matrix):
            for j, column in enumerate(row):
                if column == 1:
                    li.append([i, j])
                    sum += 1
        base = 2
        while li and base <= row_length and base <= column_length:
            temp = []
            for v in li:
                i = v[0]
                j = v[1]
                if i + base <= row_length and j + base <= column_length:
                    success = True
                    for x in range(j, j + base):
                        if matrix[i + base - 1][x] == 0:
                            success = False
                            break
                    if success:
                        for y in range(i, i + base - 1):
                            if matrix[y][j + base - 1] == 0:
                                success = False
                                break
                        if success:
                            temp.append([i, j])
                            sum += 1
            li = temp
            base += 1
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.countSquares([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]))
    print(s.countSquares([
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]))
    print(s.countSquares([
        [0, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1]
    ]))
