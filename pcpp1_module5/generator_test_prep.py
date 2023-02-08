# def f(a, b):
#     return a(b)

# print(f(lambda x: x and True, 1 > 0))

# v = [1,2,3]
# def g(a, b, m):
#     return m(a,b)
# print(g(1,1,lambda x,y: v[x:y+1]))

vect = ['alpha','bravo','charlie']
new_vect = filter(lambda s: s[-1].upper() in ['A', 'O'], vect)
for x in new_vect:
    print(x[1], end="")