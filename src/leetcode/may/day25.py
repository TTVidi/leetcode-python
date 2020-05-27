# Uncrossed Lines

# We write the integers of A and B (in the order they are given) on two separate horizontal lines.
#
# Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:
#
# A[i] == B[j]; The line we draw does not intersect any other connecting (non-horizontal) line. Note that a
# connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.
#
# Return the maximum number of connecting lines we can draw in this way.
#
#
# 该题意为将上下两行数组中相等元素使用不交叉的直线相连，问最多有多少条这样的直线？这道题我们可使用动态规划的思想求解：

# 确定状态:

# 题目要求数组A[a1,a2…ai]和数组B[b1,b2..bj]最多有多少条不交叉的连线，我们假设最优策略中ai==bj,也就是ai和bj相连,此时转化成子问题: 求数组A[a1,a2…ai-1]和数组B[b1,b2…bj-1]最多有多少条不交叉的连线，所以我们定义dp[i][j]表示数组A[a1,a2…ai]和数组B[b1,b2…bj]最多有多少条不交叉的连线。

# 转移方程:

# 设状态dp[i][j]=数组A[a1..ai]和数组B[b1…bj]最多有多少条不交叉的连线，对于任意的i,j都有：

# dp[i][j] = dp[i-1][j-1]+1 当A[i]=B[j]时
# dp[i][j] = max{dp[i-1][j], dp[i][j-1]} 当A[i] != B[j]时
# 初始条件和边界情况

# dp[0][0] = 0
# dp[i][j]就是最后结果
# 算法时间复杂度为O(mn)m n分别为数组A和B的长度
# 空间复杂度为O(mn)
#
from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        la = len(A)
        lb = len(B)
        dp = [[0] * lb for i in range(la)]
        one_idx = la
        for i, v in enumerate(A):
            if i > one_idx:
                dp[i][0] = 1
            else:
                if v == B[0]:
                    dp[i][0] = 1
                    one_idx = i
                else:
                    dp[i][0] = 0

        one_idx = lb
        for j, v in enumerate(B):
            if j > one_idx:
                dp[0][j] = 1
            else:
                if v == A[0]:
                    dp[0][j] = 1
                    one_idx = j
                else:
                    dp[0][j] = 0

        for i in range(1, la):
            for j in range(1, lb):
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp.pop(-1).pop(-1)


if __name__ == '__main__':
    s = Solution()
    print(s.maxUncrossedLines([2, 5, 1, 2, 5],
                              [10, 5, 2, 1, 5, 2]))
