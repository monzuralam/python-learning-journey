"""
Inheritance allow to define a class that inherits all methods and properties from another class
base/parent class: main class where structure build
child class: inherits from the base class
"""


# base class
class Person:
    def __init__(self, fname, lname, position, location):
        self.fname = fname
        self.lname = lname
        self.position = position
        self.location = location

    def __str__(self):
         return f"""
        Employee Information
        -------------------------------------------
        Name: {self.getname()}
        Position: {self.position}
        Location: {self.location}
        -------------------------------------------
        """

    def getname(self):
        return self.fname + " " + self.lname

    def printname(self):
        print(self.getname())


p1 = Person("Monzur", "Alam", "WordPress Developer", "Banasree, Dhaka")
print(p1)
print(p1.getname())


# child class
class Student(Person):
    def __init__(self, fname, lname, position, location, year):
        # Person.__init__(self, fname, lname, position, location)
        super().__init__(
            fname, lname, position, location
        )  # it's pretty good, don't need to write the parent class name
        self.year = year

    def get_info(self):
        return f"""
        Student Information
        -------------------------------------------
        Name: {self.getname()}
        Position: {self.position}
        Location: {self.location}
        Passing year: {self.year}
        -------------------------------------------
        """

    def print_info(self):
        print(self.get_info())

    def __str__(self):
        return self.get_info()


s1 = Student("Shakil", "Ahmed", "XII", "Rangpur", "2026")
s1.printname()
s1.print_info()