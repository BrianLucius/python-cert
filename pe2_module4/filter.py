# from random import seed, randint

# seed()
# data = [randint(-10, 10) for x in range(5)]
# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
# print(data)
# print(filtered)

numbers = (1, 2, 5, 9, 15)

def filter_numbers(num):
    nums = (1, 5, 17)
    if num in nums:
        return True
    else:
        return False
    
filtered_numbers = filter(filter_numbers, numbers)
for n in filtered_numbers:
    print(n)