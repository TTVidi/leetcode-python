# Score After Flipping Matrix

# We have a two dimensional matrix A where each value is 0 or 1.
#
# A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to
# 1s, and all 1s to 0s.
#
# After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the
# matrix is the sum of these numbers.
#
# Return the highest possible score.
#
#
#
# Example 1:
#
# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
#
#
# Note:
#
# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] is 0 or 1.
# Accepted
# 21,538
# Submissions
# 29,602
from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        l1 = len(A)
        l2 = len(A[0])
        for i in range(l1):
            if A[i][0] == 0:
                for j in range(l2):
                    A[i][j] = 1 - A[i][j]

        for j in range(1, l2):
            zc = 0
            oc = 0
            for i in range(l1):
                if A[i][j] == 0:
                    zc += 1
                else:
                    oc += 1

            if zc > oc:
                for i in range(l1):
                    A[i][j] = 1 - A[i][j]

        res = 0
        j = l2 - 1
        base = 1
        while j >= 0:
            ts = 0
            for i in range(l1):
                ts += A[i][j]
            ts *= base
            res += ts
            base <<= 1
            j -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
