# Parent/Base Class
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname, self.lname)
        print('-'*30)


x = Person('Monzur', 'Alam')
x.print_name()

# Child Class
class Student(Person):
    pass

y = Student('Shakil', 'Ahmed')
y.print_name()