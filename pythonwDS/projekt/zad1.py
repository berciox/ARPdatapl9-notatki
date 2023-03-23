from random import randint
from datetime import datetime as dt, timedelta as td
n = int(input("Podaj liczbę wierszy do wygenerowania"))


with open("dane_dzienmiesiacrok.txt", "a+", encoding="utf-8") as file:
    for i in range(n):
        file.writelines(dt.now(%H:%M))
