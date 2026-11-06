
# arbitrary arguments
def my_cousins(*names):
    print("My cousin is: ", names[2])

my_cousins('Shakil', 'Obaidullah', 'Abdullah')

# *args with regular arguments
def eid_salami(currency, *amounts):
    for amount in amounts:
        print(f"{currency} {amount}")
eid_salami('BDT', '50', '100', '150', '200', '250', '300')

# *args real example
def count_total(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(count_total(1, 5, 7, 9, 11))
print(count_total(20, 40, 60, 80, 100))

# **kwargs
def get_user_info(**details):
    print(details['name'])
    for detail in details.items():
        print(detail)

get_user_info(name = 'monzur alam', age = 28, location = 'dhaka')

# combine *args & **kwargs
def display_data(title, *args, **kwargs):
    print('Title:', title)
    print("Args: ", args)
    print("Kwargs", kwargs)

display_data('*args & **kwargs', '1', '2', name = 'Monzur', location = 'Dhaka')

# unpacking list with *
def sum( a, b, c):
    print( a + b + c)
nums = [1, 2, 4]
sum(*nums)

# unpacking dictionaries with **
def full_name(fname, lname):
    print(f"Hello, {fname} {lname}")

names = {"fname": "Monzur", "lname": "Alam"}
full_name(**names)