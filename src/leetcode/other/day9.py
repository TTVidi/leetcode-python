# Backspace String Compare Given two strings S and T, return if they are equal when both are typed into empty text
# editors. # means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        stack2 = []
        for c in S:
            if c == '#':
                if stack1 != []:
                    stack1.pop(-1)
            else:
                stack1.append(c)

        for c in T:
            if c == '#':
                if stack2 != []:
                    stack2.pop(-1)
            else:
                stack2.append(c)
        return stack1 == stack2

    def backspaceCompare2(self, S: str, T: str) -> bool:
        i = len(S) - 1
        j = len(T) - 1

        serial_s = 0
        serial_t = 0

        current_s = ''
        current_t = ''
        while True:
            if i >= 0:
                if S[i] == '#':
                    serial_s += 1
                    current_s = ''
                else:
                    if serial_s > 0:
                        serial_s -= 1
                    else:
                        current_s = S[i]

            if j >= 0:
                if T[j] == '#':
                    serial_t += 1
                    current_t = ''
                else:
                    if serial_t > 0:
                        serial_t -= 1
                    else:
                        current_t = T[j]
            if current_t == current_s:
                i -= 1
                j -= 1
            elif current_t == '':
                j -= 1
            elif current_s == '':
                i -= 1
            else:
                return False
            if i < 0 and j < 0:
                break
        if current_s == current_t:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.backspaceCompare2("bxj##tw",
                              "bxj###tw"))
