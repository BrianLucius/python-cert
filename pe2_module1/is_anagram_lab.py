text1 = input("Enter some text: ")
text2 = input("Enter some more text: ")
is_anagram = False

text1 = sorted(text1.replace(' ','').lower())
text2 = sorted(text2.replace(' ','').lower())

if text1 == text2:
    print('Anagrams')
else:
    print('Not anagrams')
