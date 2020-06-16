# Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No
# two characters may map to the same character but a character may map to itself.
#


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            dt = {}
            ds = {}
            ss = ""
            st = ""
            for i in range(len(s)):
                sc = s[i]
                tc = t[i]
                if sc in dt:
                    if dt[sc] != tc:
                        return False
                else:
                    dt[sc] = tc

                if tc in ds:
                    if ds[tc] != sc:
                        return False
                else:
                    ds[tc] = sc

                st += tc
                ss += sc
            return st == t and ss == s
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic("egg", "add"))
