import random

x = [i for i in range(10)]
print(x)

for i in range(len(x)//2):
    x.remove(random.choice(x))

print(x)
#무작위로 리스트의 반을 선별해서 제거하는 random.choice 
