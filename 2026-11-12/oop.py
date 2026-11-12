# class
class Car:
    # constructor
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # display method
    def display(self):
        print('='*25)
        print(f"Name: {self.name}, color: {self.color}")
        print('='*25)

# create instance
bmw = Car('BMW', 'black')
bmw.display()