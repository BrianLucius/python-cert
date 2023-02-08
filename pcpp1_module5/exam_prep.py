# header = 2* '+-' + '+'
# plus = 0
# for x in header:
#     if not x in header:
#         plus += 1
# print(plus)

# class Control:
#     my_ID = 1
    
#     def say(self):
#         return self.my_ID

# class Button(Control):
#     my_ID = 2

# class Radio(Button):
#     def say(self):
#         return -self.my_ID

# selection = Radio()
# element = Control()
# start = Button()

# print(selection.my_ID == 2)
# print(isinstance(start, Button))
# print(start.my_ID == -2)
# print(selection is element)

# ###############

# class Un:
#     value = "Ein"
    
#     def say(self):
#         return self.value.lower()
    
# class Deux(Un):
#     value = "zwei"

# class Troi(Un):
#     def say(self):
#         return self.value.upper()

# class Quatre(Troi, Deux):
#     pass

# d = Quatre()
# b = Deux()

# print(d.say() == 'ZWEI')
# print(isinstance(d, Un))
# print(Troi in Quatre.__bases__)

# class Example:
#     def __str__(self):
#         return __name__
# thing = Example()
# print(thing)

def boolean(op):
    return op(False, True)
print(boolean(lambda x,y: x if x else y))