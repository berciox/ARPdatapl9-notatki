# Program przyjmuje od użytkownika dwie liczby:
#     1. Liczba prawidłowych odpowiedzi (int)
#     2. Liczba pytań (int)
# Następnie program wyświetla odpowiedni komunikat na konsoli zależnie od % prawidłowych odpowiedzi:
#     100% - 90% : 5.0, 89% - 76% : 4.5, 75% - 70% : 4.0
# #     69% - 60% : 3.5, 59% - 50% : 3.0, 49% - 0% : 2.0



odp = int(input("Wprowadź liczbe prawidlowych odpowiedzi:"))
pyt = int(input("Wprowadź liczbe pytan"))
wyn = float(odp/pyt*100)
if wyn <= 100 and wyn >= 90:
    print ("5.0")
elif wyn < 90 and wyn >= 76:
    print("4.5")
elif wyn < 76 and wyn >= 70:
    print("4.0")
elif wyn < 70 and wyn >= 60:
    print("3.5")
elif wyn < 60 and wyn >= 50:
    print("3.0")
else:
    print("2.0")




# Napisz funkcję o nazwie show_temp_status, która przyjmuje jeden argument typu float
# Następnie zwraca str (nie wykonuje print!) zależnie od wartości podanego argumentu:
#     Poniżej 36.4 - wychłodzenie
#     <36.4 36.8> - norma
#     <36.9, 37.0> - stan podgorączkowy
#     Powyżej 3.71 - gorączka



def show_temp_status(temp):
    if temp < 36.4:
        return "wychłodzenie"
    elif temp >= 36.4 and temp <= 36.8:
        return "norma"
    elif temp >= 36.9 and temp <= 37.0:
        return "stan podgorączkowy"
    else:
        return "gorączka"


print(show_temp_status(38))