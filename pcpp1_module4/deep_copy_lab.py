import copy

warehouse = list()
warehouse.append({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133})
warehouse.append({'name': 'Licorice', 'price': 0.1, 'weight': 251})
warehouse.append({'name': 'Chocolate', 'price': 1, 'weight': 601})
warehouse.append({'name': 'Sours', 'price': 0.01, 'weight': 513})
warehouse.append({'name': 'Hard candies', 'price': 0.3, 'weight': 433})

print('Source list of candies')
for item in warehouse:
    print(item)

print('*'*15)
print('Proposal')
warehouse2 = copy.deepcopy(warehouse)
for item in warehouse2:
    if item['weight'] > 300:
        item['price'] = item['price'] * 0.80  # 20% discount for weights over 300

for item in warehouse2:
    print(item)