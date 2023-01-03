secret_number = 777
guess = None

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while guess != secret_number:
    guess = int(input("Your guess: "))
    if guess == secret_number:
        print('\n'+"The number is: "+str(secret_number))    
    else:
        print("Ha ha! Your're stuck in my loop!")
    
print("Well done, muggle! you are free now.")