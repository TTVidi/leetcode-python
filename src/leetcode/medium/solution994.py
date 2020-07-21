# Rotting Oranges

# In a given grid, each cell can have one of three values:
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible,
# return -1 instead.
#
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        l1 = len(grid)
        l2 = len(grid[0])

        def rotting(i: int, j: int, day: int):
            if 0 <= i < l1 and 0 <= j < l2:
                k = day + 2
                if grid[i][j] == 0:
                    return
                elif grid[i][j] == 1:
                    grid[i][j] = k
                    rotting(i - 1, j, day + 1)
                    rotting(i + 1, j, day + 1)
                    rotting(i, j - 1, day + 1)
                    rotting(i, j + 1, day + 1)
                elif grid[i][j] == 2:
                    return
                else:
                    if k < grid[i][j]:
                        grid[i][j] = k
                        rotting(i - 1, j, day + 1)
                        rotting(i + 1, j, day + 1)
                        rotting(i, j - 1, day + 1)
                        rotting(i, j + 1, day + 1)

        has_rot = False
        for i, v in enumerate(grid):
            for j, k in enumerate(v):
                if k == 2:
                    has_rot = True
                    rotting(i - 1, j, 1)
                    rotting(i + 1, j, 1)
                    rotting(i, j - 1, 1)
                    rotting(i, j + 1, 1)
        if has_rot:
            m = -1
            for i, v in enumerate(grid):
                for j, k in enumerate(v):
                    if k > 0:
                        if k == 1:
                            return -1
                        else:
                            m = max(m, k - 2)
            return m

        mx = 0
        for i, v in enumerate(grid):
            for j, k in enumerate(v):
                mx += k
        if mx == 0:
            return 0
        return -1


if __name__ == '__main__':
    s = Solution()
    # print(s.orangesRotting([[0, 1], [2, 0]]))
    # print(s.orangesRotting([[2, 1, 1, 2]]))
    print(s.orangesRotting([[2, 1, 1, 1], [0, 1, 0, 2], [0, 1, 2, 1], [1, 2, 0, 1], [1, 2, 1, 1], [1, 2, 1, 1]]))
