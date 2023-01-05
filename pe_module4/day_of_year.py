def is_year_leap(year):
    if (year < 1582):
        is_leap = False
    elif (year % 4 != 0):
        is_leap = False
    elif (year % 100 != 0):
        is_leap = True
    elif (year % 400 != 0):
        is_leap = False
    else:
        is_leap = True
    return is_leap

def days_in_month(year, month):
    if month == 2 and not is_year_leap(year):
        return 28
    elif month == 2 and is_year_leap(year):
        return 29
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def day_of_year(year, month, day):
    days = day
    for m in range(1, month):
        days += days_in_month(year, m)
    return days

print(day_of_year(2000, 12, 31))
print(day_of_year(2001, 12, 31))
print(day_of_year(2023, 1, 30))
print(day_of_year(2023, 2, 1))