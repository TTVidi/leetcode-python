# Repeated Substring Pattern Given a non-empty string check if it can be constructed by taking a substring of it and
# appending multiple copies of the substring together. You may assume the given string consists of lowercase English
# letters only and its length will not exceed 10000.
#
#
#
# Example 1:
#
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# Example 2:
#
# Input: "aba"
# Output: False
# Example 3:
#
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        i = 0
        t = ""
        while i < (l >> 1):
            t += s[i]
            if l % (i + 1) == 0:
                if s == t * (l // (i + 1)):
                    return True
            i += 1
        return False
