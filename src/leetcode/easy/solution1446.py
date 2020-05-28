#  Consecutive Characters

# Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one
# unique character.
#
# Return the power of the string.
#

class Solution:
    def maxPower(self, s: str) -> int:
        pre = s[0]
        m = 1
        c = 1
        for i in range(1, len(s)):
            if s[i] == pre:
                c += 1
                m = max(m, c)
            else:
                c = 1
                pre = s[i]
        return m


if __name__ == '__main__':
    s = Solution()
    print(s.maxPower("acc"))
