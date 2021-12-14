import random


class person:

    def __init__(self, n):
        x = [i for i in range(n)]
        self.x = x

    def __del__(self):
        print("Thanos is death.")

    def FingerSnap(self):
        random.shuffle(self.x)
        del self.x[:int(len(self.x)/2)]
        return self.x

    def __str__(self):
        return "there are {},but {} will remain.".format(len(self.x), int(len(self.x)/2))



def main():
    thanos = person(10)

    print(thanos)
    print(thanos.FingerSnap())

if __name__ == '__main__':
    main()
