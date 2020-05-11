# Reformat The String

# Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
#
# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed
# by another digit. That is, no two adjacent characters have the same type.
#
# Return the reformatted string or return an empty string if it is impossible to reformat the string.
#
#

class Solution:
    def reformat(self, s: str) -> str:
        _n_list = []
        _s_list = []
        for c in s:
            if 'a' <= c <= 'z':
                _s_list.append(c)
            else:
                _n_list.append(c)
        l_n = len(_n_list)
        l_s = len(_s_list)
        i = 0
        if l_n == l_s:
            s = ""
            while i < l_n:
                s += (_n_list[i] + _s_list[i])
                i += 1
            return s
        if l_n - l_s == 1:
            s = ""
            while i < l_s:
                s += (_n_list[i] + _s_list[i])
                i += 1
            return s + _n_list[i]
        if l_s - l_n == 1:
            s = ""
            while i < l_n:
                s += (_s_list[i] + _n_list[i])
                i += 1
            return s + _s_list[i]
        return ""


if __name__ == '__main__':
    s = Solution()
    print(s.reformat("covid2019"))
