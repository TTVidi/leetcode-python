# Max Sum of Rectangle No Larger Than K

# Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its
# sum is no larger than k.
#
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        return 1


if __name__ == '__main__':
    s = Solution()
    print(s.maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2))
