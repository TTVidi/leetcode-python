# Minimum Add to Make Parentheses Valid

# Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any
# positions ) so that the resulting parentheses string is valid.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
#
#
#
# Example 1:
#
# Input: "())"
# Output: 1
# Example 2:
#
# Input: "((("
# Output: 3
# Example 3:
#
# Input: "()"
# Output: 0
# Example 4:
#
# Input: "()))(("
# Output: 4
#
#
# Note:
#
# S.length <= 1000
# S only consists of '(' and ')' characters.

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        l = 0
        r = 0
        res = 0
        for v in S:
            if v == "(":
                if r > 0:
                    if l > r:
                        r = 0
                        l -= r
                    else:
                        r -= l
                        l = 0
                res += r
                r = 0
                l += 1
            else:
                r += 1
        res += abs(l - r)
        return res

    def minAddToMakeValid2(self, S: str) -> int:
        res = 0
        stack = []
        for v in S:
            if v == "(":
                stack.append(v)
            else:
                if stack:
                    stack.pop()
                else:
                    res += 1
        res += len(stack)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid2("()))(("))
