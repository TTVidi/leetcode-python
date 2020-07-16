# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        borrow = 0
        i = len(a) - 1
        j = len(b) - 1
        rs = ""
        while i >= 0 and j >= 0:
            k = int(a[i]) + int(b[j]) + borrow
            if k >= 2:
                borrow = 1
                rs = str(k - 2) + rs
            else:
                borrow = 0
                rs = str(k) + rs
            i -= 1
            j -= 1

        while i >= 0:
            k = int(a[i]) + borrow
            if k >= 2:
                borrow = 1
                rs = str(k - 2) + rs
            else:
                borrow = 0
                rs = str(k) + rs
            i -= 1

        while j >= 0:
            k = int(b[j]) + borrow
            if k >= 2:
                borrow = 1
                rs = str(k - 2) + rs
            else:
                borrow = 0
                rs = str(k) + rs
            j -= 1
        if borrow == 1:
            rs = "1" + rs

        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("1010", "1011"))
