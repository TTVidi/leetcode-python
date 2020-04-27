# Longest Common Subsequence

# Given two strings text1 and text2, return the length of their longest common subsequence.
#
# A subsequence of a string is a new string generated from the original string with some characters(can be none)
# deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde"
# while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
#
#
#
# If there is no common subsequence, return 0.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        _dict = {}
        for i, v in enumerate(text1):
            if v not in _dict:
                _dict[v] = [i]
            else:
                _dict[v].append(i)
        _len = len(text1)
        pre_idx = -1
        contain = 0
        for i, v in enumerate(text2):
            if v in _dict:
                for k, idx in enumerate(_dict[v]):
                    if idx > pre_idx:
                        contain += 1
                        pre_idx = idx
                        for l in range(k + 1):
                            _dict[v].pop(l)
                        break

        return contain


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence("abc", "aceftbc"))
