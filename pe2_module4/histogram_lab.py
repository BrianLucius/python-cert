from os import strerror

histogram = {}

try:
    filename = input('Enter a file name: ')
    file = open(filename, 'rt')
    ch = file.read(1).upper()
    while ch != '':
        if ch.isalpha():
            if ch in histogram.keys():
                histogram.update({ch: histogram[ch] + 1})
            else:
                histogram[ch] = 1
        ch = file.read(1).upper()
    file.close()
    
    keys = list(histogram.keys())
    keys.sort()
    for key in keys:
        print(key + ' -> ' + str(histogram[key]))
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
