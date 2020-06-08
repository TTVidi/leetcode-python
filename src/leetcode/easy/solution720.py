# Longest Word in Dictionary

# Given a list of strings words representing an English Dictionary, find the longest word in words that can be built
# one character at a time by other words in words. If there is more than one possible answer, return the longest word
# with the smallest lexicographical order.
#
# If there is no answer, return the empty string.
#
from collections import defaultdict
from functools import reduce
from itertools import accumulate
from operator import itemgetter, getitem
from typing import List


class Solution:
    def longestWord(self, a: List[str]) -> str:

        def trie():
            return defaultdict(trie)

        root = trie()
        root["#"] = True

        for x in a:
            tail = reduce(getitem, x, root)
            tail["#"] = True

        best = ""

        for x in a:
            path = accumulate(x, getitem, initial=root)
            if all(map(itemgetter("#"), path)):
                best = min(best, x, key=lambda x: (-len(x), x))

        return best


if __name__ == '__main__':
    s = Solution()
    print(s.longestWord1(["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]))
    print("yodn" < "ewqz")
