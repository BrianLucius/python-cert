class Base_Computer:
    def __init__(self, serial_number):
        self.serial_number = serial_number

class Personal_Computer(Base_Computer):
    def __init__(self, sn, connection):
        super().__init__(sn)
        self.connection = connection
        print('The computer costs $1000')

class Connection:
    def __init__(self, speed):
        self.speed = speed
    
    def download(self):
        print('Downloading at {}'.format(self.speed))

class DialUp(Connection):
    def __init__(self):
        super().__init__('9600bit/s')
    
    def download(self):
        print('Dialling the access number... '.ljust(40), end = '')
        super().download()

class ADSL(Connection):
    def __init__(self):
        super().__init__('2Mbit/s')
    
    def download(self):
        print('Waking up modem... '.ljust(40), end = '')
        super().download()

class Ethernet(Connection):
    def __init__(self):
        super().__init__('10Mbit/s')
    
    def download(self):
        print('Constantly connected...'.ljust(40), end = '')
        super().download()

my_computer = Personal_Computer('1995', DialUp())
my_computer.connection.download()

my_computer.connection = ADSL()
my_computer.connection.download()

my_computer.connection = Ethernet()
my_computer.connection.download()