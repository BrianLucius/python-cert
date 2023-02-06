import shelve

shelve_name = './pcpp1_module4/first_shelve.shlv'

my_shelve = shelve.open(shelve_name, flag = 'c')
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()

new_shelve = shelve.open(shelve_name)
print("Size:",new_shelve.__sizeof__())
print("Len:", len(new_shelve))
# print(new_shelve['USD'])
for item in new_shelve:
    print('{}: {}'.format(item, new_shelve[item]))
new_shelve.close()