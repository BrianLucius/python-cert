import copy

class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    
    def __str__(self):
        return "Name: {}, Price: {}, Weight: {}".format(self.name, self.price, self.weight)

candies = [('Lolly Pop', 0.5, 133), ('Licorice', 0.1, 251), ('Chocolate', 1, 601), ('Sours', 0.01, 513), ('Hard candies', 0.3, 433)]

warehouse = []
for treat in candies:
    warehouse.append(Delicacy(*treat))

warehouse2 = copy.deepcopy(warehouse)
for item in warehouse2:
    if item.weight > 300:
        item.price = item.price * 0.80  # 20% discount for weights over 300

print('Source list of candies')
for item in warehouse:
    print(item)

print('*'*15)
print('Proposal')
for item in warehouse2:
    print(item)