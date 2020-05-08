# Convert Integer to the Sum of Two No-Zero Integers

# Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.
#
# Return a list of two integers [A, B] where:
#
# A and B are No-Zero integers. A + B = n It's guarateed that there is at least one valid solution. If there are many
# valid solutions you can return any of them.
#
from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def not_contain_zero(num: int) -> bool:
            return str(num).count('0') == 0

        for i in range((n >> 1) + 1):
            if not_contain_zero(i) and not_contain_zero(n - i):
                return [i, n - i]
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.getNoZeroIntegers(2))
