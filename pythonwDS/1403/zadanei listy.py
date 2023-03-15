# Napisz funkcję manage_list, która przyjmuje dwa argumenty:
#     - Opcja: dodaj, usun
#     - Wartość
# Jeżeli wybraliśmy dodaj, wykonany jest append
# Jeżeli usun - wykonujemy pop()
# Funkcja niczego nie zwraca


animals = ["Kot", "Pies", "Słoń", "Żółw", "Chomik", "Papuga"]
choosen = input("Wpisz add, jezeli dodac zwierze do listy, lub delete, jezeli chcesz usunac zwierze z listy.")

def manage_lists(add, delete):
    if choosen == "add":
        animal = input("Jakie zwierze chciałbyś dodać?")
        animals.append(animal)
    elif choosen == "delete":
        animals.pop()
manage_lists(choosen,0)
print(animals)