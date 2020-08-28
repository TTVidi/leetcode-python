# Power of Four

# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example 1:
#
# Input: 16
# Output: true
# Example 2:
#
# Input: 5
# Output: false
# Follow up: Could you solve it without loops/recursion?
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        if num >= 4:
            while num != 1:
                if num % 4 == 0:
                    num >>= 2
                else:
                    return False
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(16))
