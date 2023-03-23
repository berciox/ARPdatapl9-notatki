# Znak nowej lini: \n
# W przypadku plików linia = tekst + \n
# read(n) = czyta n znaków
# readline(n) = czyta n znaków do \n włącznie (po odczytaniu \n kończy działanie)
# readlines() = zapisuje pobranie linie do listy. 1 element = 1 linia + \n jeżeli występuje


# Przykładowy problem - wyświetl imię i jego długość
# with open("names.txt", "r", encoding="utf-8") as file:
#     # Benefit open
#     for line in file:
#         tmp = line.replace('\n', '')
#         print(f"{tmp} - {len(tmp)}")
#


# words = {}
# with open("reduta.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         for word in line.replace("\n", "").split(" "):
#             if word in words.keys():
#                 words[word] += 1
#             else:
#                 words[word] = 1
#
# print(words)



# Moje chujowe
# from random import randint
# with open("lotto.txt", "a+", encoding="utf-8") as file:
#     values_list =[]
#     n = int(input("Podaj liczbę losowań:"))
#     while n != 0:
#         for i in range(6):
#             values_list.append(randint(1,49))
#         file.writelines(str(values_list)+"\n")
#         n = n-1

from random import randint
print(randint(1, 49))

n = int(input("Podaj ilość losowań: "))

for l in range(n):
    numbers = set()
    while len(numbers) < 6:
        numbers.add(f"{randint(1, 49)} ")

    with open("lotto.txt", "a+", encoding="utf-8") as file:
        file.writelines(numbers)
        file.write("\n")