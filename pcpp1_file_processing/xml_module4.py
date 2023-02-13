import xml.etree.ElementTree as et

tree = et.parse('/Users/brian/Repositories/python-cert/pcpp1_file_processing/books.xml')
root = tree.getroot()
for book in root.findall('book'):
    print(book.get('title'))