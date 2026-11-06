"""
for loop
"""
fruits = ['apple', 'banana', 'chery']
for x in fruits:
    print(x)

print('='*20)

# loop string
for x in "mango":
    print(x)

print('='*20)

# loop break
for x in fruits:
    if x == 'banana':
        break
    print(x)

print('='*20)

# loop continue
for x in fruits:
    if x == 'banana':
        continue
    print(x)

print('='*20)

# range 
for x in range(10, 15):
    print(x)

print('='*20)

# range with start & increment value
for x in range(5, 50, 5):
    print(x)

print('='*20)

# for else
for x in range( 66, 77, 3):
    print(x)
else:
    print('Done')

print('='*20)

# nested loop
dishes = ['rice', 'curry', 'beef', 'mutton']
for fruit in fruits:
    for dish in dishes:
        print(fruit, dish)

print('='*20)

# pass
for x in [0, 1, 2]:
    pass #todo: later