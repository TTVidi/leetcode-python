# Repeated DNA Sequences

# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When
# studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
#
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if s:
            li = []
            di = {}
            length = len(s)
            for i in range(length - 9):
                s1 = s[i:i + 10]
                if s1 in di:
                    if di[s1] == 1:
                        li.append(s1)
                    di[s1] = di[s1] + 1
                else:
                    di[s1] = 1

            return li


if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))
