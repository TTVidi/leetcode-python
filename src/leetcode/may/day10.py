# Find the Town Judge

# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town
# judge.
#
# If the town judge exists, then:
#
# The town judge trusts nobody. Everybody (except for the town judge) trusts the town judge. There is exactly one
# person that satisfies properties 1 and 2. You are given trust, an array of pairs trust[i] = [a, b] representing
# that the person labelled a trusts the person labelled b.
#
# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
#
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        _dist = {}
        _dist1 = {}
        for v in trust:
            k = v[1]
            vv = v[0]
            if k in _dist:
                _dist[k] = _dist[k] + 1
            else:
                _dist[k] = 1
            if vv in _dist1:
                _dist1[vv] = _dist1[vv] + 1
            else:
                _dist1[vv] = 1

        judge = -1
        for k, v in _dist.items():
            if v == N - 1 and k not in _dist1:
                judge = k
                break
        return judge


if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(2, [[1, 2]]))
