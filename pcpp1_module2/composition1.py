class Car:
    def __init__(self, engine):
        self.engine = engine

class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power
    
    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))

class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power
    
    def preheat(self):
        print('Switching on glow plugs for preheat')
    
    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))

my_car = Car(GasEngine(4))
my_car.engine.start()
my_car.engine = DieselEngine(2)
my_car.engine.preheat()
my_car.engine.start()
