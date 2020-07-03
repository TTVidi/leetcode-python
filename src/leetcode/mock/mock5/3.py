# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
#
# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the
# floor, and you can either start from the step with index 0, or the step with index 1.
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = []
        dp.append(cost[0])
        dp.append(cost[1])
        for i in range(2, len(cost)):
            dp.append(min(dp[i - 2] + cost[i], dp[i - 1] + cost[i]))

        l1 = dp.pop(-1)
        l2 = dp.pop(-1)
        return min(l1, l2)


if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
