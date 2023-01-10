text1 = input("Enter a word: ")
text2 = input("Enter the character list: ")

text1 = ''.join(sorted(text1.lower()))
text2 = ''.join(sorted(text2.lower()))

contains = False
start_pos = 0

for char in text1:
    start_pos = text2.find(char, start_pos)
    if start_pos >= 0:
        start_pos += 1
        contains = True
    else:
        contains = False
        break

if contains:
    print('Yes')
else:
    print('No')