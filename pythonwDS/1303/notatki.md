# Python w Data Science

## Podstawowe informacje

W Pythonie mamy dostępne typy danych:

* str - łańcuch znakowy
* int - liczby całkowite
* bool - prawda/fałsz (logiczny)
* float - liczby zmiennoprzecinkowe

## Szablony instrukcji w Pythonie

Instrukcja sterująca if (możemy mieć kilka ```elif```)

```python
if <warunek>:
    # instrukcje, kiedy warunek jest prawdziwy
elif <warunek>:
    # instrukcje, kiedy poprzedni warunek był fałszywy
    # a aktualnie sprawdzany prawdziwy
else:
    # instrukcje, kiedy żaden warunek nie był prawdziwy
```

Konwersja danych (pamiętamy, że możemy utracić część informacji)

```python
# str -> int
txt = 10
number = int(txt)

# float -> int
num = 11.1
to_str = str(num)
```

## Nazewnictwo

- Funkcje: ```len(x)```, ```print(x)```
- Metody: to funkcje wybranej klasy/wartości np. ```l.append(y)```, ```txt.lower()```, ```d.get(x, y)```
- Atrybuty/Pole: to zmienne należące do klasy (czyli takie, które definiujemy z użyciem ```self```)
- Argument == Parametr
- Wartość: informacja, którą można zapisać np. do zmiennej