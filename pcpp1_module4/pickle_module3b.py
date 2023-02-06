import pickle

def f1():
    print('Hello from the jar!')
    
with open('./pcpp1_module4/function.pckl', 'rb') as file_in:
    data = pickle.load(file_in)

print(type(data))
print(data)
data()