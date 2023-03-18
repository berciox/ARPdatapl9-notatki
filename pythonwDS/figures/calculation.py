def my_add(a:int,b:int):
    return str(a+b)

def my_sub(a:int,b:int):
    return str(a-b)

def my_div(a:int,b:int):
    if b == 0:
        print("Nie można podzielić przez 0")
    return str(a/b)
