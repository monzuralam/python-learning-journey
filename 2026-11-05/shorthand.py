a = 10
b = 8

# if condition
if( a > b ): print("A is winner")

# if else condition
print("B is winner") if( a <= b ) else print("Try Again!")

# assign value
bigger = a if( a > b ) else b
print("Bigger is", bigger)

c = 10
# multiple condition check
print("A") if (a > c) else print("=") if ( a == c) else print("C")