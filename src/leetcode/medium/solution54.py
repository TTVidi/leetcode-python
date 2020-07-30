# Spiral Matrix

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            total = m * n
            dir = 6
            i = 0
            j = 0
            while m > 1 and n > 1:
                if dir == 6:
                    for k in range(n - 1):
                        res.append(matrix[i][j])
                        j += 1
                    dir = 2
                elif dir == 2:
                    for k in range(m - 1):
                        res.append(matrix[i][j])
                        i += 1
                    dir = 4
                elif dir == 4:
                    for k in range(n - 1):
                        res.append(matrix[i][j])
                        j -= 1
                    dir = 8
                else:
                    # dir==8
                    for k in range(m - 1):
                        res.append(matrix[i][j])
                        i -= 1
                    i += 1
                    j += 1
                    m -= 2
                    n -= 2
                    dir = 6
            if total != len(res):
                if m > 1:
                    for k in range(m):
                        res.append(matrix[i][j])
                        i += 1
                else:
                    for k in range(n):
                        res.append(matrix[i][j])
                        j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.spiralOrder([[0]]))
    print(s.spiralOrder([[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12]]))
    print(s.spiralOrder([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]]))
    print(s.spiralOrder([[2, 5, 8],
                         [4, 0, -1]]))
    print(s.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
    #
    # print(s.spiralOrder([
    #     [1, 2],
    #     [3, 4],
    #     [5, 6]
    # ]))
    #
    # print(s.spiralOrder([
    #     [1, 2, 3, 4, 5],
    #     [10, 9, 8, 7, 6],
    #     [11, 12, 13, 14, 15]
    # ]))
    #
    # print(s.spiralOrder([
    #     [1, 10, 11],
    #     [2, 9, 12],
    #     [3, 8, 13],
    #     [4, 7, 14],
    #     [5, 6, 15]
    # ]))
