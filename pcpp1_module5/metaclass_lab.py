import time

# def get_instantiation_time(self):
#     return time.strftime('%Y-%m-%d %H:%M:%S.%s', time.gmtime(self.instantiation_time))

class My_Meta(type):
    class_list = []
    
    def __new__(mcs, name, bases, dictionary):
        My_Meta.class_list.append(name)
        
        if 'instantiation_time' not in dictionary:
            dictionary['instantiation_time'] = time.time()
            
        # if 'get_instantiation_time' not in dictionary:
        #     dictionary['get_instantiation_time'] = get_instantiation_time
        
        def get_instantiation_time(self):
            return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(dictionary['instantiation_time']))
        dictionary['get_instantiation_time'] = get_instantiation_time
        
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class Legacy_Class1(metaclass=My_Meta):
    pass
time.sleep(5)

class Legacy_Class2(metaclass=My_Meta):
    pass
time.sleep(3)

class Legacy_Class3(metaclass=My_Meta):
    pass

# print(Legacy_Class1.__dict__)
# print(Legacy_Class2.__dict__)

my_object1 = Legacy_Class1()
print('Obj1 instantiation time:', my_object1.instantiation_time, my_object1.get_instantiation_time())

my_object2 = Legacy_Class2()
print('Obj2 instantiation time:', my_object2.instantiation_time, my_object2.get_instantiation_time())

my_object3 = Legacy_Class3()
print('Obj3 instantiation time:', my_object3.instantiation_time, my_object3.get_instantiation_time())

print('Instantiated class list:', My_Meta.class_list)