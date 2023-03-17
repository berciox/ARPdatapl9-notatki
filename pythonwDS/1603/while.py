# Napisz program, gdzie użytkownik podaje liczbę n (int)
# Następnie program wyświetla wszystkie liczby parzyste od 0 do n (włącznie)

# n = int(input("Podaj liczbę:"))
# i = 0
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     else:
#         False
#     i+=1

# Wykorzystując pętle while, program wyświetli wszystkie pierwiastki
#     liczb od 10 do 2 (włącznie) (n ** 0.5)
# n=10
# while 2<=n<11:
#     print(n**0.5)
#     n-=1


# Napisz program, który sumuje wszystkie liczby całkowite z danego przedziału
# Początek i koniec podaje użytkownik
# Np. start = 10, end = 12, wynik - 33

a = int(input("Podaj początek przedziału:"))
b = int(input("Podaj koniec przedziału:"))
n=0
for i in range(a, b+1):
    n += i
print(n)