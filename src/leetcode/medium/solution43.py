# Multiply Strings

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
# also represented as a string.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
# Accepted


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        if l1 > l2:
            num1, num2 = num2, num1
            l1, l2 = l2, l1
        rs = ""
        for i in range(l1):
            ki = int(num1[l1 - 1 - i])
            t = ""
            bo = 0
            for j in range(l2):
                kj = int(num2[l2 - 1 - j])
                cu = ki * kj + bo
                bo = cu // 10
                cu %= 10
                t = str(cu) + t
            if bo > 0:
                t = str(bo) + t
                bo = 0

            if rs:
                t += ("0" * i)
                tp = ""
                lt = len(t)
                lr = len(rs)
                k = 0
                while k < lt and k < lr:
                    cu = int(t[lt - 1 - k]) + int(rs[lr - 1 - k]) + bo
                    bo = cu // 10
                    cu %= 10
                    tp = str(cu) + tp
                    k += 1

                while k < lt:
                    cu = int(t[lt - 1 - k]) + bo
                    bo = cu // 10
                    cu %= 10
                    tp = str(cu) + tp
                    k += 1

                while k < lr:
                    cu = int(rs[lr - 1 - k]) + bo
                    bo = cu // 10
                    cu %= 10
                    tp = str(cu) + tp
                    k += 1

                if bo > 0:
                    tp = str(bo) + tp
                rs = tp
            else:
                rs = t
        if rs:
            i = 0
            while i < len(rs) and rs[i] == "0":
                i += 1
            if i == len(rs):
                return "0"
            else:
                return rs[i:]
        return "0"


if __name__ == '__main__':
    s = Solution()
    print(s.multiply("9133",
                     "2"))
