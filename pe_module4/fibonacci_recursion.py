def fib(num):
    if num < 1:
        return None
    if num < 3:
        return 1
    return fib(num-1) + fib(num-2)

for n in range(1, 10):
    print(n,"->",fib(n))