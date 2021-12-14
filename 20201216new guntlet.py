import random as r

def killHalf(listx):
    lenList = len(listx)
    resultList = []
    while True:
        if len(resultList) < lenList//2:
            k = listx[r.randrange(0, lenList)]
            if not(k in resultList):
                resultList.append(k)
        else:
            break
    return resultList
print(killHalf([1, 2, 3, 4, 5, 6]))
    
