# Number of 1 Bits

# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming
# weight).
#

class Solution:
    def hammingWeight(self, n: int) -> int:
        sm = 0
        while n:
            sm += (n & 1)
            n >>= 1
        return sm


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(1011))
