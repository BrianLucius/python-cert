class IntegerList(list):
    
    @staticmethod
    def check_value_type(value):
        if type(value) is not int:
            raise ValueError('Not an integer type')
    
    def __setitem__(self, index, value):
        IntegerList.check_value_type(value)
        list.__setitem__(self, index, value)
    
    def append(self, value):
        IntegerList.check_value_type(value)
        list.append(self, value)
    
    def extend(self, iterable):
        for element in iterable:
            IntegerList.check_value_type(element)
        
        list.extend(self, iterable)

int_list = IntegerList()
int_list.append(66)
int_list.append(22)
print('Appending int elements succeed:', int_list)

int_list[0] = 42
print('Replacing int element succeed:', int_list)

int_list.extend([2, 3])
print('Extending with int elements succeed:', int_list)

try:
    int_list.append('9-10')
except ValueError:
    print('Appending string failed')

try:
    int_list[0] = '10/11'
except ValueError:
    print('Replacing string failed')

try:
    int_list.extend([997, '10/11'])
except ValueError:
    print('Extending list failed')

print('Final Result:', int_list)