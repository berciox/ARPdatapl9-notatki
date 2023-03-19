def ending_dec(func):
    def wrapper():
        func()
        print(f"---KONIEC---")
    return wrapper


@ending_dec
def ala():
    print (f"Ala ma kota")


@ending_dec
def dodawanie(a,b):
    return a + b


ala()
dodawanie(4,6)

