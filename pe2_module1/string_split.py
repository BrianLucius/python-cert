def mysplit(strng):
    if strng == '':
        return []
    
    split_list = []
    word = ''
    for char in strng:
        if not char.isspace():
            word+=char
        elif word != '':
            split_list.append(word)
            word = ''
    if word != '':
        split_list.append(word)
    return split_list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
