dictionary = {"dog":"chien", "horse":"cheval", "cat":"chat"}

for key in sorted(dictionary.keys()):
    print(key, '->', dictionary[key])
    
for english, french in sorted(dictionary.items()):
    print(english, "->", french)
    
for french in sorted(dictionary.values()):
    print(french)
    
dictionary['cat'] = 'minou'
print(dictionary)

dictionary['swan'] = 'cygne'
print(dictionary)

dictionary.update({"duck": "canard"})
print(dictionary)

del dictionary['dog']
print(dictionary)

dictionary.popitem()
print(dictionary)