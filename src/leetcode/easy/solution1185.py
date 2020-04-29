# Day of the Week

# Given a date, return the corresponding day of the week for that date.
#
# The input is given as three integers representing the day, month and year respectively.
#
# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
# "Saturday"}.
#
#

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import calendar
        days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
        week_day = calendar.weekday(year, month, day)
        for key, value in days.items():
            if week_day == value:
                return key


if __name__ == '__main__':
    s = Solution()
    print(s.dayOfTheWeek(1, 2, 3))
