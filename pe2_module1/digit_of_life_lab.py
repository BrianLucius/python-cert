bday = ''

while bday == '':
    try:
        bday = input("Enter your birthday in YYYYMMDD format: ")
        if bday.isnumeric:
            if not (6 <= len(bday) <= 8):
                bday = ''
                print("Not a valid date. Try again.")
        else:
            bday = ''
            print("Not a valid date. Try again.")
    except:
        bday = ''
        print("Not a valid date. Try again.")

def digit_of_life(bday):
    digits_sum = 0
    for i in range(len(bday)):
        digits_sum += int(bday[i])
    if len(str(digits_sum)) > 1:
        digits_sum = digit_of_life(str(digits_sum))
    return digits_sum

print(digit_of_life(bday))