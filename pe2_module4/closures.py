def outer(par):
    loc = par
    
    def inner(x):
        return loc * x
    return inner

var = 2
fun = outer(var)
print(fun(3))