# Search a 2D Matrix

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix:
            def bit_search(left: int, right: int, row: int) -> bool:
                if 0 <= left <= right <= len(matrix[row]) - 1:
                    if left == right:
                        return matrix[row][left] == target
                    middle = (left + right) >> 1
                    if matrix[row][middle] == target:
                        return True
                    elif matrix[row][middle] < target:
                        return bit_search(middle + 1, right, row)
                    return bit_search(left, middle - 1, row)
                return False

            left = 0
            right = len(matrix) - 1
            length = len(matrix[0])
            while left <= right:
                if left == right:
                    break
                middle = (left + right) >> 1
                if matrix[middle][0] <= target <= matrix[middle][length - 1]:
                    left = middle
                    break
                elif matrix[middle][0] > target:
                    right = middle - 1
                elif matrix[middle][length - 1] < target:
                    left = middle + 1

            return bit_search(0, length - 1, left)
        return False
