a_string = '10 days to departure'
b_string = '20 days to departure'
c_string = b_string

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
print('c_string identity:', id(c_string))
print('The result of value comparison:', b_string == c_string)
print('The result of identity comparison:', b_string is c_string)

d_string = ['20',' days',' to',' departure']
e_string = ['20',' days',' to',' departure']
print('d_string identity:', id(d_string))
print('e_string identity:', id(e_string))
print('The result of value comparison:', d_string == e_string)
print('The result of identity comparison:', d_string is e_string)