import pickle

def f1():
    print('Hello from the jar!')

f1()

with open('./pcpp1_module4/function.pckl', 'wb') as file_out:
    pickle.dump(f1, file_out)