# Longest Duplicate Substring

# Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (
# The occurrences may overlap.)
#
# Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring,
# the answer is "".)
#

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def count(sub: str) -> int:
            r = 0
            for i in range(len(S)):
                print(1)

        return ""


if __name__ == '__main__':
    s = Solution()
    s.longestDupSubstring("banana")
