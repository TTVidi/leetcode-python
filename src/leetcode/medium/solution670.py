# Maximum Swap

# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the
# maximum valued number you could get.
#

class Solution:
    def maximumSwap(self, num: int) -> int:
        li = [-1 for i in range(10)]
        s = list(str(num))
        l = len(s)
        i = l - 1
        while i >= 0:
            idx = ord(s[i]) - 48
            if li[idx] == -1:
                li[idx] = i
            i -= 1

        def find_idx(char: str, current_idx: int) -> int:
            n = ord(char) - 48
            j = 9
            while j > n:
                if li[j] != -1 and li[j] > current_idx:
                    return li[j]
                j -= 1
            return -1

        for i in range(l):
            idx = find_idx(s[i], i)
            if idx != -1:
                s[i], s[idx] = s[idx], s[i]
                break
        return int("".join(s))


if __name__ == '__main__':
    s = Solution()
    print(s.maximumSwap(9973))
