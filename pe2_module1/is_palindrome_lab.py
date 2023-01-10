text = input("Enter some text: ")
is_palindrome = False

text = text.replace(' ','')

for i in range(len(text)//2):
    if text[i].lower() == text[len(text)-1-i].lower():
        is_palindrome = True
    else:
        is_palindrome = False
        break
    
if is_palindrome:
    print("It's a palindrome")
else:
    print("It's not a palindrome")