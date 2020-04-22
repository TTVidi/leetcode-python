#  Decrypt String from Alphabet to Integer Mapping
# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
#
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
#
# It's guaranteed that a unique mapping will always exist.
#

class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        result = []
        while i >= 0:
            current = s[i]
            if s[i] == '#':
                current = s[i - 2] + s[i - 1]
                i -= 3
            else:
                i -= 1
            result.insert(0, chr(int(current) + 96))
        return "".join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.freqAlphabets("10#11#12"))
