# Napisz funkcję manage_list, która przyjmuje dwa argumenty:
#     - Opcja: dodaj, usun
#     - Wartość
# Jeżeli wybraliśmy dodaj, wykonany jest append
# Jeżeli usun - wykonujemy pop()
# Funkcja niczego nie zwraca


animals = ["Kot", "Pies", "Słoń", "Żółw", "Chomik", "Papuga"]
choosen = ["add", "delete"]
animal = input()
def manage_lists(add, delete):
    if choosen == "add":
        animals.append("świnia")