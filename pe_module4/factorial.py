def factorial_function(num):
    if num < 0:
        return None
    if num < 2:
        return 1
    
    fac = 1
    for n in range(2, num+1):
        fac *= n
    return fac

for t in range(0,6):
    print(t, factorial_function(t))