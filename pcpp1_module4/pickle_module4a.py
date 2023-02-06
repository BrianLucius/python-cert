import pickle

class Cucumber:
    def __init__(self):
        self.size = 'small'
    
    def get_size(self):
        return self.size

cucu = Cucumber()

with open('./pcpp1_module4/cucumber.pckl', 'wb') as file_out:
    pickle.dump(cucu, file_out)