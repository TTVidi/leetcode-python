# Number of Substrings Containing All Three Characters

# Given a string s consisting only of characters a, b and c.
#
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.
#
#
#
# Example 1:
#
# Input: s = "abcabc" Output: 10 Explanation: The substrings containing at least one occurrence of the characters a,
# b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). Example 2:
#
# Input: s = "aaacb" Output: 3 Explanation: The substrings containing at least one occurrence of the characters a,
# b and c are "aaacb", "aacb" and "acb". Example 3:
#
# Input: s = "abc"
# Output: 1
#
#
# Constraints:
#
# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        ac = 0
        bc = 0
        cc = 0

        while True:
            while (ac == 0 or bc == 0 or cc == 0) and right < len(s):
                if s[right] == "a":
                    ac += 1
                elif s[right] == "b":
                    bc += 1
                else:
                    cc += 1
                right += 1

            if ac > 0 and bc > 0 and cc > 0:
                rest = len(s) - right + 1
                while ac > 0 and bc > 0 and cc > 0:
                    res += rest
                    if s[left] == "a":
                        ac -= 1
                    elif s[left] == "b":
                        bc -= 1
                    else:
                        cc -= 1
                    left += 1
            else:
                break

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSubstrings("abc"))
