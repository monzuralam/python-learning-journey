class Person:
    def __init__(self, name, age, profession = 'student'):
        self.name = name
        self.age = age
        self.profession = profession

p1 = Person('Monzur Alam', 25, 'WordPress Developer')
print(p1.age)

# modify the properties
p1.age = 28
print(p1.age)

# add properties
p1.contact = '01712-000000'
print(p1.contact)

# memory location
print(id(p1.contact))

# delete the properties
del p1.contact

# memory location
# print(id(p1.contact))
# print(p1.contact)
