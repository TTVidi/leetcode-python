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
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dp = {}
        for connection in connections:
            fi = connection[0]
            se = connection[1]
            if fi in dp:
                dp[fi].add(se)
            else:
                dp[fi] = set()
                dp[fi].add(se)

            if se in dp:
                dp[se].add(fi)
            else:
                dp[se] = set()
                dp[se].add(fi)
        for k, v in dp.items():
            if len(v) == 1:
                print(1)
        rs = []
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
