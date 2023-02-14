import csv

summary_report = {}

with open('/Users/brian/Repositories/python-cert/pcpp1_file_processing/exam_results.csv', newline='') as csvinfile:
    reader = csv.DictReader(csvinfile, delimiter=',')
    for row in reader:
        if row['Exam Name'] not in summary_report:
            summary_report[row['Exam Name']] = {'cid':[], 'Pass': 0, 'Fail': 0, 'best': 0, 'worst': 100}
        
        if row['Candidate ID'] not in summary_report[row['Exam Name']]['cid']:
            summary_report[row['Exam Name']]['cid'].append(row['Candidate ID'])
        
        summary_report[row['Exam Name']][row['Grade']] += 1
        
        if int(row['Score']) > summary_report[row['Exam Name']]['best']:
            summary_report[row['Exam Name']]['best'] = int(row['Score'])
        
        if int(row['Score']) < summary_report[row['Exam Name']]['worst']:
            summary_report[row['Exam Name']]['worst'] = int(row['Score'])

with open('/Users/brian/Repositories/python-cert/pcpp1_file_processing/exam_report.csv', 'w', newline='') as csvoutfile:
    outfieldnames = ['Exam Name', 'Number of Candidates', 'Number of Passed Exams', 'Number of Failed Exams', 'Best Score', 'Worst Score']
    writer = csv.DictWriter(csvoutfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=outfieldnames)
    writer.writeheader()
    
    for item in summary_report:
        writer.writerow({'Exam Name': item
                        , 'Number of Candidates': len(summary_report[item]['cid'])
                        , 'Number of Passed Exams': summary_report[item]['Pass']
                        , 'Number of Failed Exams': summary_report[item]['Fail']
                        , 'Best Score': summary_report[item]['best']
                        , 'Worst Score': summary_report[item]['worst']})