# Zadanie 01
# Napisać funkcję, która zamienić stopnie Celsjusza na Kelwina. Funkcja przyjmuje jako argument temperaturę w C, a funkcja zwraca temperaturę w K. Więcej informacji o konwersji: https://www.rapidtables.org/pl/convert/temperature/how-celsius-to-kelvin.html
#
# Obie wartości maja być typu float

# def conversion(c):
#     return(f"Temperatura w stopniach Kelwina to: {c+273.15}")
# print(conversion(30))


# Zadanie 02
# Napisać funkcję, która jako argument przyjmuje dowolny łańcuch znakowy, a następnie zwraca słownik zliczający ilość wystąpień każdego słowa (kot =/= kota). Podpowiedź możemy użyć metody split(" ").
#
# def count_words(text):
#     words = text.split(" ")
#     word_counts = {}
#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
#     return word_counts
# print(count_words("Ala ma kota, a kot ma pierdolca"))



# Zadanie 03
# Użytkownik podaje trzy liczby całkowite. Następnie program zwraca informację, która z podanych liczb jest największa (dla odważnych - możecie również weryfikować czy dane liczbą są takie same).
#

# a = int(input("Podaj 1 liczbę:"))
# b = int(input("Podaj 2 liczbę:"))
# c = int(input("Podaj 3 liczbę:"))
#
# if a == b == c or a == b or a == c or b == c:
#     print("Podane liczby są równe.")
# else:
#     if a >= b and a >= c:
#         print(f"Największa liczba to {a}")
#     elif b >= a and b >= c:
#         print(f"Największa liczba to {b}")
#     else:
#         print(f"Największa liczba to {c}")


# Zadanie 04
# Napisać program, gdzie użytkownik podaje liczby całkowite i je sumuje. Program działa dopóki użytkownik nie poda liczby ujemnej. Po podaniu liczby ujemnej program wyświetla sumę podanych poprzednich liczb.
#

# suma = 0
#
# while True:
#     liczba = int(input("Podaj liczbę całkowitą: "))
#     if liczba < 0:
#         break
#     suma += liczba
#
# print("Suma podanych liczb to:", suma)








# Zadanie 05
# Napisać funkcję, która konwertuje liczbę z systemu dziesiętnego na binarny (nie używamy funkcji wbudowanych w Pythonie)
#



# def dec_to_bin(n):
#
#     binary = ""
#     while n > 0:
#         bit = n % 2
#         binary = str(bit) + binary
#         n //= 2
#     return binary
#
# print(dec_to_bin(2))












# Zadanie 06
# Użytkownik podaje liczbe całkowitą. Następnie program zwraca sumę CYFR z których składa się podana liczba. Przykładowo: użytkownik podaje 1307, program zwraca 11 (1+3+0+7). Podpowiedź: konwersja na str
#


# def sum_digits(n):
#
#     sum = 0
#     while n > 0:
#         digit = n % 10
#         sum += digit
#         n //= 10
#     return sum
#
# number = int(input("Podaj liczbę całkowitą: "))
# result = sum_digits(number)
# print(f"Suma cyfr liczby {number},to {result}")













# Zadanie 07
# Napisać program, gdzie użytkownik podaje n łańcuchów znakowych (ilość n również definiuje wcześniej użytkownik). Następnie program zwraca informacje ile łańcuchów znakowych jest unikatowych. :)
#
# Przykładowo: użytkownik podał n = 3. Następnie podał trzy łańcuchy znakowe: Kot, Pies, Kot. Program zwróci informacje, że ilość UNIKATOWYCH łańuchów znakowych to: 2.

n = int(input("Ile danych chcesz podać?: "))
my_collection = set()

for i in range(n):
    txt = input(f"Podaj txt {i+1}: ")
    my_collection.add(txt)

print(f"Ilość unikatowych wartości: {len(my_collection)}")