import calendar

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year: int, weekday: int):
        __weekday_count_in_year = 0
        c = calendar.Calendar()
        for month in range(1, 13):
            for week in c.monthdays2calendar(year, month):
                if week[weekday][0]:
                    __weekday_count_in_year += 1
        return __weekday_count_in_year

mycalendar = MyCalendar()

print(mycalendar.count_weekday_in_year(2019, 0))
print(mycalendar.count_weekday_in_year(2000, 6))
