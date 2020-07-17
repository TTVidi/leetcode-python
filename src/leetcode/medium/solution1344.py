# Angle Between Hands of a Clock

# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour % 12
        hour *= 5
        hour += (minutes / 12)
        diff = abs(hour - minutes) * 6
        if diff > 180:
            diff = 360 - diff
        return diff


if __name__ == '__main__':
    s = Solution()
    print(s.angleClock(1, 57))
