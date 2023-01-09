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
        for d in str(number):
            print(digits[int(d)][i], end=' ')
        print('')

entry = 0
while entry >= 0:
    try:
        entry = int(input("Enter a positive integer to display, or a negative value to exit: "))
        if entry >= 0:
            display_digits(entry)
    except:
        print("Invalid value entered. Try again.")

