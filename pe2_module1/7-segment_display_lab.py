digits = [['###','# #','# #','# #','###'],
          ['  #','  #','  #','  #','  #'],
          ['###','  #','###','#  ','###'],
          ['###','  #','###','  #','###'],
          ['# #','# #','###','  #','  #'],
          ['###','#  ','###','  #','###'],
          ['###','#  ','###','# #','###'],
          ['###','  #','  #','  #','  #'],
          ['###','# #','###','# #','###'],
          ['###','# #','###','  #','###']]

def display_digits(number):
    for i in range(5):
        for d in number:
            print(digits[int(d)][i], end='  ')
        print('')

entry = ''
while entry.upper() != 'Q':
    try:
        entry = input("Enter a positive integer to display or Q to exit: ")
        if entry.isnumeric():
            display_digits(entry)
        elif entry.upper() != 'Q':
            print("Invalid input. Try again.")
    except:
        print("Invalid value entered. Try again.")

