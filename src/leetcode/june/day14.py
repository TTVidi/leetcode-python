# Cheapest Flights Within K Stops

# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and the destination dst, your task is to find
# the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
#
import heapq
import sys
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adj = {u: [] for u in range(n)}
        for f in flights:
            adj[f[0]].append((f[1], f[2]))

        Q = []
        Q.append((0, src, K + 1))

        while len(Q) > 0:
            top = heapq.heappop(Q)
            d = top[0]
            u = top[1]
            k = top[2]
            if dst == u:
                return d
            if k > 0:
                for v in adj[u]:
                    heapq.heappush(Q, (d + v[1], v[0], k - 1))
        return -1


    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        di = {}
        for flight in flights:
            src_c = flight[0]
            dest = flight[1]
            cost = flight[2]
            t = {}
            if src_c in di:
                t = di[src_c]
            t[dest] = cost
            di[src_c] = t

        rs = {}

        def find_cost(current: int, k: int, path: set, total: int) -> int:
            current_cost = sys.maxsize
            if current in rs:
                for mi, min_cost in rs[current]:
                    if k >= mi:
                        current_cost = min(current_cost, min_cost)
                if current_cost != sys.maxsize:
                    rs[current][k] = current_cost
                    return current_cost
            if k == 0:
                if current == dst:
                    return total
                return -1
            if current == dst:
                return total
            if current not in di:
                return -1
            destinations = di[current]

            for key, value in destinations.items():
                if key not in path:
                    path.add(key)
                    ne = find_cost(key, k - 1, path, total + value)
                    if ne != -1:
                        current_cost = min(current_cost, ne)
                    path.remove(key)

            if current_cost == sys.maxsize:
                return -1

            return current_cost

        if K == 0:
            if src in di and dst in di[src]:
                return di[src][dst]
            return -1

        if src in di:
            c = sys.maxsize
            se = set()
            for k, v in di[src].items():
                se.add(k)
                co = find_cost(k, K, se, v)
                if co != -1:
                    c = min(c, co)
                se.remove(k)
            if c == sys.maxsize:
                c = -1
            return c
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
