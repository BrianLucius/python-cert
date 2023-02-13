import xml.etree.ElementTree as et

root = et.Element('shop')
category = et.SubElement(root, 'category', {'name': 'Vegan Products'})

product_1 = et.SubElement(category, 'product', {'name': 'Good Morning Sunshine'})
product_1_type = et.SubElement(product_1, 'type')
product_1_type.text = 'cereals'
product_1_producer = et.SubElement(product_1, 'producer')
product_1_producer.text = 'OpenEDG Testing Services'
product_1_price = et.SubElement(product_1, 'price')
product_1_price.text = '9.90'
product_1_currency = et.SubElement(product_1, 'currency')
product_1_currency.text = 'USD'

product_2 = et.SubElement(category, 'product', {'name': 'Spaghetti Veganietto'})
product_2_type = et.SubElement(product_2, 'type')
product_2_type.text = 'pasta'
product_2_producer = et.SubElement(product_2, 'producer')
product_2_producer.text = 'Programmers Eat Pasta'
product_2_price = et.SubElement(product_2, 'price')
product_2_price.text = '15.49'
product_2_currency = et.SubElement(product_2, 'currency')
product_2_currency.text = 'EUR'

product_3 = et.SubElement(category, 'product', {'name': 'Fantastic Almond Milk'})
product_3_type = et.SubElement(product_3, 'type')
product_3_type.text = 'beverages'
product_3_producer = et.SubElement(product_3, 'producer')
product_3_producer.text = 'Drinks4Coders Inc.'
product_3_price = et.SubElement(product_3, 'price')
product_3_price.text = '19.75'
product_3_currency = et.SubElement(product_3, 'currency')
product_3_currency.text = 'USD'

et.dump(root)
tree = et.ElementTree(root)
tree.write('/Users/brian/Repositories/python-cert/pcpp1_file_processing/shop.xml', 'UTF-8', True)