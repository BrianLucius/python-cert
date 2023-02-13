import xml.etree.ElementTree as et

tree = et.parse('/Users/brian/Repositories/python-cert/pcpp1_file_processing/books.xml')
root = tree.getroot()
for author in root.iter('author'):
    print(author.text)