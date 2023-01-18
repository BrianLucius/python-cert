from datetime import date
from datetime import time as dttime
import time

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

timestamp = time.time()
print("Timestamp: ", timestamp)

d = date.fromtimestamp(timestamp)
print("Date: ", d)

d2 = date.fromisoformat('2000-01-01')
print("Date: ", d2)

d3 = date(1991, 2, 3)
print("Date: ", d3)

d4 = d3.replace(year=1992, month=1, day=16)
print("Date: ", d4)

print("Weekday: ", d4.weekday())
print("ISO Weekday: ", d4.isoweekday())

t = dttime(14, 53, 20, 1)

print("Time: ", t)
print("Hour: ", t.hour)
print("Minute: ", t.minute)
print("Seconds: ", t.second)
print("microseconds: ", t.microsecond)