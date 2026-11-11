# None Type
x = None

# print
print(x)

# type check
print(type(x))

# compare
if x is None:
    print("that correct, it's none")
else:
    print("Not correct")

# Bool
print(bool(None))

# functions return none
def hello_function():
    x = 5

x = hello_function()
print(x)