# First Unique Character in a String

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = collections.Counter(list(s))
        for i, v in enumerate(s):
            if m[v] == 1:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("1123"))
