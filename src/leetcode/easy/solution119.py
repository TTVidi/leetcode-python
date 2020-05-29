# Pascal's Triangle II

# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        base = [1, 1]
        if rowIndex == 1:
            return [1, 1]
        for i in range(1, rowIndex + 1):
            temp = []
            temp.append(1)
            for k in range(1, i):
                temp.append(base[k - 1] + base[k])
            temp.append(1)
            base = temp
        return base


if __name__ == '__main__':
    s = Solution()
    print(s.getRow2(3))
