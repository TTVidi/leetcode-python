# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is
# different from X.  Each digit must be rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to
# each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9
# rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:
#
# N  will be in range [1, 10000].

class Solution:
    def rotatedDigits(self, N: int) -> int:
        def is_valid(number: int) -> bool:
            s = str(number)
            temp = ""
            for c in s:
                if c in ('0', '1', '8'):
                    temp += c
                elif c == '2':
                    temp += '5'
                elif c == '5':
                    temp += '2'
                elif c == '6':
                    temp += '9'
                elif c == '9':
                    temp += '6'
                else:
                    return False
            return temp != s

        su = 0
        for i in range(1, N + 1):
            if is_valid(i):
                su += 1

        return su


if __name__ == '__main__':
    s = Solution()
    print(s.rotatedDigits(10))
