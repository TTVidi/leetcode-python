# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in
# str.
#
# Example 1:
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# Example 3:
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# Example 4:
#
# Input: pattern = "abba", str = "dog dog dog dog" Output: false Notes: You may assume pattern contains only
# lowercase letters, and str contains lowercase letters that may be separated by a single space.
#

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        sl = str.split(" ")
        if len(sl) == len(pattern):
            dp = {}
            dp2 = {}
            for i in range(len(sl)):
                p = pattern[i]
                s = sl[i]
                if p in dp:
                    if dp[p] != s:
                        return False
                else:
                    dp[p] = s

                if s in dp2:
                    if dp2[s] != p:
                        return False
                else:
                    dp2[s] = p
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern("abba", "dog cat cat fish"))
