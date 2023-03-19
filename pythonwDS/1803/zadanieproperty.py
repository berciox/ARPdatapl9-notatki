# Napisz klasę o nazwie Product, która zawiera pole:
#     - nazwa (str)
#     - kategoria (str)
#     - sn (str)
#     - price (float)
#
# Zmienne sn oraz price są prywatne,
#     a dostęp do nich jest możliwy dzięki getter/setter
#
# Dodatkowo nie można ustawić price na wartość mniejszą niż 0.01
#     (próba ustawienia wartości mniejszej niż 0.01 powoduje ustawienie 0.01)


class Product:
    def __init__(self, nazwa, kategoria, sn, price):
        self.nazwa = nazwa
        self.kategoria = kategoria
        self.__sn = sn
        self.__price = price

    @property
    def sn(self):
        return self.__sn


    @sn.setter
    def sn(self, changesn):
        self.__sn = changesn

    @property
    def price(self):
        return self.__price

    @sn.setter
    def price(self, changeprice):

        if changeprice < 0.01:
            self.__price = 0.01
        else:
            self.__price = changeprice