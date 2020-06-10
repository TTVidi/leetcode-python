# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node,
# v is the target node, and w is the time it takes for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is
# impossible, return -1.
#
import collections
from typing import List


class Solution:
    def networkDelayTime1(self, times: List[List[int]], N: int, K: int) -> int:
        K -= 1
        nodes = collections.defaultdict(list)
        for u, v, w in times:
            nodes[u - 1].append((v - 1, w))
        dist = [float('inf')] * N
        dist[K] = 0
        done = set()
        for _ in range(N):
            smallest = min((d, i) for (i, d) in enumerate(dist) if i not in done)[1]
            for v, w in nodes[smallest]:
                if v not in done and dist[smallest] + w < dist[v]:
                    dist[v] = dist[smallest] + w
            done.add(smallest)
        return -1 if float('inf') in dist else max(dist)

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        li = [[0] * N for i in range(N)]
        for v in times:
            i = v[0] - 1
            j = v[1] - 1
            time = v[2]
            li[i][j] = time
        costs = [0] * N
        touched = []
        touched.append(K - 1)
        costs[K - 1] = 0
        while touched:
            i = touched.pop()
            cost = costs[i]
            next_times = li[i]
            for j, v in enumerate(next_times):
                if i == j:
                    continue
                if v != 0:
                    if costs[j] != 0:
                        costs[j] = min(costs[j], cost + v)
                    else:
                        if j != K - 1:
                            costs[j] = cost + v
                            touched.append(j)
        time = 0
        for i, v in enumerate(costs):
            if v == 0:
                if i == K - 1:
                    continue
                return -1
            time = max(time, v)
        return time


if __name__ == '__main__':
    s = Solution()
    print(s.networkDelayTime1([[1, 2, 1], [2, 1, 3]]
                             , 2
                             , 2))
