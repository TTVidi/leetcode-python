# Maximum Number of Balloons

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as
# possible.
#
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
#


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b_count = 0
        a_count = 0
        l_count = 0
        o_count = 0
        n_count = 0
        for s in text:
            if s == 'a':
                a_count += 1
            elif s == 'b':
                b_count += 1
            elif s == 'l':
                l_count += 1
            elif s == 'n':
                n_count += 1
            elif s == 'o':
                o_count += 1
        return min([b_count, a_count, n_count, l_count >> 1, o_count >> 1])

    def maxNumberOfBalloons2(self, text: str) -> int:
        return min([text.count('a'), text.count('b'), text.count('n'), text.count('l') >> 1, text.count('o') >> 1])


if __name__ == '__main__':
    s = Solution()
    print(s.maxNumberOfBalloons("123123"))
