import random

x = [i for i in range(10)]
print(x)

while True:
    x.remove(random.choice(x))
    if len(x) <= 5:
        break

print(x)
