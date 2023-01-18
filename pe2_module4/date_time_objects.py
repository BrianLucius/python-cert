from datetime import datetime
from datetime import date
from datetime import time

dt = datetime(2019, 11, 4, 14, 53)
print("Datetime: ", dt)
print("Date: ", dt.date())
print("Time: ", dt.time())

print("Today: ", datetime.today())
print("now: ", datetime.now())
print("utcnow: ", datetime.utcnow())

print("Timestamp: ", dt.timestamp())

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

t = time(14, 53, 20)
print(t.strftime("%H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S"))

print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
