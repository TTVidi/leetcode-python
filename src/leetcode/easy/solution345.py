# Reverse Vowels of a String

# Write a function that takes a string as input and reverse only the vowels of a string.

class Solution:
    def reverseVowels(self, s: str) -> str:
        li = []
        for v in s:
            li.append(v)
        i = 0
        j = len(s) - 1
        ow = "aeiouAEIOU"
        while i < j:
            while i < j and not ow.__contains__(li[i]):
                i += 1
            while i < j and not ow.__contains__(li[j]):
                j -= 1
            if i < j:
                li[i], li[j] = li[j], li[i]
            i += 1
            j -= 1
        return "".join(li)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels("aeiou"))
