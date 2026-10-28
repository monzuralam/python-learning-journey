# String Methods
text = "A quick brown fox jumps over the lazy dog"
location = 'Banasree, Dhaka'

# uppercase 
print(text.upper())

# center
print(text.center(20))
print(text.center(50, '-')) #with charecter
print(location.center(50, '*'))

# count
print(text.count(' ')) # count how many occurs
print(location.count('a'))

# encode
print(text.encode())
print(text.encode('ascii', 'ignore')) # encoding method & ignore

# endswith
profile_photo = 'monzuralam.jpg'
print(profile_photo.endswith('.jpg')) # check image extension
print(profile_photo.endswith(('.jpg', '.png'))) # check multiple value

# expandtabs
salam = 'A\ts\ts\ta\tl\ta\tm\tu\ta\tl\ti\tk\tu\tm'
print(salam)
print(salam.expandtabs())
print(salam.expandtabs(2))
print(salam.expandtabs(0))

# find
print(text.find('cow')) #find cow, if not found then return -1
# print(text.index('cow')) # if not found then return error

# format 
print("Hello, my name is {} & I'm {} years old".format("Monzur Alam", 26)) # default placeholder with value
print("I'm working for {1} & It's located in the {0}".format("Dhaka", "OMH")) # index value
print("It's price: {price:.2f}".format(price=40))

# index
print("Welcome to the Python World".index('Python'))

# isalnum ( check the alphabet numeric )
print('Python3'.isalnum())

# isalpha ( check only the alphabet )
print('Python'.isalpha())

# isascii ( check the ascii number )
print('Hello World'.isascii())

# isdecimal
print("47".isdecimal())

# isdigit
print('3c3'.isdigit())

# isidentifier: a valid identifier can't start with space or number
print('Hello world'.isidentifier())
print('Bangladesh'.isidentifier())

# islower: check the all charecters is lower
print('nice to meet you'.islower())

# isnumeric
print('1111'.isnumeric())

# isprintable
print("Order #11".isprintable())

# isspace
print("    ".isspace())
print('Next World War 3'.isspace())

# istitle
print('Hello World'.istitle())
print('HELLO WORLD'.istitle())

# isupper
print('HELLO NEXT'.isupper())

# join
device = ('Laptop', 'Mobile', 'Headphone')
print(" ".join(device))
print("#".join(device))

# ljust
print("Python".ljust(20), "is a programming language")
print("Breakfast".ljust(15, "="), "done")

# lower
print("HELLO, PYHTON".lower())

# maketrans
soap = "I love the Leona"
mytable = soap.maketrans('L','M')
print(soap.translate(mytable))

username = 'monzur!alam,'
usertable = username.maketrans('','','!,')
print(username.translate(usertable))

# partition
plan = "Today, I'll meet a new people"
print(plan.partition('new'))

# replace
print(plan.replace('new', 'old'))

# split
print(plan.split())

# strip
nexa = "Nexa is a  popular  software.        "
print(nexa.strip())