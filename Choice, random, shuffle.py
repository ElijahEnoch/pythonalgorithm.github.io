import random


choice_list = [ 1, "hello", 1.5, True ]
for i in range(3):
    value = random.choice(choice_list)
    print(value)
