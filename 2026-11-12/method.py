class Student:
    def __init__(self, name, age, currentClass = 'V'):
        self.name = name
        self.age = age
        self.currentClass = currentClass

    def __str__(self):
        return f"{self.name} - {self.age} - {self.currentClass}"

    def info(self):
        print('-'*30)
        print('Student Info')
        print('-'*30)
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Class: ', self.currentClass)
        print('-'*30)

s1 = Student("Monzur Alam", "28", "XV")
print(s1) # print beautifully because of __str__ method

# del method
del s1.info

# info
s1.info()

