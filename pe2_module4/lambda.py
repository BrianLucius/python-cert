# two = lambda: 2
# sqr = lambda x: x * x
# pwr = lambda x, y: x ** y

# for a in range(-2, 3):
#     print(sqr(a), end = " ")
#     print(pwr(a, two()))
    
# def print_function(args, fun):
#     for x in args:
#         print('f(', x, ')=', fun(x), sep='')
        
# print_function([x for x in range(-2, 3)], lambda a: 2*a**2 - 4*a + 2)

# list_1 = [x for x in range(5)]
# list_2 = list(map(lambda x,y: 2 ** x, list_1))
# print(list_2)

# for x in map(lambda x: x * x, list_2):
#     print(x, end=' ')
# print()

for y in map(lambda x:x ** 2, [1,2,3,4]):
    print(y)
    
for y in map(lambda x:x ** 2, [x for x in range(1, 5)]):
    print(y)

print(list(map(lambda x:x ** 2, [x for x in range(1, 5)])))

# any_list = [1, 2, 3, 4]
# even_list = list(map(lambda x: x | 1, any_list))
# print(even_list)