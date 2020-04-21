# Number of Islands Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is
# surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four
# edges of the grid are all surrounded by water.
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for x, g in enumerate(grid):
            for y, v in enumerate(g):
                if grid[x][y] == '1':
                    count += 1
                    self.draw(grid, x, y)
        return count

    def draw(self, grid: List[List[str]], x: int, y: int) -> None:
        y_max = len(grid[x])
        y_min = 0
        x_max = len(grid)
        x_min = 0
        grid[x][y] = '-1'
        # draw left
        if y - 1 >= y_min and grid[x][y - 1] == '1':
            self.draw(grid, x, y - 1)
        # draw right
        if y + 1 < y_max and grid[x][y + 1] == '1':
            self.draw(grid, x, y + 1)
        # draw top
        if x - 1 >= x_min and grid[x - 1][y] == '1':
            self.draw(grid, x - 1, y)
        # draw bottom
        if x + 1 < x_max and grid[x + 1][y] == '1':
            self.draw(grid, x + 1, y)


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
