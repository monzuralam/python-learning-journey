"""
Dictionary
"""
fruits = {
    "type": "fruits",
    "apple": 350,
    "banana": 40,
    "guava": 100
}

print('=' * 20)

# length
print(len(fruits))

print('=' * 20)

# create dict using constructor
info = dict(name = 'Monzur Alam', age = 28, position = 'WordPress Developer', colors = ('white', 'black', 'green'))
print(info)

print('=' * 20)

# set default value on the dictionary
info.setdefault('city', 'rangpur')
print(info)
print('='*20)

# access dictionary
print(fruits['banana'])
print(fruits.get('apple')) # 350

print('=' * 20)

# get keys
print(fruits.keys())

# get values
print(fruits.values())

# get Items
print(fruits.items())

# check if key exits on the dict
if "apple" in fruits:
    print("Yes, stock")

print('='*20)

# change item
fruits['apple'] = 360
print(fruits)

# change item by update method
fruits.update({'apple': 350})
print(fruits)
print('='*20)

# add item
fruits['pineapple'] = 100
print(fruits)

# add item via update method as well
fruits.update({'mango': '50'})
print(fruits)
print('='*20)

# add item via unpacking
new_fruits = {"date": 300, "papaya": 60, "cocunut": 80}
print({**fruits, **new_fruits})

# add item via union (|) operator
print(fruits | new_fruits)

# add item via update (|=) operator
update_fruits = fruits | new_fruits
print(update_fruits)

print('='*20)

# remove item by pop(accept key)
fruits.pop('mango')
print(fruits)

# remove last item by popitem() : note: 3.7 remove the last item b
fruits.popitem()
print(fruits)

# del keyword to delete specific key
del fruits['guava']
print(fruits)

# clear the dictionary
fruits.clear()
print(fruits)

# delete the dictionary
# del fruits
# print(fruits)
print('='*20)

foods = {
    "rice": "20",
    "biriyani": "120",
    "polao": "80",
    "chicken_fry": "100",
    "kacchi": "220"
}

# loop the dictionary
for x in foods:
    print(x,':', foods[x])

# loop through the key, value item
for x,y in foods.items():
    print(x, y)

print('='*20)

laptop = {
    "name": "hp",
    "model": "840g5",
    "generation": "10th",
    "ram": "16GB",
    "SSD": "128GB"
}

# copy dictionary using the copy method ( shalow copy )
another_laptop = laptop.copy()
print(another_laptop)

# copy dictionary via dict constructor ( shalow copy )
new_laptop = dict(laptop)
print(new_laptop)

# copy dictionary using the deepcopy method ( deep copy )
import copy
deep_laptop = copy.deepcopy(new_laptop)
print(deep_laptop)

print('='*20)

devices = {
    "laptop": {
        "brand": "Dell",
        "model": "XPS 15",
        "price": 150000
    },
    "smartwatch": {
        "brand": "Apple",
        "model": "Watch Series 10",
        "price": 45000
    },
    "desktop": {
        "brand": "HP",
        "model": "Pavilion Desktop",
        "price": 85000
    },
    "smartphone": {
        "brand": "Samsung",
        "model": "Galaxy S25",
        "price": 95000
    },
    "tablet": {
        "brand": "Apple",
        "model": "iPad Air",
        "price": 75000
    }
}

print(devices)
print('='*20)

# nested loops
for x, obj in devices.items():
    print(x.capitalize())
    print('--------------')

    for y in obj:
        print(obj[y])