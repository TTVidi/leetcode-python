# Minimum Path Sum Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right
# which minimizes the sum of all numbers along its path.
from typing import List
import sys


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        remember = {'0,0': grid[0][0]}

        def min_path(x: int, y: int) -> int:
            idx = ",".join([str(x), str(y)])
            if idx in remember:
                return remember[idx]
            left = y - 1
            top = x - 1
            left_min = sys.maxsize
            top_min = sys.maxsize
            if left >= 0:
                left_min = min_path(x, left)
            if top >= 0:
                top_min = min_path(top, y)
            mi = min(top_min, left_min) + grid[x][y]
            remember[idx] = mi
            return mi

        return min_path(len(grid) - 1, len(grid[0]) - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
