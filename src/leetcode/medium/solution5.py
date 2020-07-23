# Longest Palindromic Substring

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"
#

class Solution:
    def longestPalindrome1(self, s: str) -> str:
        n = len(s)

        def getLen(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        start = 0
        longest = 0
        for i in range(n):
            curr_len = max(getLen(i, i), getLen(i, i + 1))  # odd, even case
            if curr_len < longest:
                continue

            longest = curr_len
            start = i - (curr_len - 1) // 2  # consider even case

        return s[start:start + longest]

    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(begin: int, end: int) -> bool:
            while begin <= end:
                if s[begin] != s[end]:
                    return False
                begin += 1
                end -= 1
            return True

        length = len(s)
        l = 0
        start = 0
        i = 0
        while i < length - l:
            j = i + l + 1
            while j < length:
                if is_palindrome(i, j):
                    start = i
                    l = j - i
                j += 1
            i += 1
        return s[start:start + l + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
