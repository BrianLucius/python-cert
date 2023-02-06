import pickle

a_list = ['a', 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print('Intermediate object type, used to preserve data:', type(bytes))

b_list = pickle.loads(bytes)
print('A type of deserialized object:', type(b_list))
print('Contents:', b_list)


a_dict = {'make':'cadillac', 'model':'XTS', 'trim':'Platinum'}
bytes = pickle.dumps(a_dict)
print('Intermediate object type, used to preserve data:', type(bytes))

b_dict = pickle.loads(bytes)
print('A type of deserialized object:', type(b_dict))
print('Contents:', b_dict)