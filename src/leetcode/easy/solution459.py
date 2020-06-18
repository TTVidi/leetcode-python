# Repeated Substring Pattern

# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies
# of the substring together. You may assume the given string consists of lowercase English letters only and its
# length will not exceed 10000.
#
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        if length > 1:
            i = 0
            j = length - 1
            s1 = ""
            s2 = ""
            repeats = []
            while i < j:
                s1 += s[i]
                s2 = s[j] + s2
                if s1 == s2:
                    repeats.append(s1)
                i += 1
                j -= 1
            if repeats:
                for repeat in repeats:
                    if length % len(repeat) == 0:
                        times = length // len(repeat)
                        if repeat * times == s:
                            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern("ababababab"))
