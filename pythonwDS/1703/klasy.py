class Car:
    def __init__(self, color, price, brand):
        self.color = color
        self.price = price
        self.brand = brand
        self.running = False
        self.spec = []

    def __str__(self):
        return f"{self.brand}, {self.color}, {self.price}"


    def switch(self):
        if self.running:
            self.running = False
        else:
            self.running = True

c1 = Car("Czerwony", 589999, "Ferrari")
c2 = Car("Zielony", 80000, "VW")

c1.color = "Srebrny"
print(c1)