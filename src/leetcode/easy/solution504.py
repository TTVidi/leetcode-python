# Base 7

# Given an integer, return its base 7 string representation.


class Solution:
    def convertToBase7(self, num: int) -> str:
        base = ""
        if num < 0:
            num *= -1
            base = "-"
        stack = []
        while num >= 7:
            stack.append(num % 7)
            num //= 7
        stack.append(num)
        while stack:
            base += str(stack.pop(-1))
        return base


if __name__ == '__main__':
    s = Solution()
    print(s.convertToBase7(100))
