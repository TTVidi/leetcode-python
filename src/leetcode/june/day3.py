#  Two City Scheduling

# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][
# 0], and the cost of flying the i-th person to city B is costs[i][1].
#
# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        from queue import PriorityQueue
        priority = PriorityQueue()

        for i, v in enumerate(costs):
            priority.put((-abs(v[0] - v[1]), i))
        n = len(costs)
        a = n >> 1
        b = a
        s = 0
        while not priority.empty():
            idx = priority.get()[1]
            cost = costs[idx]
            if a == 0:
                s += cost[1]
            elif b == 0:
                s += cost[0]
            else:
                if cost[0] > cost[1]:
                    s += cost[1]
                    b -= 1
                else:
                    s += cost[0]
                    a -= 1
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
