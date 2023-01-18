import time

timestamp = 1572879180
print(time.ctime(timestamp))
print(time.ctime())
print(time.gmtime())
print(time.localtime())

st = time.gmtime(timestamp)
print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0 ,0, 308, 0)))

print(time.asctime())

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

print(time.strptime("2000/1/1 00:00:00", "%Y/%m/%d %H:%M:%S"))