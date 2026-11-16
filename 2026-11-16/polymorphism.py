# Without Polymorphism
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!!!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!!!")


car = Car('BMW', '2024')
car.move()

boat = Boat('Karnaphuly', '2022')
boat.move()

plane = Plane('Biman Bangladesh', '2019')
plane.move()

# with polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Move!!!')

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print(self.model, "Sail")

class Plane(Vehicle):
    def move(self):
        print(self.model, "Fly")

c1 = Car('Ford', 'Mustang')
b1 = Boat('Marbella', 'Luxary')
p1 = Plane('Biman', 'Balaka')

for x in (c1, b1, p1):
    print('+'*30)
    print(x.brand)
    print('='*30)
    print(x.model)
    print('='*30)
    x.move()