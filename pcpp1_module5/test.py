from datetime import datetime

class Factory(type):
    classes = list()
    def __new__(mcs, name, bases, dictionary):
        dictionary["instantiation_time"] = datetime.now()
        
        def get_instantiation_time():
            return dictionary["instantiation_time"]
        
        dictionary["get_instantiation_time"] = get_instantiation_time
        
        obj = super().__new__(mcs, name, bases, dictionary)
        mcs.classes.append(name)
        return obj



class Test(metaclass=Factory):
    pass
class Test2(metaclass=Factory):
    pass
class Test3(metaclass=Factory):
    pass

t = Test()
t2 = Test2()
t3 = Test3()
print("Test2 get_instantiation_time(): ",t2.get_instantiation_time())
print("Test class has attributes: ",(Test.__dict__))
print("Test2 class has attributes: ",(Test2.__dict__))
print("Test3 class has attributes: ",(Test3.__dict__))
print("list the class names that are instantiated by your metaclass: ",(Factory.classes))