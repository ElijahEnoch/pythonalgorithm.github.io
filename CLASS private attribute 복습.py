class P:
    def __init__(self, name, age, address, tresaure):
        self.name = name
        self.age = age
        self.address = address
        self.__tresaure = tresaure#private attribute

    def pay(self, amount):
        self.__tresaure += amount
        print('now remain {}'.format(self.__tresaure))

Mariah = P('Mariah', 20, 'Seoul', 10000)
Mariah.pay(3000)
