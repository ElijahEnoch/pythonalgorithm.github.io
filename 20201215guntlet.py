import random as r

def killHalf(listx):
    lenList = len(listx)
    r.shuffle(listx)
    while True:
        listx.pop()
        if lenList/2 >= len(listx):
            break
    return listx
print(killHalf([1, 2, 3, 4, 5, 6]))
    
