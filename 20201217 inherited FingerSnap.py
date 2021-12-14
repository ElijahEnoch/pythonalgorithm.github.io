import random


class super:

    def __init__(self, n):
        self.classname = __class__.__name__
        x = [i for i in range(n)]
        self.x = x

    def __del__(self):
        print(__class__.__name__+"Thanos is death.")

    def FingerSnap(self):
        pass

    def __str__(self):
        return "now there are {},but {} will remain.".format(len(self.x), int(len(self.x)/2))

class shuffle(super):

    def FingerSnap(self):
        
        random.shuffle(self.x)
        del self.x[:int(len(self.x)/2)]
        return self.x


class choice(super):

    
    def FingerSnap(self):
        while len(self.x) > 5:
            self.x.remove(random.choice(self.x))
        return self.x

class sample(super):

    def FingerSnap(self):
        self.x = random.sample(self.x, len(self.x)//2)
        return self.x


class newList(super):

    def FingerSnap(self):
        newList = []
        while len(newList) < len(self.x)//2:
            k = self.x[random.randrange(0, len(self.x))]
            if not k in newList:
                newList.append(k)
        return newList


def main():
    thanos1 = newList(10)
    thanos2 = sample(14)
    thanos3 = sample(16)
    thanos4 = shuffle(18) 

    print(thanos1)
    print(thanos1.FingerSnap())
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")

    print(thanos2)
    print(thanos2.FingerSnap())
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")

    print(thanos3)
    print(thanos3.FingerSnap())
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")

    print(thanos4)
    print(thanos4.FingerSnap())
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")

if __name__ == '__main__':
    main()
