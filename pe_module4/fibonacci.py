def fib(num):
    if num < 1:
        return None
    if num < 3:
        return 1
    
    elem_1 = elem_2 = 1
    for n in range(3, num+1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for n in range(1, 10):
    print(n, "->", fib(n))