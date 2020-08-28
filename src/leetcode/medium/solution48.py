# Rotate Image

# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
# another 2D matrix and do the rotation.
#
# Example 1:
#
# Given input matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# Example 2:
#
# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        length = len(matrix)

        def circleConvert(i: int, j: int):
            t = length
            temp = matrix[i][j]
            matrix[i][j] = matrix[t - j - 1][i]
            matrix[t - j - 1][i] = matrix[t - i - 1][t - j - 1]
            matrix[t - i - 1][t - j - 1] = matrix[j][t - i - 1]
            matrix[j][t - i - 1] = temp

        k = (length >> 1)
        i = 0
        j = 0
        m = length
        while k > 0:
            for l in range(j, m - 1):
                circleConvert(i, l)
            i += 1
            j += 1
            m -= 1
            k -= 1


if __name__ == '__main__':
    s = Solution()
    s.rotate([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    s.rotate([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ])
