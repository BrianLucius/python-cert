import csv

with open('/Users/brian/Repositories/python-cert/pcpp1_file_processing/contacts.csv', newline='') as csvfile:
    # reader = csv.DictReader(csvfile)
    fieldnames = ['Name', 'Phone']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in reader:
        print(row['Name'], ':', row['Phone'])