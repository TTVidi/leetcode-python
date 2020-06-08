# Power of Two


# Given an integer, write a function to determine if it is a power of two.
#

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pw = 1
        while pw <= n:
            if pw == n:
                return True
            pw <<= 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(4))
