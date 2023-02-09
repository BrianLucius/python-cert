# class Package:
#     spam = ''
    
#     def __init__(self, content):
#         Package.spam += content + ';'

# envelope_1 = Package('Cap')
# envelope_2 = Package('Tran')
# print(envelope_2.spam)

# class Collection:
#     __stamps = 2
#     coins = 4
    
#     def __init__(self, stuff):
#         self.stuff = stuff
    
#     def dispose(self):
#         del self.stuff
    
#     def __action(self):
#         pass
    
#     def get(self):
#         return self.stuff
    
#     def print(self):
#         # print(self.get())
#         print(Collection.get(self))

# binder = Collection(1)
# # print(binder.get())
# binder.print()
# print(binder.__dict__)
# binder.dispose()

# binder._Collection__stamps +=1
# Collection._Collection__stamps += 1

# Collection._Collection__action()
# binder._Collection__action()

# print(binder.__dict__)
# print(Collection.__dict__)
# print('stuff' in binder.__dict__)
# print(len(binder.__dict__) > 0)
# print(Collection.__dict__['dispose'])
# print(binder.__dict__['dispose'])

# class Ceil:
#     Token = 1
    
#     def __init__():
#         print(True)
    
#     def get_token(self):
#         return 1

# class Floor(Ceil):
#     def get_token(self):
#         return 2

#     def set_token(self):
#         pass

# holder = Floor()
# print(hasattr(holder, 'Token'), hasattr(Ceil,'set_token'))

# test = Ceil()

# alpha "Alpha"
# say - lower

# gamma "Alpha"        beta "Beta"
# say-upper           say-lower

# delta
# gamma, beta
# say-upper

# class Team:
#     def show_ID(self):
#         print(self.get_ID())
    
#     def get_ID(self):
#         return('anonymous')

# class A(Team):
#     def get_ID(self):
#         return "Alpha"

# a = A()
# a.show_ID()

# class Top:
#     pass

# class Left(Top):
#     pass

# class Right(Top):
#     pass

# class Bottom(Left, Top):
#     pass

# class Alpha:
#     value = "Alpha"
#     def say(self):
#         return self.value.lower()

# class Beta(Alpha):
#     value = "Beta"


# class Gamma(Alpha):
#     def say(self):
#         return self.value.upper()

# class Delta(Gamma, Beta):
#     pass

# d = Delta()
# b = Beta()
# # print(d.say())
# # print(Delta.__bases__)
# print(d.__dict__)
# print(b.__dict__)

import inspect 

class Cat:
    Species = 1
    
    def __init__(self):
        print('Cat:',__name__)
        self.CatInstance = 1.414
    
    def get_species(self):
        return 'kitty'
    
class Tiger(Cat):
    def __init__(self):
        super().__init__()
        print('Species:',self.Species)
        print('Tiger:',__name__)
        self.TigerInstance = 3.14
    
    def get_species(self):
        return 'tiggy'
    
    def set_species(self):
        pass
    
creature = Tiger()
print(creature.Species)
print(hasattr(creature, "Species"), hasattr(Cat, "set_species"))
print(creature.__dict__)
print(inspect.getmembers(creature))