# Knight Dialer

# A chess knight can move as indicated in the chess diagram below:
#
#  .
#
#
#
# This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1
# hops.  Each hop must be from one key to another numbered key.
#
# Each time it lands on a key (including the initial placement of the knight), it presses the number of that key,
# pressing N digits total.
#
# How many distinct numbers can you dial in this manner?
#
# Since the answer may be large, output the answer modulo 10^9 + 7.
#
class Solution:
    def knightDialer(self, N: int) -> int:
        if N == 1:
            return 10
        dp = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        s = 0
        for i in range(N - 1):
            temp = {}
            s = 0
            for k, v in dp.items():
                base = 2
                if k == 4 or k == 6:
                    base = 3
                times = base * v
                s += times
                if k in temp:
                    temp[k] += times
                else:
                    temp[k] = times
            dp = temp
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.knightDialer(4))
