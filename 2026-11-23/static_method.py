class Car:
    count = 0

    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
        Car.count += 1

    def __str__(self):
        return f"Name: {self.name}, Model: {self.model}, Color: {self.color}"

    def display_car(self):
        pass

    # creating static method
    def show_count():
        print(Car.count)
        return
    counter = staticmethod(show_count)

c1 = Car('BMW', '2022', 'black')
c2 = Car('Ferari', '2023', 'yellow')
c3 = Car('Audi', '2021', 'red')

c1.counter()
Car.counter()


class Student:
    count = 0

    def __init__(self, name, roll ):
        self.name = name
        self.roll = roll
        Student.count += 1

    def __str__(self):
        return f"Name: {self.name}, Roll: {self.roll}"

    @staticmethod
    def show_count():
        print(Student.count)

s1 = Student('Monzur', 1)
s2 = Student('Shakil', 2)

Student.show_count()