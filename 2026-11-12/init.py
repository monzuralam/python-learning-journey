# Food Class
class Food:
    # constructor method
    def __init__(self, name, quantity = 1):
        self.name = name
        self.quantity = quantity

    # display
    def display(self):
        print('-'*30)
        print(f"{self.name}:{self.quantity}")
        print('-'*30)

food = Food('Sweet')
print(food.name)
food.display()

f1 = Food('Cake', 10)
f1.display()

# self name can be anything but need to keep the first parameter
class Laptop:

    def __init__(nexa, name, brand, price):
        nexa.name = name
        nexa.brand = brand
        nexa.price = price

    def info(alpha):
        print('-'*30)
        print('Details Information')
        print('-'*30)
        print('Name: ', alpha.name)
        print('Brand: ', alpha.brand)
        print('Price: ', alpha.price)
        print('-'*30)

l1 = Laptop("HP Probook 840g7", "hp", 40)
l1.info()

add = input("Do you add another one(yes or y): ")
if( add.lower() == 'yes' or add.lower() == 'y'  ):
    name = input("Enter your laptop name: ")
    brand = input("Enter your brand name: ")
    price = input("Enter your price name: ")

    l2 = Laptop(name, brand, price)
    l2.info()
else:
    print("Thanks")