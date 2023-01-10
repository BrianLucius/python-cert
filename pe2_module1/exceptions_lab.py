def read_int(prompt, min, max):
    value = ''
    while value == '':
        try:
            value = input(prompt)
            if not min <= int(value) <= max:
                value = ''
                print("Error: the value is not within the permitted range (",min,"...",max,")")
        except:
            value = ''
            print("Error: wrong input")
    return value

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)