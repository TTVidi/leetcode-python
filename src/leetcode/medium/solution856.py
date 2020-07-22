# Score of Parentheses

# Given a balanced parentheses string S, compute the score of the string based on the following rule:
#
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
#
#
# Example 1:
#
# Input: "()"
# Output: 1
# Example 2:
#
# Input: "(())"
# Output: 2
# Example 3:
#
# Input: "()()"
# Output: 2
# Example 4:
#
# Input: "(()(()))"
# Output: 6
from typing import List


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        def split(sub: str) -> List[str]:
            res = []
            l = 0
            r = 0
            temp = ""
            for v in sub:
                temp += v
                if v == "(":
                    l += 1
                else:
                    r += 1
                    if l == r:
                        l = 0
                        r = 0
                        res.append(temp)
                        temp = ""
            return res

        def is_recursive(sub: str) -> bool:
            if sub[0] == sub[1] == "(":
                return True
            return False

        def score(sub: str) -> int:
            if sub == "()":
                return 1
            sp = split(sub)
            total = 0
            for v in sp:
                if is_recursive(v):
                    v = v[1:-1]
                    total += (score(v) << 1)
                else:
                    total += score(v)
            return total

        return score(S)


if __name__ == '__main__':
    s = Solution()
    print(s.scoreOfParentheses("(()(()))"))
