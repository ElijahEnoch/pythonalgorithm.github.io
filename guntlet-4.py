import random

x = [i for i in range(10)]
print(x)
random.shuffle(x)

x[:5] = []

print(x)
