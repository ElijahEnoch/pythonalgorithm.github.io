import random as r

print([r.choice([True, False]) for i in range(10)])#1

print([i for i in range(10) if r.randrange(0,2)])
