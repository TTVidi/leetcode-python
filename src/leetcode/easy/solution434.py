# Number of Segments in a String

# Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space
# characters.
#
# Please note that the string does not contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5

class Solution:
    def countSegments(self, s: str) -> int:
        i = 0
        pre = ""
        res = 0
        while i < len(s):
            if s[i] == " ":
                if pre:
                    res += 1
                    pre = ""
            else:
                pre = s[i]
            i += 1
        if pre:
            res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countSegments("Of all the gin joints in all the towns in all the world,   "))
    print(s.countSegments("Hello, my name is John"))
