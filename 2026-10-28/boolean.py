# It's return a True or False value
print(10 > 9)

print(bool(True))

print(bool('Hello world'))

print(bool(10))

print(10 < 80)

print(bool(('Apple', 'Banana')))

# false value return
print(bool(False))
print(bool(None))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# functions
def my_functions():
    return True

if my_functions():
    print("Yes") 
else:
    print("No")