def combiner(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))

combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')



def combiner(a, b, *args, **kwargs):
    super_combiner(*args, **kwargs)

def super_combiner(*my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_kwargs:', my_kwargs)

combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')


def combiner(a, b, *args, c=20, **kwargs):
    super_combiner(c, *args, **kwargs)

def super_combiner(my_c, *my_args, **my_kwargs):
    print('my_c:', my_c)
    print('my_args:', my_args)
    print('my_kwargs:', my_kwargs)

combiner(10, '20', 40, 60, 30, c=2, argument1=50, argument2='66')