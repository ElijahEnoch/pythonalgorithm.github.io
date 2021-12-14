class P:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet#private attribute

    def pay(self, amount):
        self.__wallet -= amount
        print('now remain {}'.format(self.__wallet))

Mariah = P('Mariah', 20, 'Seoul', 10000)
Mariah.pay(3000)
#private attribute is not available outside of class.
