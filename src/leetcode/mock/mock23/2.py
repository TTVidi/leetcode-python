# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
#
#
#
# Example 1:
#
# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# Example 2:
#
# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]
#
#
# Note:
#
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        l1 = len(matrix)
        l2 = len(matrix[0])
        m = l1 * l2

        def find_distance(i: int, j: int, direction: int, se: set) -> int:
            if i < 0 or i >= l1 or j < 0 or j >= l2:
                return m
            if matrix[i][j] <= 0:
                return abs(matrix[i][j])

            up = 8
            down = 2
            left = 4
            right = 6
            l, r, d, u = m, m, m, m

            search_flag = True

            se.add((i, j))

            if direction != up:
                if (i + 1, j) not in se:
                    d = find_distance(i + 1, j, down, se)
                    if d == 0:
                        search_flag = False

            if direction != down and search_flag:
                if (i - 1, j) not in se:
                    u = find_distance(i - 1, j, up, se)
                    if u == 0:
                        search_flag = False

            if direction != left and search_flag:
                if (i, j + 1) not in se:
                    r = find_distance(i, j + 1, right, se)
                    if r == 0:
                        search_flag = False

            if direction != right and search_flag:
                if (i, j - 1) not in se:
                    l = find_distance(i, j - 1, left, se)

            distance = min(l, r, d, u) + 1
            matrix[i][j] = -distance
            se.remove((i, j))
            return distance

        for i, v in enumerate(matrix):
            for j, k in enumerate(v):
                if k == 1:
                    find_distance(i, j, 0, set())

        for i in range(l1):
            for j in range(l2):
                if matrix[i][j] < 0:
                    matrix[i][j] = -matrix[i][j]
        return matrix


if __name__ == '__main__':
    s = Solution()
    print(s.updateMatrix(
        [[0, 0, 1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
         [1, 0, 1, 1, 1, 0, 1, 1, 1, 0]]))
    print(s.updateMatrix(
        [[0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1]]))
