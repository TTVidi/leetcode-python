# Reverse bits of a given 32 bits unsigned integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        def convert_to_str(x: int) -> str:
            s = ""
            while x != 1:
                s += str(x % 2)
                x >>= 1
            s += "1"
            diff = 32 - len(s)
            for i in range(diff):
                s += "0"
            return s

        def convert_to_num(x: str) -> int:
            k = 1
            s = 0
            length = len(x)
            for i in range(length):
                if x[length - i - 1] == "1":
                    s += k
                k <<= 1
            return s

        if n == 0:
            return 0
        return convert_to_num(convert_to_str(n))


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(0))
