#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(number)
if number < 0:
    print("the number is negative")
elif number > 0:
    print("the number is positive")
else:
    print("the number is zero")
