class Phone:
    def __init__(self, number):
        self.number = number
        
    def turn_on(self):
        return print("mobile phone", self.number, "is turned on.")
    
    def turn_off(self):
        return print("mobile phone is turned off.")
    
    def call(self, number):
        return print("calling:", number)

frank = Phone(number='555-1212')
rose = Phone(number='987-6543')

frank.turn_on()
rose.turn_on()
frank.call('430-0710')
rose.call('989-1826')
frank.turn_off()
rose.turn_off()