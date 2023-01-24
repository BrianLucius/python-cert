import random

class Apple:
    apples_processed = 0
    apples_processed_weight = 0
    
    def __init__(self, weight):
        Apple.apples_processed += 1
        Apple.apples_processed_weight += weight

for i in range(1000):
    if Apple.apples_processed_weight <= 300 - 0.5:
        packing = Apple(random.uniform(0.2, 0.5))
    
print("Apples packed:", Apple.apples_processed)
print("Packed weight:", Apple.apples_processed_weight)