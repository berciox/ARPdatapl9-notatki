# Napisz funkcję, która jako PIERWSZY argument przyjmuje rodzaj operacji
#     "suma", "różnica", "iloczyn"
# a następnie wykona sumowanie/odejmowanie/mnożenie wszystkich argumentów
# podanych po pierwszym. Ilość argumentów do obliczeń może być dowolna

def my_func(operation:str, *args):
    result = 0
    if operation == "suma":
        for i in range(1, len(my_func())):
            result += my_func(i)
            print(result)
    elif operation == "roznica":
        for i in range(1, len(my_func())):
            result -= my_func(i)
            print(result)
    elif operation == "iloczyn":
        for i in range(1, len(my_func())):
            result *= my_func(i)
            print(result)
    else:
        return None
my_func("suma", 23, 11, 15, 11)