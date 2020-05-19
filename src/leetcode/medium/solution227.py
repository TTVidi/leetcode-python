# Basic Calculator II

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer
# division should truncate toward zero.
#

class Solution:
    def calculate(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        res, num = 0, 0
        sign = '+'
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and s[i] != " ") or i == len(s) - 1:
                if sign == '-':
                    stack.append(-num)
                if sign == '+':
                    stack.append(num)
                if sign == '*':
                    product = stack.pop() * num
                    stack.append(product)
                if sign == '/':
                    quotient = stack.pop() / num
                    stack.append(int(quotient))
                sign = s[i]
                num = 0

        while stack:
            res += stack.pop()
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.calculate("1-1+1"))
