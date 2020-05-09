# Check If It Is a Straight Line
#
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        l = len(coordinates)
        if l <= 2:
            return True
        x_dist = coordinates[0][0] - coordinates[1][0]
        y_dist = coordinates[0][1] - coordinates[1][1]
        i = 2
        if x_dist == 0:
            while i < l:
                if coordinates[i][0] != coordinates[0][0]:
                    return False
                i += 1
            return True
        if y_dist == 0:
            while i < l:
                if coordinates[i][1] != coordinates[0][1]:
                    return False
                i += 1
            return True
        k = y_dist / x_dist
        while i < l:
            ki = (coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0])
            if ki != k:
                return False
            i += 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
