from os import strerror

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self):
        super()


class FileEmpty(StudentsDataException):
    def __init__(self):
        super()

students = {}

try:
    filename = input('Input filename to process: ')
    file = open(filename, 'rt')
    line = file.readline()
    if line == '':
        raise(FileEmpty)
    while line != '':
        record = line.split()
        if len(record) != 3:
            raise(BadLine)
        student_name = record[0]+' '+record[1]
        if student_name in students.keys():
            students.update({student_name: students[student_name] + float(record[2])})
        else:
            students[student_name] = float(record[2])
        line = file.readline()
    for item in sorted(students.items()):
        print(item[0], '\t', item[1])
except FileEmpty:
    print("File is empty. Try a different file.")
except BadLine:
    print("Found incomplete data for row: " + str(record))
except IOError as e:
    print("I/O error occurred: " + strerror(e.errno))


# /Users/brian/Repositories/python-cert/pe2_module4/students.txt