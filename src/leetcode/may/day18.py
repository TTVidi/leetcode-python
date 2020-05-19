# Permutation in String

# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words,
# one of the first string's permutations is the substring of the second string.
#
#
#
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        low_idx = len(s1)
        length = len(s2)
        if length < low_idx:
            return False
        _dict = collections.Counter(s1)
        _set_not = collections.Counter(s2).keys() - _dict.keys()
        pre_idx = 0
        i = 0
        _temp = {}
        while i < length:
            c = s2[i]
            if c in _set_not:
                i += 1
                pre_idx = i
                _temp = {}
                continue
            if c in _temp:
                _temp[c] = _temp[c] + 1
            else:
                _temp[c] = 1

            if i - pre_idx == low_idx - 1:
                if _temp == _dict:
                    return True
                pre = s2[pre_idx]
                if _temp[pre] == 1:
                    _temp.pop(pre)
                else:
                    _temp[pre] = _temp[pre] - 1
                i += 1
                pre_idx += 1
                continue
            else:
                i += 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))
