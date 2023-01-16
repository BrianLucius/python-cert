from os import strerror

try:
    ccnt = lcnt = 0
    for line in open('/Users/brian/Repositories/python-cert/pe2_module4/text.txt', 'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:   ", lcnt)
except IOError as e:
    print('I/O error occurrend:  ', strerror(e.errno))