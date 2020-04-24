# Minimum Falling Path Sum

# Given a square array of integers A, we want the minimum sum of a falling path through A.
#
# A falling path starts at any element in the first row, and chooses one element from each row.  The next row's
# choice must be in a column that is different from the previous row's column by at most one.
#
import sys
from typing import List


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        length = len(A)
        if length == 1:
            return A[0][0]
        i = 1
        min_path = sys.maxsize
        while i < length:
            for j in range(length):
                if j == 0:
                    A[i][j] += min(A[i - 1][j + 1], A[i - 1][j])
                elif j == length - 1:
                    A[i][j] += min(A[i - 1][j - 1], A[i - 1][j])
                else:
                    A[i][j] += min(A[i - 1][j - 1], A[i - 1][j + 1], A[i - 1][j])
                if i == length - 1:
                    min_path = min(min_path, A[i][j])
            i += 1

        return min_path


if __name__ == '__main__':
    s = Solution()
    # print(s.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(s.minFallingPathSum([[1]]))
