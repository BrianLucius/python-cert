from random import random, randint, seed

# seed(0)

for i in range(5):
    print(random())
    print(randint(1,9))
    
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

