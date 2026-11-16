class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if( age > 0 ):
            self.__age = age
        else:
            print("Must Positive Number")

p1 = Person('Monzur', 29)
print(p1.name)
# print(p1.__age) # generate error
print(p1.get_age())

p1.set_age(20)
print(p1.get_age())

class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0
    
    def get_grade(self):
        print(self.__grade)
    
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must between 0 to 100")

    def get_status(self):
        if self.__grade >= 60:
            print("Passed")
        else:
            print("Failed")

print('-'*30)
s1 = Student('Shakil')
s1.set_grade(59)
s1.get_grade()
s1.get_status()