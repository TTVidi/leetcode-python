# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses
# strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid
# parentheses strings.
#
# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S =
# A+B, with A and B nonempty valid parentheses strings.
#
# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are
# primitive valid parentheses strings.
#
# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
#
#
#
# Example 1:
#
# Input: "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:
#
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation:
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:
#
# Input: "()()"
# Output: ""
# Explanation:
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
#

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        rs = ""
        t = ""
        for v in S:
            if not stack:
                stack.append(v)
            else:
                if v == ")":
                    po = stack.pop()
                    if stack:
                        t += v
                        t = po + t
                    else:
                        rs += t
                        t = ""
                else:
                    stack.append(v)
        return rs

    def removeOuterParentheses2(self, S: str) -> str:
        rs = ""
        temp = ""
        left = 0
        right = 0
        for v in S:
            temp += v
            if v == "(":
                left += 1
            else:
                right += 1
                if left == right:
                    left = 0
                    right = 0
                    rs += temp[1:-1]
                    temp = ""
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.removeOuterParentheses2("()()"))
