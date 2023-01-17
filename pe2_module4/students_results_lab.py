from os import strerror

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self, record):
        StudentsDataException.__init__(self)
        self.record = record

class FileEmpty(StudentsDataException):
    def __init__(self, filename):
        StudentsDataException.__init__(self)
        self.filename = filename.split('/')[-1]

students = {}

try:
    filename = input('Input filename to process: ')
    file = open(filename, 'rt')
    line = file.readline().strip()
    
    if line == '':
        raise FileEmpty(filename)
    
    while line != '':
        record = line.split()
        if len(record) != 3:
            raise BadLine(str(record))
        student_name = record[0] + ' ' + record[1]
        if student_name in students.keys():
            students.update({student_name: students[student_name] + float(record[2])})
        else:
            students[student_name] = float(record[2])
        line = file.readline()
        
    for item in sorted(students.items()):
        print(item[0], '\t', item[1])
except FileEmpty as fe:
    print("Error: File \"" + fe.filename + "\" is empty. Try a different file.")
except BadLine as bl:
    print("Error: found incomplete data for row: " + bl.record)
except IOError as e:
    print("I/O error occurred: " + strerror(e.errno))