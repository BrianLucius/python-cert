import xml.etree.ElementTree as et

tree = et.parse('/Users/brian/Repositories/python-cert/pcpp1_file_processing/books.xml')
root = tree.getroot()
print('The root tag is: ',root.tag)
print('The root has the following children: ')
for child in root:
    print(child.tag, child.attrib)