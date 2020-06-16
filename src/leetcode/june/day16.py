# Validate IP Address

# Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.
#
# IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers,
# each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;
#
# Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.
#
# IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The
# groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid
# one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the
# address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and
# using upper cases).
#
# However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons
# (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.
#
# Besides, extra leading zeros in the IPv6 is also invalid. For example, the address
# 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.
#
# Note: You may assume there is no extra space or special characters in the input string.
#
from string import hexdigits


class Solution:
    def validIPAddress(self, IP: str) -> str:

        # check whether is a iPV4
        def is_ip_v4() -> bool:
            arr = IP.split(".")
            if len(arr) == 4:
                for v in arr:
                    if not v.isdigit():
                        return False
                    int_v = int(v)
                    str_v = str(int_v)
                    if len(str_v) == len(v):
                        if 0 <= int_v <= 255:
                            continue
                    return False
                return True
            return False

        # check whether is a iPV4
        def is_ip_v6() -> bool:
            res = 0
            ipv6 = IP.split(':')
            if len(ipv6) == 8:
                for x in ipv6:
                    if x == '' or len(x) > 4 or not all(c in hexdigits for c in x):
                        res = 1
                        break
                if not res:
                    return True
            return False

        if is_ip_v4():
            return "IPv4"

        if is_ip_v6():
            return "IPv6"
        return "Neither"


if __name__ == '__main__':
    s = Solution()
    print(s.validIPAddress("1e1.4.5.6"))

