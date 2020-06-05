# Reverse String

# Write a function that reverses a string. The input string is given as an array of characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
# extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        k = l - 1
        k >>= 1
        for i in range(k + 1):
            s[i], s[l - i - 1] = s[l - i - 1], s[i]

    def reverseString1(self, s: List[str]) -> None:
        s.reverse()
