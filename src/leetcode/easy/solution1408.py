# String Matching in an Array

# Given an array of string words. Return all strings in words which is substring of another word in any order.
#
# String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of
# words[j].
#
#
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        t = str(words)
        _li = []
        for word in words:
            if t.count(word) > 1:
                _li.append(word)
        return _li


if __name__ == '__main__':
    s = Solution()
    print(s.stringMatching(["mass", "as", "hero", "superhero"]))
