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
    
    hist_sorted = sorted(histogram.items(), key=lambda x:(-x[1], x[0]))
    
    file = open(filename+'.hist', 'wt')
    for i in range(len(hist_sorted)):
        file.write(hist_sorted[i][0] + ' -> ' + str(hist_sorted[i][1]) + '\n')
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
