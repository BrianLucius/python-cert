word_without_vowels = ""

word = input("Enter a word: ")
word = word.upper()

for letter in word:
    if letter in ['A','E','I','O','U']:
        continue
    word_without_vowels += letter
    
print("The word is: ", word_without_vowels)