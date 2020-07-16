# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120 Output: 21 Note: Assume we are dealing with an environment which could only store integers within the
# 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0
# when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        positive = True
        if x < 0:
            positive = False
            x = abs(x)
        m = 2 ** 31 - 1
        s = str(x)
        rs = ""
        length = len(s)
        for i in range(length):
            rs += s[length - 1 - i]
        x = int(rs)
        if x > m:
            return 0
        if positive:
            return x
        return -x


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1534236469))
