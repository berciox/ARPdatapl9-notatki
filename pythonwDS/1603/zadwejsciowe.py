# Napisz funkcję, która przyjmuja łańcuch znakowy
#     (dla ułtawienia: same małe litery)
# Przykładowo: alamakotaakotmapierdolca
# Funkcja ma zwrócić słownik (return), który zawiera informacje w postaci:
#     Klucz - litera
#     Wartość - ilość wystąpień litery w tekście
# Przykładowo: dla klucza "l" wartości to 2

slownik = {}

def lancuch_znakowy(fraza):
    for c in fraza:
        if c not in slownik:
            slownik[c] = fraza.count(c)
    return slownik
print(lancuch_znakowy("alamakotaakotmapierdolca"))