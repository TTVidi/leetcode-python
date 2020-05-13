# Remove K Digits

# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is
# the smallest possible.
#
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
#

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        l = len(num)
        if k >= l:
            return "0"

        def format_(n: str) -> str:
            i = 0
            while i < len(n):
                if n[i] == '0':
                    i += 1
                else:
                    break
            return n[i:]

        while num != "0" and k > 0:
            idx = 1
            while idx < len(num):
                if num[idx] >= num[idx - 1]:
                    idx += 1
                else:
                    break
            num = format_(num[:idx - 1] + num[idx:])
            k -= 1
        rs = format_(num)
        if rs == "":
            return "0"
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.removeKdigits("10", 2))
