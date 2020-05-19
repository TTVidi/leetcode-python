# Find All Anagrams in a String

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than
# 20,100.
#
# The order of output does not matter.
#
import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        low_idx = len(p)
        length = len(s)
        if length < low_idx:
            return []
        _dict = collections.Counter(p)
        _set_not = collections.Counter(s).keys() - _dict.keys()
        li = []
        pre_idx = 0
        i = 0
        _temp = {}
        while i < length:
            c = s[i]
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
                    li.append(pre_idx)
                pre = s[pre_idx]
                if _temp[pre] == 1:
                    _temp.pop(pre)
                else:
                    _temp[pre] = _temp[pre] - 1
                i += 1
                pre_idx += 1
                continue
            else:
                i += 1
        return li


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("abab", "ab"))
