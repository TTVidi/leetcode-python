# Count Negative Numbers in a Sorted Matrix

# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
#
# Return the number of negative numbers in grid.
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i, row in enumerate(grid):
            if grid[i][0] < 0:
                count += (m - i) * n
                break
            for j, column in enumerate(grid[i]):
                if column < 0:
                    count += (n - j)
                    break
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countNegatives([[4, 3, 2, -1],
                            [3, 2, 1, -1],
                            [1, 1, -1, -2],
                            [-1, -1, -2, -3]
                            ]))
