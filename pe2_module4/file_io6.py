from os import strerror

# try:
#     fo = open('/Users/brian/Repositories/python-cert/pe2_module4/writetext.txt', 'wt')
#     for i in range(10):
#         s = "Line #" + str(i) + "\n"
#         for ch in s:
#             fo.write(ch)
#     fo.close()
# except IOError as e:
#     print("I/O error occured:", strerror(e.errno))

try:
    fo = open('/Users/brian/Repositories/python-cert/pe2_module4/writetext2.txt', 'wt')
    for i in range(10):
        s = "Line #" + str(i) + "\n"
        fo.write(s)
    fo.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))