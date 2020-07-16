# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from
# the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k
# but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example: Input: s = "abcdefg", k = 2 Output: "bacdfeg" Restrictions: The string consists of lower English letters
# only. Length of the given string and k will in the range [1, 10000]
#
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        k_count = 1
        temp = ""
        rs = ""

        def reverse(st: str) -> str:
            tp = ""
            for i in range(len(st)):
                tp += st[len(st) - i - 1]
            return tp

        for i in range(len(s)):
            rs += s[i]
            if len(rs) == k:
                if k_count % 2 == 1:
                    temp += reverse(rs)
                else:
                    temp += rs
                rs = ""
                k_count += 1
        if rs != "":
            if k_count % 2 == 1:
                temp += reverse(rs)
            else:
                temp += rs
        return temp


if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("a", 2))
