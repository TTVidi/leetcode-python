# Maximum 69 Number
# Given a positive integer num consisting only of digits 6 and 9.
#
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        for i, c in enumerate(s):
            if c == '6':
                return int(s[:i] + '9' + s[i + 1:])
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.maximum69Number(9666))
