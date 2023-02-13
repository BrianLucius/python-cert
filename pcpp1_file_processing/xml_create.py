import xml.etree.ElementTree as et

root = et.Element('data')
movie_1 = et.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
movie_2 = et.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})
et.dump(root)

tree = et.ElementTree(root)
tree.write('/Users/brian/Repositories/python-cert/pcpp1_file_processing/movies2.xml',  'UTF-8', True)