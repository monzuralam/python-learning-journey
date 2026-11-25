# There are two type of constructor on the class. default constructor and parameterized constructor

# default constructor
class Device:
    def __init__(self):
        self.name = 'HP PROBOOK'
        self.price = '40K'

    def __str__(self):
        return f"{self.name} - {self.price}"

d1 = Device()
print(f"Name: {d1.name}" )
print(f"Price: {d1.price}")

# parameterized constructor
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.__age = None

    def __str__(self):
        return f"{self.name} - {self.position}"

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

e1 = Employee('Monzur Alam', 'WordPress Developer')
e2 = Employee('Kawser Ali', 'IT Officer')

print(f"Name: {e1.name}")
print(f"Position: {e1.position}")
e1.set_age(25)
print(f"Age {e1.get_age()}")
print(f"Name: {e2.name}")
print(f"Position: {e2.position}")

