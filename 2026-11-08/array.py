# python doesn't support built in array, python list can be used instead of array
cars = ["BMW", "TOYOTA", "FERARI", "VOLVO", "FORD"]
print(cars)

print(len(cars)) # array lenght

# loop
for car in cars:
    print(car.capitalize())

# add item
cars.insert(1, 'MERCIDIS')
cars.append('NISSAN')
print(cars)

# remove item
cars.pop(1) # remove by index
print(cars)
cars.remove('VOLVO') # remove by name
print(cars)
