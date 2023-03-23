# Zadanie 01
# Napisz funkcję, która jak argument przyjmuje listę liczby całkowitych, a zwraca wartość int jako największa liczba z listy (nie wolno używać max).
#
# Dodatkowo zabezpiecz program, przed błednymi danymi (np. tekst)

# def find_max(numbers: list) -> float:
#     try:
#         current_max = float(numbers[0])
#     except ValueError:
#         print("Błedne dane!")
#         exit(-999)
#     if len(numbers) == 1:
#         return current_max
#     else:
#         for i in range(1, len(numbers)):
#             try:
#                 if current_max < numbers[i]:
#                     current_max = float(numbers[i])
#             except TypeError:
#                 continue
#         return current_max
#
#
#
# n = [1,4,1,5,6]
# print(find_max(n))
















# Zadanie 02
# Napisz moduł, który będzie posiadał funkcje obliczające:
#
# Funkcje kwadratową (zwraca listę rozwiązań)
# Pierwiastek drugiego stopnia z podanej liczby
# N element ciągu harmonicznego (prośba o weryfikacje czym jest ciag z netem)










# Zadanie 03
# Napisz program, który narysuje trójkąt zależnie od podanego n
#
# Np. n = 3 to wynik jest
#
# *
# **
# ***
# Dodaj dekorator, który dodatkowo dopisze "-----------" na dole trójkąta oraz policzy liczbę *

# def line_decorator(func):
#     def wrapper(*args, **kwargs):
#
#         return func(*args,**kwargs)
#         print("-----------")
#         for i in range(n):
#             print(sum(n))
#
#     return wrapper
#
#
# @line_decorator
# def draw_tree(n):
#     for i in range(n):
#         print((i+1) * "*")
#
#
# draw_tree(5)
def trigger_base(func):
    def wrapper (*args, **kwargs):
        func(*args, **kwargs)
        print("--------------------")
        count_of_star = 0
        for i in range(1, args[0]+1):
            count_of_star += i
        print(f"Suma fwiazdek: {count_of_star}")
    return wrapper

@trigger_base
def print_asterix(n:int):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end = "")
        print()

print_asterix(7)