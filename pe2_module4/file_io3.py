from os import strerror

try:
    ccnt = lcnt = 0
    s = open('/Users/brian/Repositories/python-cert/pe2_module4/text.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharters in file:", ccnt)
    print("Lines in file:    ", lcnt)
except IOError as e:
    print("I/O Error occured: ", strerror(e.errno))