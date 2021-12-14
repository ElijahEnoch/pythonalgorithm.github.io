import random

x = [i for i in range(10)]
print(x)

y = random.sample(x, len(x)//2)
print(y)
