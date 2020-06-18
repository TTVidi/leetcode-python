# Convert a Number to Hexadecimal

# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase. The hexadecimal string must not contain extra leading 0s. If
# the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the
# hexadecimal string will not be the zero character. The given number is guaranteed to fit within the range of a
# 32-bit signed integer. You must not use any method provided by the library which converts/formats the number to hex
# directly.
#
class Solution:
    def toHex(self, num: int) -> str:
        numb = []
        if num >= 0:
            if num == 0:
                return "0"
            else:
                while (num > 0):
                    numb.append(num % 16)
                    if num < 16:
                        break
                    num = num // 16

                numb2 = numb[::-1]
                numb2 = [hex(x) for x in numb2]
                return "".join([x[2] for x in numb2])
        else:
            number = abs(num)  # 负数的补码，就是其绝对值的反码加1！！！！！！！！！！！！！
            # binary_number = int("{:032b}".format(number))
            flipped_binary_number = bin(~(number) + 1 & 0xFFFFFFFF)
            print(flipped_binary_number)
            num = int(flipped_binary_number[2:], 2)
            while (num > 0):
                numb.append(num % 16)
                if num < 16:
                    break
                num = num // 16
            numb2 = numb[::-1]
            numb2 = [hex(x) for x in numb2]
            return "".join([x[2] for x in numb2])
