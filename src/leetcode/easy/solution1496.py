# Path Crossing

# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east,
# or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
#
# Return True if the path crosses itself at any point, that is, if at any time you are on a location you've
# previously visited. Return False otherwise.
#

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = set()
        idx = (0, 0)
        s.add(idx)
        for c in path:
            if c == 'N':
                idx = (idx[0] + 1, idx[1])
            if c == 'S':
                idx = (idx[0] - 1, idx[1])
            if c == 'W':
                idx = (idx[0], idx[1] - 1)
            if c == 'E':
                idx = (idx[0], idx[1] + 1)
            if idx in s:
                return True
            s.add(idx)
        return False
