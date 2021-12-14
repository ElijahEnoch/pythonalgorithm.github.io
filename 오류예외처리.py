class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")
    #pass


class MyError(Exception):
    def __str__(self):
        return "허용되지않는 별명입니다,"

def say_nick(nick):
    if nick == 'fool':
        raise MyError()
    print(nick)

eagle = Eagle()
eagle.fly()    

try:
    say_nick("천사")
    say_nick("fool")
except MyError as e:
    print("e")

