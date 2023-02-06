import pickle

class Cucumber:
    def __init__(self):
        self.size = 'large'
    
    def get_size(self):
        return self.size
    
with open('./pcpp1_module4/cucumber.pckl', 'rb') as file_in:
    data = pickle.load(file_in)

print(type(data))
print(data)
print(data.size)
print(data.get_size())