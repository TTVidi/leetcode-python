# Destination City

# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi
# to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
#
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one
# destination city.
#
#
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        _dict = {}
        for path in paths:
            _dict[path[0]] = path[1]

        for v in _dict.values():
            if _dict.get(v):
                continue
            return v



if __name__ == '__main__':
    s = Solution()
    print(s.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
    print(s.destCity([["B", "C"], ["D", "B"], ["C", "A"]]))
    print(s.destCity([["A", "Z"]]))
    print(s.destCity([["XX", "YY"], ["ZZ", "QQ"], ["YY", "CC"],
                      ["CC", "ZZ"], ["QQ", "LL"]]))
