hat_list = [1, 2, 3, 4, 5]

new_num = int(input("Enter a replacement number: "))
hat_list[2] = new_num

del hat_list[4]
print("List length: ", len(hat_list))

print(hat_list)