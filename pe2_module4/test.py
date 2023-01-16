# def fun(n):
#     for i in range(n):
#         return i
    
# print(fun(10))

# def fun(n):
#     for i in range(n):
#         yield i
    
# for x in fun(10):
#     print(x)

# t = [x for x in fun(10)]
# print(t)

# t = list(fun(10))
# print(t)

# for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
#     print(v, end=" ")
# print()

# for v in (1 if x % 2 == 0 else 0 for x in range(10)):
#     print(v, end=" ")
# print()

def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
