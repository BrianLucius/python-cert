from datetime import date
from datetime import datetime
from datetime import timedelta

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)


dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 23)

print(dt1 - dt2)

delta = timedelta(weeks=2, days=2, hours=3, minutes=32, seconds=19)
print(delta)