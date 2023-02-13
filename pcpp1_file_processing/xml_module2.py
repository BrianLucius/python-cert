import xml.etree.ElementTree as et

tree = et.parse('/Users/brian/Repositories/python-cert/pcpp1_file_processing/books.xml')
root = tree.getroot()
print('My Books:\n')
for book in root:
    print('Title: ', book.attrib['title'])
    print('Author: ', book[0].text)
    print('Year: ', book[1].text, '\n')