# Find N Unique Integers Sum up to Zero

# Given an integer n, return any array containing n unique integers such that they add up to 0.
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        if n % 2 == 1:
            arr.append(0)
            n -= 1
        current = 1
        while n > 0:
            arr.append(current)
            arr.append(-current)
            current += 1
            n -= 2
        return arr


if __name__ == '__main__':
    s = Solution()
    print(s.sumZero(5))
