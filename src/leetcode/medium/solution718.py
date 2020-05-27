#  Maximum Length of Repeated Subarray

# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        la = len(A) + 1
        lb = len(B) + 1
        dp = [[0] * lb for i in range(la)]
        m = 0
        for i in range(1, la):
            for j in range(1, lb):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    m = max(m, dp[i][j])
                else:
                    dp[i][j] = 0
        return m

    def findLength2(self, A: List[int], B: List[int]) -> int:
        la = len(A) + 1
        lb = len(B) + 1
        dp = [[0] * lb for i in range(la)]
        for i in range(1, la):
            for j in range(1, lb):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp.pop(-1).pop(-1)


if __name__ == '__main__':
    s = Solution()
    print(s.findLength([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 8, 10, 9, 11]))
