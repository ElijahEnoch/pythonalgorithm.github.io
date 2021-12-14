import random

x = [i for i in range(10)]
print(x)
random.shuffle(x)

del x[:5]

print(x)
