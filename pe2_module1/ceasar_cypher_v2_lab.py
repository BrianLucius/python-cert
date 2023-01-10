# Caesar cipher.
text = input("Enter your message: ")
shift = ''

while shift == '':
    try:
        shift = input("Enter a shift value between 1 and 25: ")
        if shift.isnumeric:
            if not (1 <= int(shift) <= 25):
                shift = ''
                print("Value must be between 1 and 25. Try again.")
        else:
            shift = ''
            print("Not a valid shift value. Try again.")
    except:
        shift = ''
        print("Not a valid shift value. Try again.")

shift = int(shift)
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
    else:
        code = ord(char) + shift
        if (char.isupper() and code > ord('Z')) or (char.islower() and code > ord('z')):
            code = code - 26
        cipher += chr(code)

print(cipher)