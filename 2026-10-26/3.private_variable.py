# Private Variable
class Food:
    def __init__(self, name = "Rice", price = "20.00"):
        self.__name = name
        self.__price = price

    def display(self):
        return f"Food: {self.__name} & Price: {self.__price}"

food_init = Food("Beef", "700")
# access via method
print(food_init.display())

# access private variable by classname
print(food_init._Food__name)