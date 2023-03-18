# Napisać klasę Person, która zawiera pola:
#     - imie (str)
#     - nazwisko (str)
#     - adres (str)
#     - wiek (int)
# Dodatkowo klasa posiada metody:
#     - __str__ - zwraca tekst w formacie: "Nazwisko, Imie, adres"
#     - check_is_adult() - zwraca true, jeżeli wiek >= 18
#
# Napisać klasę Customer, która dziedziczy po Person, a dodatkowo:
# Posiada pola:
#     - orders (list)
#     - login (str)
#     - total_order_cost (float)
# Oraz funkcje:
#     - str - wykorzystuje dziedziczony str, a dodatkowo na początku podaje login
#     - add_order(product, cost) - dodaje krotke do listy zamowien
#         Można dodać zamówienie tylko jak użytkownik jest pełnoletni
#         Dodatkowo aktualizuje wartość total_order_cost po dodaniu zamówienia
#     - show_orders() - wyświetla wszystkie zamówienia (jeden pod drugim)



class Person:
    def __init__(self, name, surrname, adress, age):
        self.name = name
        self.surrname = surrname
        self.adress = adress
        self.age = age

    def __str__(self):
        return f"{self.surrname} {self.name} {self.adress}"

    def check_is_adult(self):
        if self.age >= 18:
            return True

class Customer(Person):
    def __init__(self, name, surrname, adress, age, login):
        super().__init__(name, surrname, adress, age)
        self.orders = []
        self.login = login
        self.total_order_cost = 0.0

    def __str__(self):
        return f"{self.login} {super.__str__()}"

    def add_order(self,product, cost):
        if self.check_is_adult():
            self.orders.append(product,cost)



