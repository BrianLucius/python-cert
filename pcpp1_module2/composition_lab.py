class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires
    
    def get_vin(self):
        print('VIN number is {}'.format(self.VIN))

class Tires:
    def __init__(self, size):
        self.tire_size = size
        self.tire_pressure = 0
    
    def get_pressure(self):
        print('Tire pressure is {}'.format(self.tire_pressure))
    
    def inflate(self, pressure):
        self.tire_pressure = pressure
        print('Inflated tires to {} pressure'.format(self.tire_pressure))

class City(Tires):
    def __init__(self):
        super().__init__(15)

class OffRoad(Tires):
    def __init__(self):
        super().__init__(18)

class Engine:
    def __init__(self, engine):
        self.engine = engine
        self.state = 'stopped'
    
    def start(self):
        self.state = 'running'
        print('Starting {} engine'.format(self.engine))
    
    def stop(self):
        self.state = 'stopped'
        print('Stopping {} engine'.format(self.engine))
    
    def get_state(self):
        print('{} engine is currently {}'.format(self.engine, self.state))

class Electric(Engine):
    def __init__(self):
        super().__init__('Electric')
    
    def get_state(self):
        super().get_state()

class Gasoline(Engine):
    def __init__(self):
        super().__init__('Gasoline')
    
    def get_state(self):
        super().get_state()

city_car = Vehicle('abc123', Electric(), City())
all_terrain = Vehicle('xyz987', Gasoline(), OffRoad())

print('** City Car **')
city_car.get_vin()
city_car.tires.get_pressure()
city_car.engine.get_state()
city_car.tires.inflate(35)
city_car.engine.start()
city_car.tires.get_pressure()
city_car.engine.get_state()

print('\n** All Terrain Vehicle **')
all_terrain.get_vin()
all_terrain.tires.get_pressure()
all_terrain.engine.get_state()
all_terrain.tires.inflate(65)
all_terrain.engine.start()
all_terrain.tires.get_pressure()
all_terrain.engine.get_state()