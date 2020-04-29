# Play with Chips

# There are some chips, and the i-th chip is at position chips[i].
#
# You can perform any of the two following types of moves any number of times (possibly zero) on any chip:
#
# Move the i-th chip by 2 units to the left or to the right with a cost of 0.
# Move the i-th chip by 1 unit to the left or to the right with a cost of 1.
# There can be two or more chips at the same position initially.
#
# Return the minimum cost needed to move all the chips to the same position (any position).
from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd,even = 0,0
        for i in chips:
            if i%2==0:
                even+=1
            else:
                odd+=1
        if even>=odd:
            return odd
        else:
            return even


if __name__ == '__main__':
    s = Solution()
    print(s.minCostToMoveChips([12, 34, 57]))
