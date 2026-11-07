"""
lambda function ( anonymous function )
"""

# single arguments
sum = lambda x: x + 1

print(sum(10))

# double arguments
mul = lambda a, b: a * b
print(mul(10, 5))


def my_function(n):
    return lambda a: a * n


doubler = my_function(2)
tripler = my_function(3)
print(doubler(11))
print(tripler(11))

# lambda with built in function map, filter, sorted,
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# double
double = list(map(lambda number: number * 2, numbers))  # noqa: C417
print(double)

even_numbers = list( filter( lambda number: number % 2 == 0 , numbers))
print(even_numbers)

students = [('Monzur', 42), ('Ruhin', 41), ('Rubel', 60)]
# sort by numeric 
sorted_students = sorted( students, key=lambda x: x[1])
print(sorted_students)

fruits = ['banana', 'guava', 'mango', 'pineapple', 'woodapple', 'chery']

# sort by length
sorted_fruits = sorted( fruits, key = lambda x : len(x))
print(sorted_fruits)

# sort by alphabetically
asc_fruits = sorted( fruits, key = lambda x : x)
print(asc_fruits)