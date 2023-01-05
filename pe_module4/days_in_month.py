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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    result = days_in_month(yr, mo)
    print(yr, mo, "->", result, "days", end=" ")
    if result == test_results[i]:
        print("Ok")
    else:
        print("Failed")