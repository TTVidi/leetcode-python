# Valid Parenthesis String Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
class Solution:
    def checkValidString(self, s: str) -> bool:
        r = []
        stack = []
        for i, c in enumerate(s):
            if c == '*':
                r.append(i)
            elif c == '(':
                stack.append(i)
            else:
                if not stack:
                    if not r:
                        return False
                    r.pop(-1)
                else:
                    stack.pop(-1)

        while stack:
            if r:
                idx = r.pop(-1)
                left = stack.pop(-1)
                if idx > left:
                    continue
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkValidString("((*)(*()(())())())()()((()())((()))(*"))
