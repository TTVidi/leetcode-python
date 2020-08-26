# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
#
# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the
# floor, and you can either start from the step with index 0, or the step with index 1.
import random
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
    so = Solution()
    print(so.minCostClimbingStairs([3, 19, 10, 12, 13, 6, 1, 19, 13, 12, 20, 14, 18, 11, 10, 11, 8, 12, 4, 8, 19, 19, 10, 3]))
    # case = "C://Users//tangtao02//Desktop//算法/2/case.txt"
    # result = "C://Users//tangtao02//Desktop//算法/2/result.txt"
    # c = open(case, 'w+')
    # r = open(result, 'w+')
    #
    # cr = []
    # rr = []
    #
    # for i in range(100):
    #     j = random.randint(2, 30)
    #     li = []
    #
    #     for k in range(j):
    #         li.append(random.randint(0, 20))
    #
    #     cr.append(str(li) + "\n")
    #     rr.append(str(so.minCostClimbingStairs(li)) + "\n")
    #
    # c.writelines(cr)
    # r.writelines(rr)
    # c.close()
    # r.close()
