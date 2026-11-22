class Car:
    totalCar = 0
    condition = 'good'

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

    @classmethod
    def change_condition(cls, condition):
        cls.condition = condition

    @staticmethod
    def is_valid_price(price):
        return price > 0

Car.change_condition('Bad')
print(Car.condition)