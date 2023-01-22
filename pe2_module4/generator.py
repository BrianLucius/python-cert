# for i in range (1, 5, 2):
#     print(i)

# def fun(n):
#     for i in range(n):
#         # return i
#         yield i
    
# for x in fun(6):
#     print(x)

# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2
        
# for x in powers_of_2(8):
#     print(x)
    
# t = [y for y in powers_of_2(8)]
# print(t)

# l = list(powers_of_2(8))
# print(l)

# for i in range(129):
#     if i in powers_of_2(8):
#         print(i)

def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(20))
print(fibs)