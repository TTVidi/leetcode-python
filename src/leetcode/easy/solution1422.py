# Maximum Score After Splitting a String

# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty
# substrings (i.e. left substring and right substring).
#
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the
# right substring.
#
#
#

class Solution:
    def maxScore(self, s: str) -> int:
        total = len(s)
        zero_ = 0
        for c in s:
            if c == "0":
                zero_ += 1

        one_ = total - zero_
        if one_ == 0 or zero_ == 0:
            return total - 1

        m = 0
        c_zero = 0
        for i, v in enumerate(s):
            if i == total - 1:
                break
            if v == "0":
                c_zero += 1
            m = max(m, (c_zero << 1) + one_ - i - 1)

        return m


if __name__ == '__main__':
    s = Solution()
    print(s.maxScore("11100"))
