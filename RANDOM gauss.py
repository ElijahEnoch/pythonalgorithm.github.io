import random

sum = 0
for i in range(100):
    value = random.gauss(10, 5)
    sum += value
    avg = sum / (i+1)
    print(value, "\t", avg)
