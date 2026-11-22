class Car:
    totalCar = 0

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        Car.totalCar += 1

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}"

    def start(self):
        print(f"{self.brand} car has been starting")

    def stop(self):
        print(f"{self.brand} car has been starting")

    def brake(self):
        print(f"{self.brand} car braked")

# Built in class attributes
print("Car.__doc__", Car.__doc__)
print("Car.__name__", Car.__name__)
print("Car.__module__", Car.__module__)
print("Car.__bases__", Car.__bases__)
print("Car.__dict___", Car.__dict__)
print('-'*40)

# Access the class attributes
print("Car.totalCar", Car.totalCar)
print('-'*40)

c1 = Car('BMW', '2022', 'black')
c1.model = 2023
print(c1)
c1.start()
c1.brake()

# check attr of the class
print(hasattr(c1, 'brand'))
setattr(c1, 'price', '500k')
print(getattr(c1, 'price'))
delattr(c1, 'price')
print('-'*40)

c2 = Car('Ferari', '2023', 'yellow')
c2.start()
c2.stop()
print(f"Total car is {Car.totalCar}")