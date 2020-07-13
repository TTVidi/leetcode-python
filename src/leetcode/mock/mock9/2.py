# There are 8 prison cells in a row, and each cell is either occupied or vacant.
#
# Each day, whether the cell is occupied or vacant changes according to the following rules:
#
# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
#
# We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied,
# else cells[i] == 0.
#
# Given the initial state of the prison, return the state of the prison after N days (and N such changes described
# above.)
#
#
#
# Example 1:
#
# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation:
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
#
# Example 2:
#
# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]
#
#
# Note:
#
# cells.length == 8
# cells[i] is in {0, 1}
# 1 <= N <= 10^9
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        return []

    def prisonAfterNDays1(self, cells: List[int], N: int) -> List[int]:
        dp = {}
        dp2 = {}
        mod = N
        for i in range(1, N + 1):
            temp = []
            sb = ""
            for j in range(8):
                k = 0
                if 0 < j < 7:
                    k = 1 - (cells[j - 1] ^ cells[j + 1])
                temp.append(k)
                sb += str(k)
            cells = temp
            if sb in dp:
                mod = i - 1
                break
            else:
                dp[sb] = i
                dp2[i] = cells
        if mod == N:
            return dp2[mod]
        else:
            r = N % mod
            if r == 0:
                return dp2[mod]
            return dp2[r]


if __name__ == '__main__':
    s = Solution()
    print(s.prisonAfterNDays1([1, 0, 0, 1, 0, 0, 1, 0],
                              16))
