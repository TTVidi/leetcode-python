# Is Subsequence

# Given a string s and a string t, check if s is subsequence of t.
#
# You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length
# ~= 500,000) string, and s is a short string (<=100).
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a
# subsequence of "abcde" while "aec" is not).
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1 = 0
        l2 = 0
        while l1 < len(s) and l2 < len(t):
            if s[l1] == t[l2]:
                l1 += 1
            l2 += 1
        return l1 == len(s)


if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence("abcc", "abbdcec"))
