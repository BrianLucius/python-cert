def is_prime(num):
    if num <= 3:
        return num > 1
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
      if num % i == 0 or num % (i+2) == 0:
          return False
    return True

for i in range(1, 41):
    if is_prime(i+1):
        print(i + 1, end=" ")
print()