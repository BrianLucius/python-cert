class Stack:
    def __init__(self):
        self.__stack_list = []
        
    def push(self, val):
        self.__stack_list.append(val)
        
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
        
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    
    def get_sum(self):
        return self.__sum
        
stack_object = Stack()
stack_object2 = Stack()

stack_object.push(1)
stack_object.push(2)
stack_object.push(3)

stack_object2.push('x')
stack_object2.push('y')
stack_object2.push('z')

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

print(stack_object2.pop())
print(stack_object2.pop())
print(stack_object2.pop())

print('=== Adding Stack ===')
my_stack = AddingStack()
my_stack.push(3)
print('get_sum:', my_stack.get_sum())
my_stack.push(2)
print('get_sum:', my_stack.get_sum())
my_stack.push(1)
print('get_sum:', my_stack.get_sum())

print('pop:', my_stack.pop())
print('get_sum:',my_stack.get_sum())
print('pop:',my_stack.pop())
print('get_sum:',my_stack.get_sum())
print('pop:',my_stack.pop())
print('get_sum:',my_stack.get_sum())