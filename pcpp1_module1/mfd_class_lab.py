class MFD():
    print('I am a multi-function device')

class Scanner(MFD):
    def scan(self):
        print('Scanner class scanning...')

class Printer(MFD):
    def print(self):
        print('Printer class printing...')

class Fax(MFD):
    def send(self):
        print('Faxing class faxing...')
    
    def print(self):
        print('Faxing class printing...')

class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax, Printer):
    pass

device1 = MFD_SPF()
device2 = MFD_SFP()

print('MFD_SPF')
device1.scan()
device1.print()
device1.send()
print()

print('MFD_SFP')
device2.scan()
device2.print()
device2.send()
