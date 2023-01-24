# from datetime import date

# date_1 = date(1992, 1, 16)
# date_2 = date(1991, 2, 5)

# print(date_1 - date_2)

# def fun(n):
#     s = '+'
#     for i in range(n):
#         s += s
#         yield s

# for x in fun(2):
#     print(x, end='')

# my_tuple = (0, 1, 2, 3, 4, 5, 6)
# foo = list(filter(lambda x: x-0 and x-1, my_tuple))
# print(foo)

# def I():
#     s = 'abcdef'
#     for c in s[::2]:
#         yield c

# for x in I():
#     print(x, end='')
    
# try:
#     raise Exception
# except BaseException:
#     print("a")
# except Exception:
#     print("b")
# except:
#     print("c")

# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

# print(issubclass(A, C))

# from datetime import timedelta

# delta = timedelta(weeks = 1, days = 7, hours = 11)
# print(delta * 2)

# class A:
#     def __init__(self):
#         pass

# a = A(1)
# print(hasattr(a, 'A'))

# class A:
#     A = 1
#     def __init__(self):
#         self.a = 0

# b = A()
# print(hasattr(A, 'a'))

# x = "\\\"
# print(len(x))

from datetime import datetime

datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)
print(datetime_1 - datetime_2)