from module import suml, prodl
import sys

for p in sys.path:
    print(p)

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print("Sum:", suml(zeroes))
print("Product:", prodl(ones))