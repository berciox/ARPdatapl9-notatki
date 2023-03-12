# a = int(input("Podaj liczbę"))
# b = a % 2
# if b == 0:
#     print("Liczba jest podzielna przez 2")
# else:
#     print("Liczba nie jest podzielna przez 2")

c = int(input("Podaj liczbę"))

if c % 3 == 0 and c % 5 ==0:
    print("Pif paf")
elif c % 3 == 0 and c % 5 != 0:
    print("Pif")
elif c % 3 != 0 and c % 5 == 0:
    print("Paf")
else:
    print("Twoja liczba to:", c)