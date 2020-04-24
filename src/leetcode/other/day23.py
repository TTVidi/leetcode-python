# Bitwise AND of Numbers Range

# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        if m == n:
            return m
        base = 1
        while base <= m:
            base *= 2
        base = base >> 1
        if n >= (base << 1):
            return 0
        sum = 0
        while base >= 1:
            if m == base:
                sum += base
                break
            if m > base:
                m -= base
                n -= base
                sum += base
            else:
                if n >= base:
                    break
            base >>= 1
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.rangeBitwiseAnd(125, 127))
