import xml.etree.ElementTree

cars_for_sale = xml.etree.ElementTree.parse('/Users/brian/Repositories/python-cert/pcpp1_restful_apis/cars.xml').getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
        print(' =', prop.text)