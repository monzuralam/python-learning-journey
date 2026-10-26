"""
# Variable is a store value in the memory
Rules
1. start with a letter or underscore
2. can contain letters, numbers, and underscores
3. not start with a number
4. meaningfull variable name easy to understand
"""

# integer variable
x = 10 # integer 

print(x)

food_price = 1000

print(f"Food price is {food_price:.2f}")

x, y, z = "Mango", "Grape", "Guava"

print( x, y, z )

# float 
laptop_price = float( 1299.99 )
print(laptop_price)

# memory
print(f"food memory: {id(food_price)}")
print(f"laptop memory: {id(laptop_price)}")

# delete the meory
del laptop_price
print(laptop_price)