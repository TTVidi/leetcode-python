# Counting Bits

# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's
# in their binary representation and return them as an array.
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        li = []
        base = 1
        for i in range(num + 1):
            if i == 0:
                li.append(0)
            elif i == 1:
                li.append(1)
            else:
                if base * 2 == i:
                    base = base << 1
                    li.append(1)
                else:
                    rest = i - base
                    li.append(li[rest] + 1)
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(32))
