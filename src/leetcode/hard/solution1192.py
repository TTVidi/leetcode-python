# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network
# where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other
# server directly or indirectly through the network.
#
# A critical connection is a connection that, if removed, will make some server unable to reach some other server.
#
# Return all critical connections in the network in any order.
#
#
#
# Example 1:
#
#
#
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
#
#
# Constraints:
#
# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
# There are no repeated connections.
import collections
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(set)

        for connection in connections:
            graph[connection[0]].add(connection[1])
            graph[connection[1]].add(connection[0])

        rs = []
        distance = [-1] * n

        def search(node: int, parent: int, level: int) -> int:
            distance[node] = level + 1
            for nextNode in graph[node]:
                if nextNode == parent:
                    continue
                elif distance[nextNode] == -1:
                    distance[node] = min(distance[node], search(nextNode, node, level + 1))
                else:
                    distance[node] = min(distance[node], distance[nextNode])

            if distance[node] == level + 1 and node != 0:
                rs.append([parent, node])
            return distance[node]

        search(0, -1, 0)

        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.criticalConnections(6,
                                [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]))
