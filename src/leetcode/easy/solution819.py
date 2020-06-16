# Most Common Word

# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned
# words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not
# case sensitive.  The answer is in lowercase.
#
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = set()
        for u in banned:
            s.add(u)
        word = ""
        ignore = "!?',;."
        mp = {}
        mx = ""
        for v in paragraph:
            if ignore.__contains__(v):
                v = " "
            if v == " ":
                if s.__contains__(word):
                    word = ""
                    continue
                if word == "":
                    continue
                if word in mp:
                    mp[word] += 1
                    if mp[word] > mp[mx]:
                        mx = word
                else:
                    if mx == "":
                        mx = word
                    mp[word] = 1
                word = ""
                continue
            v = v.lower()
            word += v
        if word != "":
            if word in mp:
                mp[word] += 1
                if mp[word] > mp[mx]:
                    mx = word
            else:
                if mx == "":
                    mx = word
                mp[word] = 1

        return mx


if __name__ == '__main__':
    s = Solution()
    print(s.mostCommonWord("a, a, a, a, b,b,b,c, c",
                           ["a"]))
