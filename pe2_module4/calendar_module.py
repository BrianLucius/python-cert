import calendar

calendar.setfirstweekday(calendar.SUNDAY)

print(calendar.calendar(2020, 3, 1, 6, 3))
print(calendar.month(2022, 1))

print(calendar.weekday(2020, 12, 24))

print(calendar.weekheader(3))

print("Is leap: ",calendar.isleap(2020))
print("Years with leap days: ", calendar.leapdays(2010, 2021))

c = calendar.Calendar(calendar.SUNDAY)
for weekday in c.iterweekdays():
    print(weekday, end=" ")
print('')
    
c2 = calendar.Calendar()
for date in c2.itermonthdates(2019, 11):
    print(date, end=" ")
print('')

print('\nmonthdays: ')
c2 = calendar.Calendar()
for date in c2.itermonthdays(2019, 11):
    print(date, end=" ")
print('')

print('\nmonthdays2: ')
c2 = calendar.Calendar()
for date in c2.itermonthdays2(2019, 11):
    print(date, end=" ")
print('')

print('\nmonthdays3: ')
c2 = calendar.Calendar()
for date in c2.itermonthdays3(2019, 11):
    print(date, end=" ")
print('')

print('\nmonthdays4: ')
c2 = calendar.Calendar()
for date in c2.itermonthdays4(2019, 11):
    print(date, end=" ")
print('')

print('\nmonthdays2calendar: ')
for data in c2.monthdays2calendar(2019, 11):
    print(data)
print('')