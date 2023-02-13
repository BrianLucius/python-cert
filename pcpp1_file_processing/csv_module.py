import csv

with open('/Users/brian/Repositories/python-cert/pcpp1_file_processing/contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(','.join(row))