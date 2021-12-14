import random

x = [i for i in range(10)]
print(x)
random.shuffle(x)


for i in range(len(x)//2):
    x.pop()

print(x)
