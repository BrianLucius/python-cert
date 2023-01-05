def factorial_function(num):
    if num < 0:
        return None
    if num < 2:
        return 1
    
    return factorial_function(num-1) * num

for t in range(0,6):
    print(t, factorial_function(t))