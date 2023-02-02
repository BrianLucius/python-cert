class Car:
    def __init__(self, VIN):
        print('Ordinary __init__ was called for:', VIN)
        self.VIN = VIN
        self.brand = ''
    
    @classmethod
    def including_brand(cls, VIN, brand):
        print('Class method was called')
        _car = cls(VIN)
        _car.brand = brand
        return _car

car1 = Car('ABC123')
car2 = Car.including_brand('DEF987', 'SomeBrand')

print(car1.VIN, car1.brand)
print(car2.VIN, car2.brand)