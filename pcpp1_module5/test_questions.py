# class OwnDict(dict):
#     def __setitem__(self, _key, _val):
#         super().__setitem__(_key, _val)
    
#     def update(self, *args, **kwargs):
#         for _key, _val in dict(*args, **kwargs).items():
#             self.__setitem__(_key, _val)

# own_dict = OwnDict()
# own_dict[4] = 1
# own_dict[2] = 0.5
# print(own_dict)


# class OwnList(list):
#     def __setitem__(self, index, value):
#         list.append(self, value)
    
#     def append(self, value):
#         if len(self) > 0:
#             list.__setitem__(self, -1, value)
#         else:
#             list.append(self, value)

# own_list = OwnList()
# own_list.append(3)
# own_list.append(2)
# print(own_list)

# for i in range(1):
#     print("#")
# else:
#     print("#")

# i=0
# while i <= 5:
#     i+=1
#     if i%2 == 0:
#         break
#     print("*")

# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s+= t[i][i]
# print(s)

# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0])

# x = 3
# y = 2
# x = x%y
# x = x%y
# y = y%x
# print(y)

# 1 2 3 4
# 1 4 9 16

# numbers = [0, 2, 7, 9, 10]
# foo = map(lambda num: num **2, numbers)
# print(list(foo))

# def my_fun(n):
#     s = '+'
#     for i in range(n):
#         s += s
#         yield s

# for x in my_fun(2):
#     print(x, end='')

# class A:
#     def __init__(self, v):
#         self.__a = v + 1
# a = A(0)
# print(a.__a)

# try:
#     raise Exception
# except BaseException:
#     print('a')
# except Exception:
#     print('b')
# except:
#     print('c')

class A:
    A = 1
    def __init__(self):
        self.a = 0
print(hasattr(A, 'a'))
