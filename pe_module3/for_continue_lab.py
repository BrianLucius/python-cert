word = input("Enter a word: ")
word = word.upper()

for letter in word:
    if letter in ['A','E','I','O','U']:
        continue
    print(letter)