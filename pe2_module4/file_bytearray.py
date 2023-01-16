from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10-i
    
try:
    bf = open('/Users/brian/Repositories/python-cert/pe2_module4/file.bin','wb')
    bwritten = bf.write(data)
    bf.close()
    print(str(bwritten) + ' bytes written to file.')
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

# readdata = bytearray(10)

try:
    rbf = open('/Users/brian/Repositories/python-cert/pe2_module4/file.bin', 'rb')
    # bread = rbf.readinto(readdata)
    readdata = bytearray(rbf.read())
    rbf.close()
    for i in readdata:
        print(hex(i), end=' ')
    # print('\n' + str(bread) + ' bytes read from file.')
    print('\n' + str(len(readdata)) + ' bytes read from file.')
except IOError as e:
    print("I/O exception occurred: ", strerror(e.errno))