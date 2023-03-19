def ending_dec(func):
    def wrapper():
        func()
        print("---KONIEC---")
    return wrapper


@ending_dec
def ala():
    print ("Ala ma kota")


@ending_dec
def dodawanie(a,b):
    return a + b


ala()


