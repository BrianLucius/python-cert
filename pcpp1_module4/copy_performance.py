import copy
import time
import sys

a_list = [(1,2,3) for x in range(1000000)]

print('Object size:',sys.getsizeof(a_list))

print('Single reference copy')
time_start = time.time()
b_list = a_list
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:',id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)

print()

print('Shallow copy')
time_start = time.time()
c_list = a_list[:]
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:',id(a_list), id(c_list))
print('Same memory chunks?', a_list is c_list)

print()

print('Deep copy')
time_start = time.time()
d_list = copy.deepcopy(a_list)
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:',id(a_list), id(d_list))
print('Same memory chunk?', a_list is d_list)