import json

# sample json
x =  '{ "name":"John", "age":30, "city":"New York"}'

# load json
y = json.loads(x)

print(y)
print(y['name'])

cars = {
    'name': 'BMW',
    'model': '2024',
    'color': 'black',
    'weight': '500kg'
}

print(json.dumps(cars)) #without indent
print(json.dumps(cars, indent = 4)) # with indent
print(json.dumps(cars, indent = 2, separators = ('.', '='))) # with separator
print(json.dumps(cars, indent = 4, sort_keys = True))