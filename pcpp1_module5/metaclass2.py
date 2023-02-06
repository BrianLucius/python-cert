def greetings(self):
    print('Just a greeting function, but it could be something more useful like a check sum')

class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class My_Class1(metaclass=My_Meta):
    pass

class My_Class2(metaclass=My_Meta):
    def greetings(self):
        print('We are ready to greet you!')

myobj1 = My_Class1()
print(My_Class1.__dict__)
myobj1.greetings()

myobj2 = My_Class2()
print(My_Class2.__dict__)
myobj2.greetings()