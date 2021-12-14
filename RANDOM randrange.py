import random

print("EVEN NUMBERS")
for i in range(3):
    print(random.randrange(0, 101, 2))
print(sep = '\n')

print("ODD NUMBERS")
for i in range(3):
    print(random.randrange(99, 0, -2))

