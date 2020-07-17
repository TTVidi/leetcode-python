# Daily Temperatures

# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days
# you would have to wait until a warmer temperature. If there is no future day for which this is possible,
# put 0 instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4,
# 2, 1, 1, 0, 0].
#
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range
# [30, 100].
#
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        dp = {}

        def find(l: List[int], index: int) -> int:
            r = -1
            for c in l:
                if c > index:
                    r = c - index
                    break
            return r

        for i, v in enumerate(T):
            if v in dp:
                dp[v].append(i)
            else:
                dp[v] = [i]

        rs = []
        for i, v in enumerate(T):
            flag = False
            diff = len(T)
            for t in range(v + 1, 101):
                if t in dp:
                    f = find(dp[t], i)
                    if f > 0:
                        diff = min(diff, f)
                        flag = True
            if not flag:
                rs.append(0)
            else:
                rs.append(diff)

        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
