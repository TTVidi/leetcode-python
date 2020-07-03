# Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        if s:
            _set = set()
            i = 0
            j = i + 1
            length = len(s)
            _set.add(s[0])
            while i < length and j < length:
                if s[j] in _set:
                    mx = max(mx, j - i)
                    while i < j:
                        _set.remove(s[i])
                        i += 1
                        if s[i-1] == s[j]:
                            break
                _set.add(s[j])
                j += 1
            mx = max(mx, j - i)
        return mx


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcdefg"))
