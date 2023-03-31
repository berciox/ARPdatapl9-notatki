from datetime import datetime as dt, timedelta as td
from random import randint, uniform

now = dt.now()
hours_ago = now - td(hours=2)

for _ in range(10):
    with open("dane_20230323.txt", "a", encoding="utf-8") as file:
        time = dt.now() - td(hours=randint(-24,24), minutes=randint(-60,60))
        first_value = str(randint(0,100))
        second_value = str(round(uniform(0.1, 1.0), 2))
        row = time.strftime("%H:%M") + ";" + first_value + ";" + second_value + "\n"
        file.write(row)



