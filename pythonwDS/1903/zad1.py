# Zadanie 01
# Napisz funkcję, która jak argument przyjmuje listę liczby całkowitych, a zwraca wartość int jako największa liczba z listy (nie wolno używać max).
#
# Dodatkowo zabezpiecz program, przed błednymi danymi (np. tekst)


#
# def max_value(*args):
#     najwieksza = 0
#     for i in *args:
#         if i == najwieksza or i > najwieksza:
#             najwieksza = i
#         return najwieksza
#
#
# max_value([5,3,2,5,2,1])
















# Zadanie 02
# Napisz moduł, który będzie posiadał funkcje obliczające:
#
# Funkcje kwadratową (zwraca listę rozwiązań)
# Pierwiastek drugiego stopnia z podanej liczby
# N element ciągu harmonicznego (prośba o weryfikacje czym jest ciag z netem)


class Calculations:
    def square_func(self, *args):
        return











# Zadanie 03
# Napisz program, który narysuje trójkąt zależnie od podanego n
#
# Np. n = 3 to wynik jest
#
# *
# **
# ***
# Dodaj dekorator, który dodatkowo dopisze "-----------" na dole trójkąta oraz policzy liczbę *

def line_decorator(func):
    def wrapper(*args, **kwargs):

        return func(*args,**kwargs)
        print("-----------")
        for i in range(n):
            print(sum(n))

    return wrapper


@line_decorator
def draw_tree(n):
    for i in range(n):
        print((i+1) * "*")


draw_tree(5)