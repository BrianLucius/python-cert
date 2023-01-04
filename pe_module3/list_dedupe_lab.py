my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
deduped_list = []

for i in my_list:
    if i not in deduped_list:
        deduped_list.append(i)

print("The list with unique elements only:")
print(deduped_list)