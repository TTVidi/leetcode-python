# Spiral Matrix II

# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0] * n for i in range(n)]
        i = 0
        j = 0
        idx = 1
        while n > 1:
            for k in range(n):
                arr[i][j] = idx
                idx += 1
                j += 1

            j -= 1
            i += 1

            for k in range(n - 1):
                arr[i][j] = idx
                idx += 1
                i += 1

            i -= 1
            j -= 1

            for k in range(n - 1):
                arr[i][j] = idx
                idx += 1
                j -= 1

            j += 1
            i -= 1

            for k in range(n - 2):
                arr[i][j] = idx
                idx += 1
                i -= 1

            i += 1
            j += 1

            n -= 2

        if n == 1:
            arr[i][j] = idx
        return arr


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(1))
    print(s.generateMatrix(2))
    print(s.generateMatrix(3))
    print(s.generateMatrix(4))
    print(s.generateMatrix(5))
