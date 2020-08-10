# Longest Valid Parentheses

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
# parentheses substring.
#
# Example 1:
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = []
        valid = 0
        for c in s:
            if c == "(":
                stack.append(c)
            if c == ")":
                if stack:
                    stack.pop()
                    valid += 2
                    res = max(res, valid)
                else:
                    valid = 0

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses("(()"))
    print(s.longestValidParentheses(")()())"))
    print(s.longestValidParentheses("((((())))"))
    print(s.longestValidParentheses("(())"))
    print(s.longestValidParentheses("(()))"))
    print(s.longestValidParentheses("((()())"))
    print(s.longestValidParentheses("(((()))"))
    print(s.longestValidParentheses("((((()"))
    print(s.longestValidParentheses("()(()"))
