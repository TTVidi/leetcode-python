# Valid Parenthesis String Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
import random


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
    so = Solution()
    # print(s.checkValidString("((*)(*()(())())())()()((()())((()))(*"))
    case = "C://Users//tangtao02//Desktop//算法/1/case.txt"
    result = "C://Users//tangtao02//Desktop//算法/1/result.txt"
    c = open(case, 'w+')
    r = open(result, 'w+')

    cr = []
    rr = []

    for i in range(100):
        j = random.randint(1, 100)
        s = ""
        for k in range(j):
            f = random.randint(1, 3)
            if f == 1:
                s += "("
            elif f == 2:
                s += ")"
            else:
                s += "*"
        cr.append(s+"\n")
        rr.append(str(so.checkValidString(s))+"\n")

    c.writelines(cr)
    r.writelines(rr)
    c.close()
    r.close()
