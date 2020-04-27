# Palindromic Substrings

# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of
# same characters.
#

class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count = 0
        dp = [[0  for _ in range(length)] for _ in range(length)]
        for L in range(1,length+1):
            for i in range(0,length-L+1):
                j = i+L-1
                if i == j:
                    dp[i][j] = 1
                    count+=1
                elif s[i] == s[j]:
                    temp_i = i
                    temp_j =j
                    if abs(temp_i - temp_j) == 1:
                        dp[i][j] = 1
                        count+=1
                    else:
                        if dp[i+1][j-1] == 1:
                            dp[i][j] = 1
                            count+=1

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings("abccba"))
