class Student:
    def __init__(self, name, surrname):
        self.name = name
        self.surrname = surrname
        self.grades_list = []
        self.avr_grade = 0.0

    def __str__(self):
        return f"{self.name} {self.surrname} - {self.avr_grade}"

    def __int__(self):
        return int(sum(self.grades_list))

    def __float__(self):
        return self.avr_grade

    def add_grade(self, grade):
        if grade in (2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0):
            self.grades_list.append(grade)
            self.avr_grade = sum(self.grades_list) / len(self.grades_list)
            print("Dodano ocenę")
        else:
            print("Ocena nieprawidłowa")

s1 = Student("Jan", "Bąk")
#print(s1.name, s1.surrname, s1.avr_grade)
s1.add_grade(5.0)
s1.add_grade(2.0)
# print(s1.name, s1.surrname, s1.avr_grade)

print(s1.)
