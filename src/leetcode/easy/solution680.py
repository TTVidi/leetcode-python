# Valid Palindrome II

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                return  s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
            l += 1
            r -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.validPalindrome("abca"))
