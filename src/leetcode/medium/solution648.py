#  Replace Words

# 648. Replace Words
# Medium
#
# 745
#
# 131
#
# Add to List
#
# Share In English, we have a concept called root, which can be followed by some other words to form another longer
# word - let's call this word successor. For example, the root an, followed by other, which can form another word
# another.
#
# Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the
# sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the
# shortest length.
#
# You need to output the sentence after the replacement.
#
#
#
# Example 1:
#
# Input: dict = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
#
#
# Constraints:
#
# The input will only have lower-case letters.
# 1 <= dict.length <= 1000
# 1 <= dict[i].length <= 100
# 1 <= sentence words number <= 1000
# 1 <= sentence words length <= 1000
from typing import List


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        dp = set()
        for d in dict:
            dp.add(d)

        def find(s: str) -> str:
            res = ""
            for i in range(len(s)):
                temp = s[:i + 1]
                if temp in dp:
                    return temp
            return res

        res = ""
        word = ""

        for i in range(len(sentence)):
            if sentence[i] == " ":
                r = find(word)
                if r:
                    res += r
                else:
                    res += word
                res += " "
                word = ""
            else:
                word += sentence[i]

        if word:
            r = find(word)
            if r:
                res += r
            else:
                res += word

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
