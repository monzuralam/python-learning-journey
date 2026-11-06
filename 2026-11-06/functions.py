"""
functions
"""
def init():
    print("Hello world")

init()

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 /9;

# call the funciton
print(fahrenheit_to_celsius(88))
print(fahrenheit_to_celsius(66))

# return value
def get_salam():
    return "Assalamualikum"

print(get_salam())

# pass statement
def pass_func():
    pass

pass_func()

# default parameter value
def get_breakfast(name = "rice, lentils"):
    return f"Today's menu is: {name}"

print(get_breakfast('biriyani'))

# keyword arguments
def get_exam_book(exam = 'PSC', book = 'Primary Shikkok Niyog Analysis'):
    return f"Exam: {exam}, Book: {book}"

# call the function with keyword arguments
print(get_exam_book(book = 'NTRCA Nibondhon', exam = 'NTRCA'))

# positional arguments
def get_animal_info(name = 'cow', food = 'staw and hay', profitable = 'Yes'):
    return f"My {name} eats {food} and it's profitable: {profitable}"

print(get_animal_info('goat', 'grass'))
print(get_animal_info('duck', profitable = 'No', food = 'rice, paddy'))

# pass different data types
def my_favorite_food(names):
    for name in names:
        print(name)

my_favorite_food(['beef', 'ruti'])

# positional arguments
def hello_food(name, /):
    print("Food: ", name)

hello_food('Biriyani')

# keyword only arguments
def hello_func_arg(*, name):
    print("Hello, ", name)

hello_func_arg(name='Monzur')

# combine positional & keyword argument
def combo_function(name, /, *, age):
    print(f"Hi, I'm {name} & {age} years old")

combo_function('Monzur', age = 29)
