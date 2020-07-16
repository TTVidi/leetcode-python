# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.
#
#
#
# Example 1:
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation:
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:
#
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation:
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
#
#
# Note:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# All strings contain lowercase English letters only.
import collections
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = collections.Counter(chars)
        length = 0
        for word in words:
            sub = collections.Counter(word)
            l = 0
            for k, v in sub.items():
                if k in count:
                    if count[k] >= v:
                        l += v
                        continue
                l = 0
                break
            length += l
        return length


if __name__ == '__main__':
    s = Solution()
    print(s.countCharacters(["hello","world","leetcode"], "welldonehoneyr"))
