from abc import ABC, abstractmethod

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass
    
    @abstractmethod
    def get_scanner_status(self):
        pass
    
class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass
    
    @abstractmethod
    def get_printer_status(self):
        pass
    
class MFD1(Scanner, Printer):
    def __init__(self, printer_serial_number, printer_max_resolution, scanner_serial_number, scanner_max_resolution):
        self.printer_serial_number = printer_serial_number
        self.printer_max_resolution = printer_max_resolution
        self.scanner_serial_number = scanner_serial_number
        self.scanner_max_resolution = scanner_max_resolution
    
    def scan_document(self):
        print('Document has been scanned.')
    
    def get_scanner_status(self):
        print({'scanner_max_resolution':self.scanner_max_resolution, 'scanner_serial_number':self.scanner_serial_number})
    
    def print_document(self):
        print('Document has been printed.')
    
    def get_printer_status(self):
        print({'printer_max_resolution':self.printer_max_resolution, 'printer_serial_number':self.printer_serial_number})

class MFD2(MFD1):
    def print_operation_history(self):
        print('Printed operational history.')

class MFD3(MFD2):
    def send_fax(self):
        print('Sending fax')

mfd1 = MFD1('abc123', 'low', 'cba321', 'low')
print('MFD1:')
mfd1.scan_document()
mfd1.get_scanner_status()
mfd1.print_document()
mfd1.get_printer_status()
print()

mfd2 = MFD2('def456', 'better', 'fed654', 'better')
print('MFD2:')
mfd2.scan_document()
mfd2.get_scanner_status()
mfd2.print_document()
mfd2.get_printer_status()
mfd2.print_operation_history()
print()

mfd3 = MFD3('ghi789', 'premium', 'ihg987', 'premium')
print('MFD3:')
mfd3.scan_document()
mfd3.get_scanner_status()
mfd3.print_document()
mfd3.get_printer_status()
mfd3.print_operation_history()
mfd3.send_fax()
print()