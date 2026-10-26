"""
Numbers
- types: int, float, complex
- check type by type(variable)
- random
"""

# int
pen_price = int(15.00)
print(f"Pen price: {pen_price} & type: {type(pen_price)}")

# float
notebook_price = float(19.99)
print(f"Notebook price {notebook_price} & type {type(notebook_price)}")

# complex
complex_price = complex('2+4j')
print(f"Complex price: {complex_price} & type {type(complex_price)}")

# random number
import random

# specific range
print(random.randrange(1, 100))

# Binary number
bin_number = 0b1010;
print(f"Binary Number: {bin_number} & type: {type(bin_number)}")

# Octal Number
oct_number = 0O110
print(f"Octal Number: {oct_number} & type {type(oct_number)}")

# Hexadecimal Number
hexa_number = 0XA4
print(f"Hexa number: {hexa_number} & type {type(hexa_number)}")