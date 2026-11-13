"""
Magic methods are special methods who are start with double underscore & end with double underscore __ like as (__init__, __str__). because of the double underscores, they are called dunder methods.
"""
class Car:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

c1 = Car('BMW', '10M', 'Black')

# without magic methods show the memory address
print(c1)

class Car:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    # str method must return string, otherwise you will get error
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Color: {self.color}"

c2 = Car('BMW', '10M', 'Black')
print(c2)
print('-'*30)

class Car:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    # str method must return string, otherwise you will get error
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Color: {self.color}"

    # repr method control technical representation, meant for developers.
    def __repr__(self):
        return f"Car(name={self.name!r}, 'price={self.price}', 'color={self.color}')" # if use !r then automaticly create quotation('')
    
c3 = Car('Audi', '12M', 'Black')
print(c3)
print(repr(c3))
print('-'*30)

# compare objects ( check two object exact same memory address )
c4 = Car('Audi', '12M', 'Black')
print(c3 == c4)

# change how to compare
class Car:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    # str method must return string, otherwise you will get error
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Color: {self.color}"

    # repr method control technical representation, meant for developers.
    def __repr__(self):
        return f"Car(name={self.name!r}, 'price={self.price}', 'color={self.color}')" # if use !r then automaticly create quotation('')

    # eq method how to compare your objects
    def __eq__(self, other):
        return self.name == other.name and self.color == self.color

c5 = Car('Mercedes', '12M', 'White')
c6 = Car('Mercedes', '11M', 'White')
print(c5 == c6)
print('-'*30)

# add method control what happend when you use an operator like +, on your own objects. this is called operator overloading.
class Car:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    # str method must return string, otherwise you will get error
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Color: {self.color}"

    # repr method control technical representation, meant for developers.
    def __repr__(self):
        return f"Car(name={self.name!r}, 'price={self.price}', 'color={self.color}')" # if use !r then automaticly create quotation('')

    # eq method how to compare your objects
    def __eq__(self, other):
        return self.name == other.name and self.color == self.color

    # add method 
    def __add__(self, other):
        if( ('M' in self.price and 'M' in other.price) or ( 'm' in self.price and 'm' in other.price)):
            return f"{int(self.price.replace('M', '')) + int(other.price.replace('M', ''))}M"
        return self.price + other.price

c7 = Car('Toyota', '10M', 'yellow')
c8 = Car('BMW', '12M', 'Black')
print(c7+c8)
print('-'*30)

# __len__ method controls the built in len() functions
class Company:
    def __init__(self, employees):
        self.employees = employees
    
    def __len__(self):
        return len(self.employees)

c9 = Company(['Monzur', 'Ruhin', 'Rubel', 'Kawsar'])
print(c9)
print(len(c9))
print('-'*30)

# __lt__ method( less than ) controls the < operator does for your objects, without __lt__ method getting error
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age > other.age

p1 = Person('Monzur', 29)
p2 = Person('Kawsar', 30)
print(p1 < p2)
print(p1 > p2)

# sorting with __it__()
p3 = Person('Rayhan', 31)
sorted_person = sorted([p1, p2, p3])
print(sorted_person[0].age) # if not use the __lt__ method the you'll get error
print('-'*30)

# the __contains__ method the controls what the in operator checks in your own objects
class Company:
    def __init__(self, employees):
        self.employees = employees
    
    def __contains__(self, name):
        return name in self.employees

c10 = Company(['Monzur', 'Ruhin', 'Rubel', 'Kawsar'])
print('Monzur' in c10)
print('-'*30)

# __call__ method lets an object be like called a function, using object() syntax
class ClickCounter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

click = ClickCounter()
print(click())
print(click())
print(click())